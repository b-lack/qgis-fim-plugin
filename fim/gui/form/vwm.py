import os
import copy
from PyQt5.QtCore import QTimer

from qgis.core import QgsMessageLog, QgsPointXY, QgsPoint
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog, QScroller
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import QtGui

from jsonschema import Draft7Validator, exceptions

from ...utils.helper import Utils
from .chips import Chips

UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'vwm.ui'))

class VWM(QtWidgets.QWidget, UI_CLASS):
    """VWM."""

    save = pyqtSignal(object)
    save_data = pyqtSignal(object)

    def __init__(self, interface, schema, info_browser):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.updating = False

        self.interface = interface
        self.schema = schema
        self.info_browser = info_browser

        self.isSetup = False

        self.validationTimer = None

        self.vwmTabs.currentChanged.connect(self.change_tab)
        
        QScroller.grabGesture(self.scrollArea_general, QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_coordinates, QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_baumplot1, QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_landmarken1, QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_baumplot2, QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_landmarken2, QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_transekt, QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_verjuengungstransekt, QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_weiserpflanzen, QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_bestockung, QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_bodenvegetation, QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_stoerung, QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_bestandesbeschreibung, QScroller.LeftMouseButtonGesture)

        self.show()

    def change_tab(self, tab):
        """Change the tab."""

        self.update_info()
        self.cancelConnections()

    def cancelConnections(self):
        """Cancel connections."""

        if hasattr(self, 'nav'):
            self.nav.cancelConnection(True)
            
    def update_info(self):
        """Update the info browser."""

        self.info_browser.clear()

        current_tab_schema = self.getSchemaByCurrentTab()
        if current_tab_schema is not None:
            self.info_browser.append("<h1>" + str(current_tab_schema['title'] + "</h1>"))
            if 'description' in current_tab_schema:
                self.info_browser.append("<p>" + str(current_tab_schema['description']) + "</p>")

    def updateJson(self, json):
        """Update the json."""

        self.updating = True

        # Focus Tab 0
        self.vwmTabs.setCurrentIndex(0)

        self.json = json
        self.setUp()

        self.updating = False

    def validateAll(self):
        """Validate the whole json."""
        
        v = Draft7Validator(self.schema)

        self.schemaErrors = sorted(v.iter_errors(self.json), key=lambda e: e.path)
        lfbErrors = self.lfbLayers()

        for error in lfbErrors:
            self.schemaErrors.append(error)

        self.cancelConnections()

        self.save_data.emit(self.schemaErrors)
        self.save_json()

    def save_json(self):
        """Save the json."""

        if self.updating == False:
            self.save.emit(self.json)

    def nextTab(self):
        """Go to the next tab."""

        self.vwmTabs.setCurrentIndex(self.vwmTabs.currentIndex() + 1)
    
    def previousTab(self):
        """Go to the previous tab."""

        self.vwmTabs.setCurrentIndex(self.vwmTabs.currentIndex() - 1)


    def gnavs_default_settings(self):
        return {
            "degUnits": "gon",
            "meassurementSetting": 100,
            "bestMeassurementSetting": 70,
            "aggregationType": 'mean',
            "sortingValues": [
                {"name": "Quality", "value": "qualityIndicator", "direction": True, "active": True},

                {"name": "PDOP", "value": "pdop", "direction": True, "active": True},
                {"name": "HDOP", "value": "hdop", "direction": True, "active": True},
                
                {"name": "Satellites Used", "value": "satellitesUsed", "direction": False, "active": True}
            ],
        }
    
    def getSchemaByCurrentTab(self):
        """Get the schema by the current tab."""

        tabNr = self.vwmTabs.currentIndex()

        key = list(self.schema['properties'])[tabNr]
       
        return self.schema['properties'][key]

    def aggregatedValuesChanged(self, gpsInfos):
        """Update the aggregated values"""

        from gnavs.gui.measurement.aggregation import Aggregation

        from gnavs.utils.utils import Utils as ganvs_utils

        aggregation = Aggregation(self.interface, self.gnavs_default_settings())
        aggregated = aggregation.aggregate(gpsInfos)

        #self.precisionNote.updateIndicator(gpsInfos)
        self.precisionNote.update(aggregated)

        if aggregated['longitude'] == 0 or aggregated['latitude'] == 0:
            return

        position = QgsPointXY(QgsPoint(aggregated['longitude'], aggregated['latitude']))
        ganvs_utils.clearLayer('lfb-tmp-position', 'point')
        ganvs_utils.drawPosition('lfb-tmp-position', position)

        self.json['coordinates']['istgeom_x'] = aggregated['latitude']
        self.json['coordinates']['istgeom_y'] = aggregated['longitude']
        self.json['coordinates']['istgeom_elev'] = aggregated['elevation']
        self.json['coordinates']['istgeom_hdop'] = aggregated['hdop']
        self.json['coordinates']['istgeom_vdop'] = aggregated['vdop']
        #self.json['istgeom_pdop'] = aggregated['pdop']
        self.json['coordinates']['istgeom_sat'] = int(aggregated['satellitesUsed'])

        #self.inputChanged.emit(self.json, self.attr, True)

        self.setUpTextField('istgeom_y', 'coordinates', 'istgeom_y', None, None, lambda: self.validateTab('coordinates', 1))
        self.setUpTextField('istgeom_x', 'coordinates', 'istgeom_x', None, None, lambda: self.validateTab('coordinates', 1))
        self.setUpTextField('istgeom_elev', 'coordinates', 'istgeom_elev', None, None, lambda: self.validateTab('coordinates', 1))
        self.setUpTextField('istgeom_sat', 'coordinates', 'istgeom_sat', None, None, lambda: self.validateTab('coordinates', 1))
        self.setUpTextField('istgeom_hdop', 'coordinates', 'istgeom_hdop', None, None, lambda: self.validateTab('coordinates', 1))
        self.setUpTextField('istgeom_vdop', 'coordinates', 'istgeom_vdop', None, None, lambda: self.validateTab('coordinates', 1))

    def setUp(self):
        """Set up the form."""

        if self.isSetup == False:
            if Utils.pluginAvailable('gnavs'):
                from gnavs.gui.recording.recording import Recording
                from gnavs.gui.measurement.precision import PrecisionNote
                from gnavs.gui.navigate.selection import Selection

                # General

                self.nav = Recording(self.interface, False, self.gnavs_default_settings())
                self.nav.toggleButtonsChanged('navigation')
                self.nav.toggleFocus(True)
                
                self.gnavs_navigation.addWidget(self.nav)
                selection = Selection(self.interface, True, "gon")
                self.gnavs_navigation.addWidget(selection)
                self.nav.currentPositionChanged.connect(selection.updateCoordinates)

                rec = Recording(self.interface, True, self.gnavs_default_settings())
                rec.aggregatedValuesChanged.connect(self.aggregatedValuesChanged)
                self.gnavs_recording.addWidget(rec)
                self.precisionNote = PrecisionNote(self.interface)
                self.gnavs_recording.addWidget(self.precisionNote)
            else:
                # PLACEHOLDER
                pass
        
        

        self.setUpTextField('spaufsucheaufnahmetruppkuerzel', 'general', 'spaufsucheaufnahmetruppkuerzel', None, None, lambda: self.validateTab('general', 0))
        self.setUpTextField('spaufsucheaufnahmetruppgnss', 'general', 'spaufsucheaufnahmetruppgnss', None, None, lambda: self.validateTab('general', 0))
        self.setUpGeneralComboBox('spaufsuchenichtbegehbarursacheid', 'general', 'spaufsuchenichtbegehbarursacheid', None, None, lambda: self.generalValidation())
        self.setTreeWidget('spaufsuchenichtwaldursacheidTreeWidget', 'general', 'spaufsuchenichtwaldursacheid', None, None, lambda: self.generalValidation())
        self._validateTab('general', 0)
        
        # Coordinates
        self.setUpGeneralComboBox('spaufsucheverschobenursacheid', 'coordinates', 'spaufsucheverschobenursacheid', None, None, lambda: self.coordinatesValidation())
        self.setUpGeneralComboBox('s_perma', 'coordinates', 's_perma', None, None, lambda: self.validateTab('coordinates', 1))
        self.setUpTextField('istgeom_y', 'coordinates', 'istgeom_y', None, None, lambda: self.validateTab('coordinates', 1))
        self.setUpTextField('istgeom_x', 'coordinates', 'istgeom_x', None, None, lambda: self.validateTab('coordinates', 1))
        self.setUpTextField('istgeom_elev', 'coordinates', 'istgeom_elev', None, None, lambda: self.validateTab('coordinates', 1))
        self.setUpTextField('istgeom_sat', 'coordinates', 'istgeom_sat', None, None, lambda: self.validateTab('coordinates', 1))
        self.setUpTextField('istgeom_hdop', 'coordinates', 'istgeom_hdop', None, None, lambda: self.validateTab('coordinates', 1))
        self.setUpTextField('istgeom_vdop', 'coordinates', 'istgeom_vdop', None, None, lambda: self.validateTab('coordinates', 1))
        self._validateTab('coordinates', 1)

        # Baumplot
        self.setUpTextField('azimuttransektploteins', 'baumplot1', 'azimuttransektploteins', None, None, lambda: self.validateTab('baumplot1', 2))
        self.setUpArray('baumplot1', 'baumplot1', self.baumplotAdd, self.baumplotAddError)

        # Landmarken
        self.setUpArray('landmarken1', 'landmarken1', self.landmarken1Add, self.landmarken1AddError)

        # Baumplot
        self.setUpArray('baumplot2', 'baumplot2', self.baumplot2Add, self.baumplot2AddError)

        # Landmarken
        self.setUpArray('landmarken2', 'landmarken2', self.landmarken2Add, self.landmarken2AddError)


        #Transekt
        self.setUpGeneralComboBox('schutzmassnahmeid', 'transekt', 'schutzmassnahmeid')
        self.setUpTextField('transektstoerungursache', 'transekt', 'transektstoerungursache')

        #Transekt
        self.setUpTextField('verjuengungstransektlaenge', 'verjuengungstransekt', 'verjuengungstransektlaenge', None, None, lambda: self.validateTab('verjuengungstransekt', 7))
        self.setUpArray('verjuengungstransekt', 'verjuengungstransekten', self.verjuengungstransektAdd, self.verjuengungstransektAddError)

        # Weiserpflanzen
        self.setUpTextField('krautanteil', 'weiserpflanzen', 'krautanteil', None, None, lambda: self.validateTab('weiserpflanzen', 8))
        self.setUpObject('weiserpflanzen', 'moos')
        self.setUpObject('weiserpflanzen', 'kraut')
        self.setUpObject('weiserpflanzen', 'grass')
        self.setUpObject('weiserpflanzen', 'farne')
        self.setUpObject('weiserpflanzen', 'doldengewaechse')
        self.setUpObject('weiserpflanzen', 'beerenstraucher')
        self.setUpObject('weiserpflanzen', 'grosstraucher')

        # Transektinfo
        self.setUpCheckBox('transektfrassmaus', 'transektinfo', 'transektfrassmaus', None, None, lambda: self.validateTab('transektinfo', 9))
        self.setUpCheckBox('transektfrasshase', 'transektinfo', 'transektfrasshase', None, None, lambda: self.validateTab('transektinfo', 9))
        self.setUpCheckBox('transektfrassbieber', 'transektinfo', 'transektfrassbieber', None, None, lambda: self.validateTab('transektinfo', 9))

        # Bestandsbeschreibung
        self.setUpGeneralComboBox('bestandbetriebsartid', 'bestandsbeschreibung', 'bestandbetriebsartid', None, None, self.save_json)
        self.setUpGeneralComboBox('bestandkronenschlussgradid', 'bestandsbeschreibung', 'bestandkronenschlussgradid', None, None, self.save_json) #, None, None, lambda: self.validateTab('bestandsbeschreibung', 10)
        self.setUpGeneralComboBox('bestandschutzmassnahmenid', 'bestandsbeschreibung', 'bestandschutzmassnahmenid', None, None, self.save_json)
        self.setUpGeneralComboBox('bestandnschichtigid', 'bestandsbeschreibung', 'bestandnschichtigid', None, None, lambda: self.validate_best_besch())
        
        #try:
        #    self.bestandnschichtigid.currentIndexChanged.disconnect()
        #except:
        #    pass

        #self.bestandnschichtigid.currentIndexChanged.connect(self.validation_t_bestockung)
        self.validation_t_bestockung()

        self.setUpGeneralComboBox('bestandbiotopid', 'bestandsbeschreibung', 'bestandbiotopid')

        self.setUpTextField('bestandbedeckungsgradunterstand', 'bestandsbeschreibung', 'bestandbedeckungsgradunterstand')
        self.setUpTextField('bestandbedeckungsgradgraeser', 'bestandsbeschreibung', 'bestandbedeckungsgradgraeser')
        self.setUpTextField('bestandheterogenitaetsgradid', 'bestandsbeschreibung', 'bestandheterogenitaetsgradid')

        # Bestockung
        self.setUpArray('t_bestockung', 't_bestockung', self.t_bestockungAdd, self.t_bestockungAddError, lambda: self.validation_t_bestockung())

        # Bodenvegetation
        self.setUpArray('t_bodenvegetation', 't_bodenvegetation', self.t_bodenvegetationAdd, self.t_bodenvegetationAddError)


        # Störung
        self.setUpCheckBox('thinning', 'stoerung', 'thinning', None, None, self.save_json)
        self.setUpCheckBox('sanitaryStrokes', 'stoerung', 'sanitaryStrokes', None, None, self.save_json)
        self.setUpCheckBox('wildfire', 'stoerung', 'wildfire', None, None, self.save_json)
        self.setUpCheckBox('storm', 'stoerung', 'storm', None, None, self.save_json)
        self.setUpCheckBox('soilCultivation', 'stoerung', 'soilCultivation', None, None)
        self.setUpTextField('note', 'stoerung', 'note', None, None)


        self.validateAll()
        # next time update values only
        self.isSetup = True

    def validate_best_besch(self):
        self.validateTab('bestandsbeschreibung', 10)
        self.validation_t_bestockung()

    def coordinatesValidation(self):
        """Validate the coordinates tab."""

        #if self.json['coordinates']['spaufsucheverschobenursacheid'] != None:
        #    for i in range(2, 13):
        #        if self.vwmTabs.isTabEnabled(i):
        #            self.vwmTabs.setTabEnabled(i, False)
        #else:
        for i in range(2, 13):
            self.vwmTabs.setTabEnabled(i, True)
        
        self.validateTab('coordinates', 1)

    def generalValidation(self):
        """Validate the general tab."""

        if self.json['general']['spaufsuchenichtbegehbarursacheid'] != 1 or self.json['general']['spaufsuchenichtwaldursacheid'] != 0:
            for i in range(1, 13):
                if self.vwmTabs.isTabEnabled(i):
                    self.vwmTabs.setTabEnabled(i, False)
        else:
            self.vwmTabs.setTabEnabled(1, True)
            self.coordinatesValidation()

        
        self.validateTab('general', 0)

    def validateTab(self, parentName, tab):
        
        self._validateTab(parentName, tab)
        return
        if self.validationTimer != None:

            self.validationTimer.cancel()
            self.validationTimer = None
        self.validationTimer = threading.Timer(0.5, lambda: self._validateTab(parentName, tab))
        self.validationTimer.start()

    def _validateTab(self, parentName, tab):
        
        
        tabErrors = self._validate(self.schema['properties'][parentName], self.json[parentName])
        
        if len(tabErrors) > 0:
            self.vwmTabs.setTabIcon(tab, QtGui.QIcon(':icons/red_rect.png'))
        else:
            self.vwmTabs.setTabIcon(tab, QtGui.QIcon())

        self.validationTimer = None

        #self.validate.emit(self.json)

        self.validateAll()

    # UTILS
    def _validate(self, schema, value):
        """Validate the json."""

        v = Draft7Validator(schema)

        return sorted(v.iter_errors(value), key=lambda e: e.path)
    
    def getDefault(self, schema):
        """Set the default value."""

        if "default" in schema:
            return schema['default']
        elif "enum" in schema:
            return schema["enum"][0]
        elif schema['type'] == "boolean":
            return False
        elif schema['type'] == "string":
            return None
        elif schema['type'] == "number":
            return None
        
        return None
    
    def shouldBeNumeric(self, schema):
        """Check if the value should be numeric."""
        return (type(schema['type']) == str and (schema['type'] == "number" or schema['type'] == "integer") or (hasattr(schema['type'], "__len__") and ("integer" in schema['type'] or "number" in schema['type'])))
    def shouldBeNumber(self, schema):
        """Check if the value should be a number."""
        return (type(schema['type']) == str and (schema['type'] == "number") or (hasattr(schema['type'], "__len__") and ("number" in schema['type'])))
    def shouldBeInteger(self, schema):
        """Check if the value should be an integer."""
        return (type(schema['type']) == str and (schema['type'] == "integer") or (hasattr(schema['type'], "__len__") and ("integer" in schema['type'])))
    def isfloat(self, num):
        """Check if the value is a float."""
        try:
            float(num)
            return True
        except ValueError:
            return False
    
    # SET UP

    # Object
    def setUpObject(self, parentName, childName):
        """Set up an object."""

        schema = self.schema['properties'][parentName]['properties'][childName]

        if childName not in self.json[parentName]:
            self.json[parentName][childName] = self.getDefault(schema)

        
        if hasattr(self, childName + 'Error'):
            getattr(self, childName + 'Error').hide()

        def onUpdate():
            percentTotal = 0
            for child in self.json[parentName][childName]:
                childPercent = self.json[parentName][childName][child]
                if isinstance(childPercent, int):
                    percentTotal += childPercent

            if hasattr(self, childName + 'Error'):
                if percentTotal > 100:
                    getattr(self, childName + 'Error').show()
                    getattr(self, childName + 'Error').setText('Die Summe der Prozentwerte darf nicht größer als 100 sein.')
                    #self.krautError.show()
                else:
                    getattr(self, childName + 'Error').hide()
                    getattr(self, childName + 'Error').setText('')
                    #self.krautError.hide()

            self.save_json()
        
        if self.json[parentName][childName] == None:
            self.json[parentName][childName] = {}

        for child in schema['properties']:

            #self.json[parentName][childName][child] = 0
            
            self.setUpTextField(
                child,
                parentName,
                child,
                self.json[parentName][childName],
                schema['properties'][child],
                onUpdate
            )
            
        onUpdate()

    # ARRAYS
    def setUpArrayBestockung(self, parentName, childName):
        """Set up an array."""

        # on activate Tab
        self.validation_t_bestockung()

        schema = self.schema['properties'][parentName]['properties'][childName]

        objectValues = {}

        def update_json():
            """Add Obj to json."""
            self.json[parentName][childName].append(objectValues.copy())
            refresh_fields()

            self.validation_t_bestockung()

        def refresh_fields():
            self.setUpGeneralComboBox('schicht_id', 't_bestockung', 'schicht_id', objectValues, schema['items']['properties']['schicht_id'])
            self.setUpGeneralComboBox('icode_ba', 't_bestockung', 'icode_ba', objectValues, schema['items']['properties']['icode_ba'])
            self.setUpGeneralComboBox('nas_id', 't_bestockung', 'nas_id', objectValues, schema['items']['properties']['nas_id'])
            self.setUpGeneralComboBox('entsart_id', 't_bestockung', 'entsart_id', objectValues, schema['items']['properties']['entsart_id'])
            self.setUpGeneralComboBox('vert_id', 't_bestockung', 'vert_id', objectValues, schema['items']['properties']['vert_id'])
            self.setUpTextField('ba_anteil', 't_bestockung', 'ba_anteil', objectValues, schema['items']['properties']['ba_anteil'])

        try:
            self.addBestockungBtn.clicked.disconnect()
        except:
            pass
        
        self.addBestockungBtn.clicked.connect(update_json)
        refresh_fields()

    def refresh_baumplot(self, parentName, objectValues, schema, validateArray):
        """Refresh the baumplot."""

        self.setUpGeneralComboBox(
            parentName+'_icode_ba',
            parentName,
            'icode_ba',
            objectValues,
            schema['items']['properties']['icode_ba'])
        self.setUpTextField(
            parentName+'_azimut',
            parentName,
            'azimut',
            objectValues,
            schema['items']['properties']['azimut'], validateArray)
        self.setUpTextField(
            parentName+'_distanz',
            parentName,
            'distanz',
            objectValues,
            schema['items']['properties']['distanz'], validateArray)
        self.setUpTextField(
            parentName+'_bhd',
            parentName,
            'bhd',
            objectValues,
            schema['items']['properties']['bhd'], validateArray)
        self.setUpTextField(
            parentName+'_messhoehebhd',
            parentName,
            'messhoehebhd',
            objectValues,
            schema['items']['properties']['messhoehebhd'], validateArray)
        self.setUpCheckBox(
            parentName+'_schaele',
            parentName,
            'schaele',
            objectValues,
            schema['items']['properties']['schaele'])
        self.setUpCheckBox(
            parentName+'_fege',
            parentName,
            'fege',
            objectValues,
            schema['items']['properties']['fege'])
    
    def refresh_landmarken(self, parentName, objectValues, schema, validateArray):
        """Refresh the landmarken."""
        self.setUpTextField(
            parentName+'_landmarken',
            parentName,
            'landmarken',
            objectValues,
            schema['items']['properties']['landmarken'], validateArray)
        
        self.setUpTextField(
            parentName+'_azimut',
            parentName,
            'azimut',
            objectValues,
            schema['items']['properties']['azimut'], validateArray)
        
        self.setUpTextField(
            parentName+'_distanz',
            parentName,
            'distanz',
            objectValues,
            schema['items']['properties']['distanz'], validateArray)
    
    def refresh_t_bodenvegetation(self, parentName, objectValues, schema, validateArray):
        """Refresh the t_bodenvegetation."""
        self.setUpGeneralComboBox(
            parentName+'_bodenveggr',
            parentName,
            'bodenveggr',
            objectValues,
            schema['items']['properties']['bodenveggr'], validateArray)
        self.setUpGeneralComboBox(
            parentName+'_verteilung',
            parentName,
            'verteilung',
            objectValues,
            schema['items']['properties']['verteilung'], validateArray)
        self.setUpTextField(
            parentName+'_anteil',
            parentName,
            'anteil',
            objectValues,
            schema['items']['properties']['anteil'], validateArray)
        
    def refresh_verjuengungstransekt(self, parentName, objectValues, schema, validateArray):
        self.setUpGeneralComboBox(
            parentName+'_ba_icode',
            parentName,
            'ba_icode',
            objectValues,
            schema['items']['properties']['ba_icode'],
            validateArray
        )
        self.setUpGeneralComboBox(
            parentName+'_height',
            parentName,
            'height',
            objectValues,
            schema['items']['properties']['height'],
            validateArray
        )
        self.setUpTextField(
            parentName+'_verjuengungstransektbhd',
            parentName,
            'verjuengungstransektbhd',
            objectValues,
            schema['items']['properties']['verjuengungstransektbhd'],
            validateArray
        )
        self.setUpGeneralComboBox(
            parentName+'_verjuengungstransektschutzmassnahmen',
            parentName,
            'verjuengungstransektschutzmassnahmen',
            objectValues,
            schema['items']['properties']['verjuengungstransektschutzmassnahmen'],
            validateArray
        )

        self.setUpCheckBox(
            parentName+'_verjuengungstransekttriebverlustdurchinsektenfrass',
            parentName,
            'verjuengungstransekttriebverlustdurchinsektenfrass',
            objectValues,
            schema['items']['properties']['verjuengungstransekttriebverlustdurchinsektenfrass']
        )
        self.setUpCheckBox(
            parentName+'_verjuengungstransekttriebverlustdurchschalenwildverbiss',
            parentName,
            'verjuengungstransekttriebverlustdurchschalenwildverbiss',
            objectValues,
            schema['items']['properties']['verjuengungstransekttriebverlustdurchschalenwildverbiss']
        )
        self.setUpCheckBox(
            parentName+'_verjuengungstransekttriebverlustdurchfrost',
            parentName,
            'verjuengungstransekttriebverlustdurchfrost',
            objectValues,
            schema['items']['properties']['verjuengungstransekttriebverlustdurchfrost']
        )
        self.setUpCheckBox(
            parentName+'_verjuengungstransekttriebverlustdurchtrockenheit',
            parentName,
            'verjuengungstransekttriebverlustdurchtrockenheit',
            objectValues,
            schema['items']['properties']['verjuengungstransekttriebverlustdurchtrockenheit']
        )
        self.setUpCheckBox(
            parentName+'_verjuengungstransekttriebverlustdurchfege',
            parentName,
            'verjuengungstransekttriebverlustdurchfege',
            objectValues,
            schema['items']['properties']['verjuengungstransekttriebverlustdurchfege']
        )
    def refresh_t_bestockung(self, parentName, objectValues, schema, validateArray):
        self.setUpGeneralComboBox(parentName+'_schicht_id', 't_bestockung', 'schicht_id', objectValues, schema['items']['properties']['schicht_id'], validateArray)
        self.setUpGeneralComboBox(parentName+'_icode_ba', 't_bestockung', 'icode_ba', objectValues, schema['items']['properties']['icode_ba'], validateArray)
        self.setUpGeneralComboBox(parentName+'_nas_id', 't_bestockung', 'nas_id', objectValues, schema['items']['properties']['nas_id'], validateArray)
        self.setUpGeneralComboBox(parentName+'_entsart_id', 't_bestockung', 'entsart_id', objectValues, schema['items']['properties']['entsart_id'], validateArray)
        self.setUpGeneralComboBox(parentName+'_vert_id', 't_bestockung', 'vert_id', objectValues, schema['items']['properties']['vert_id'], validateArray)
        self.setUpTextField(parentName+'_ba_anteil', 't_bestockung', 'ba_anteil', objectValues, schema['items']['properties']['ba_anteil'], validateArray)


    def setUpArray(self, parentName, childName, addElementBtn, addElementError, onUpdate=None):
        """Set up an array."""

        addElementError.hide()
        
        schema = self.schema['properties'][parentName]['properties'][childName]
        objectValues = {}

        def reset_error():
            addElementError.setText('')
            addElementError.hide()

        def update_json():

            arrayElements = self.json[parentName][childName]
            foundSame = False

            if 'azimut' in objectValues and 'distanz' in objectValues:
                for element in arrayElements:
                    if objectValues['distanz'] == element['distanz'] and objectValues['azimut'] == element['azimut']:
                        foundSame = True
                        break
            
            if foundSame == False:
                self.json[parentName][childName].append(objectValues.copy())
                addElementError.hide()
                objectValues.clear()
                refresh_fields()

                self.fillTable(parentName, childName, schema)

                if hasattr(self, parentName+'_collapsable'):
                    getattr(self, parentName+'_collapsable').setCollapsed(True)
            
                if onUpdate is not None:
                    onUpdate()
            else:
                addElementError.setText('Ein Eintrag mit gleichen Werten (Azimut und Distanz) existiert bereits.')
                addElementError.show()
                QTimer.singleShot(3000, reset_error)
                pass

        
        def validateArray():
            errors = self._validate(schema['items'], objectValues)     
            
            if len(errors) > 0:
                addElementBtn.setEnabled(False)
            else:
                addElementBtn.setEnabled(True)
            
            if 'verjuengungstransektbhd' in objectValues:
                if objectValues['height'] == 6 and objectValues['verjuengungstransektbhd'] == None:
                    addElementError.setText('BHD muss angegeben werden, wenn eine Höhe größer 2 Meter gewählt ist.')
                    addElementError.show()
                else:
                    addElementError.hide()

            self.save_json()

        def refresh_fields():
            if parentName == 'baumplot1' or parentName == 'baumplot2':
                self.refresh_baumplot(parentName, objectValues, schema, validateArray)
            elif parentName == 'landmarken1' or parentName == 'landmarken2':
                self.refresh_landmarken(parentName, objectValues, schema, validateArray)
            elif parentName == 't_bodenvegetation':
                self.refresh_t_bodenvegetation(parentName, objectValues, schema, validateArray)
            elif parentName == 'verjuengungstransekt':
                self.refresh_verjuengungstransekt(parentName, objectValues, schema, validateArray)
            elif parentName == 't_bestockung':
                self.refresh_t_bestockung(parentName, objectValues, schema, validateArray)
        
        
        refresh_fields()
        self.fillTable(parentName, childName, schema)

        if self.isSetup == True:
            
            return
        
        try:
            addElementBtn.clicked.disconnect(update_json)
        except:
            pass

        addElementBtn.clicked.connect(update_json)
        

    # COMBOBOX
    def setUpCheckBox(self, objectName, parentName, childName, objectValues = None, schema = None, onUpdate = None):
        """Set up a combo box."""

        if schema is None: # if root schema
            schema = self.schema['properties'][parentName]['properties'][childName]

        if hasattr(self, objectName):
            element = getattr(self, objectName)
        else:
            QgsMessageLog.logMessage("Element " + childName + " not found in " + parentName, 'FIM')
            return
        
        
        if objectValues is not None:
            if childName not in objectValues:
                objectValues[childName] = self.getDefault(schema)

            element.setChecked(objectValues[childName])
        else:
            if childName not in self.json[parentName]:
                self.json[parentName][childName] = self.getDefault(schema)

            element.setChecked(self.json[parentName][childName])

        if self.isSetup == True:
            return

        element.setText(schema['title'])

        if hasattr(self, objectName + 'Description'):
            if 'description' in schema:
                getattr(self, objectName + 'Description').setText(schema['description'])
            else:
                getattr(self, objectName + 'Description').setText('')

        def update_json(state):
            if objectValues is not None:
                objectValues[childName] = state == 2
            else:
                self.json[parentName][childName] = state == 2

            if onUpdate is not None:
                onUpdate()

        try:
            element.stateChanged.disconnect()
        except:
            pass

        element.stateChanged.connect(update_json)

    def setUpGeneralComboBox(self, objectName, parentName, childName, objectValues = None, schema = None, onUpdate = None):
        """Set up a combo box."""

        if hasattr(self, objectName):
            element = getattr(self, objectName)
        else:
            QgsMessageLog.logMessage("Element " + childName + " not found in " + parentName, 'FIM')
            return

        if schema is None: # if root schema
            schema = self.schema['properties'][parentName]['properties'][childName]

        
        def refresh_field():

            if objectValues is not None:
                if childName not in objectValues or objectValues[childName] is None:
                    objectValues[childName] = self.getDefault(schema)
                
                index = schema['enum'].index(objectValues[childName])
                element.setCurrentIndex(index)
            else:
                if childName not in self.json[parentName] or self.json[parentName][childName] is None:
                    self.json[parentName][childName] = self.getDefault(schema)
                
                index = schema['enum'].index(self.json[parentName][childName])
                element.setCurrentIndex(index)

            return index
        
        

        if self.isSetup == True:
            index = refresh_field()
            return

        if hasattr(self, objectName + 'Label'):
            getattr(self, objectName + 'Label').setText(schema['title'])

        element.addItems(schema['enumLabels'])
        
        def validate():
            errors = self._validate(schema, schema['enum'][element.currentIndex()])

            if len(errors) > 0:
                if hasattr(self, objectName + 'Error'):
                    getattr(self, objectName + 'Error').setText(str(errors[0].message))
                element.setStyleSheet("QComboBox {\n border: 2px solid red;}")
            else:
                if hasattr(self, objectName + 'Error'):
                    getattr(self, objectName + 'Error').setText('')
                element.setStyleSheet("QComboBox {\n border: 2px solid green;}")

        def update_json(index):
            value = schema['enum'][index]

            validate()

            if objectValues is not None:
                objectValues[childName] = value
            else:
                self.json[parentName][childName] = value

            if onUpdate is not None:
                onUpdate()

        def update_value_by_chip(index):
            """Set DD value by chip."""
            update_json(index)
            refresh_field()
        
        def update_value_by_combo(indexFromCombo):
            """Set DD value by combo."""

            if 'chips' in locals():
                chips.setValue(schema['enumLabels'][indexFromCombo])

            update_json(element.currentIndex())
            refresh_field()

        try:
            element.currentIndexChanged.disconnect()
        except:
            pass

        element.currentIndexChanged.connect(update_value_by_combo)
        validate()
        
        index = refresh_field()
            

        if hasattr(self, parentName + '_' + childName + '_chips'):
            maxChipCount = 15 #schema['qtChips']
            chips = Chips(self.interface, schema, maxChipCount)
            chips.setValue(schema['enumLabels'][index])
            getattr(self, parentName + '_' + childName + '_chips').addWidget(chips)
            chips.inputChanged.connect(update_value_by_chip)

            if maxChipCount >= len(schema['enum']):
                getattr(self, objectName).hide()

        
    def setTreeWidget(self, objectName, parentName, childName, objectValues = None, schema = None, onUpdate = None):
        """Set up a combo / Tree Widget."""

        if hasattr(self, objectName):
            element = getattr(self, objectName)
        else:
            QgsMessageLog.logMessage("Element " + childName + " not found in " + parentName, 'FIM')
            return
        
        if schema is None: # if root schema
            schema = self.schema['properties'][parentName]['properties'][childName]

        if childName not in self.json[parentName] or self.json[parentName][childName] is None:
            self.json[parentName][childName] = self.getDefault(schema)


        if hasattr(self, objectName + 'Label'):
            getattr(self, objectName + 'Label').setText(schema['title'])

        def refresh_field():
            idx = schema['enum'].index(self.json[parentName][childName])
            self.spaufsuchenichtwaldursacheidText.setText(str(schema['enumLabels'][idx]))

        def update_json(item):
            value = int(item.data(0, 1))

            refresh_field()

            if objectValues is not None:
                objectValues[childName] = value
            else:
                self.json[parentName][childName] = value

            if onUpdate is not None:
                onUpdate()

        element.itemClicked.connect(update_json)
        refresh_field()

        element.clear()

        if 'description' in schema:
            element.setHeaderLabels([schema['description']])

        items = {}

        for idx, item in enumerate(schema['enum']):
            if item is None or item < 100 :
                items[str(item)] = {
                    'name': schema['enumLabels'][idx],
                    'children': {}
                }

        for idx, item in enumerate(schema['enum']):
            if item is not None and item > 100 :
                if item < 10000:
                    index = int(str(item)[0])
                else:
                    index = int(str(item)[0] + str(item)[1])

                if str(index) in items :
                    items[str(index)]['children'][str(item)] = {
                        'name': schema['enumLabels'][idx],
                        'children': {}
                    }
                else:
                    items[str(item)] = {
                        'name': schema['enumLabels'][idx],
                        'children': {}
                    }

        self.setTreeItems(element, items, parentName, childName)

    def setTreeItems(self, tree, items, parentName, childName):

        for attr, item in items.items():

            child = QtWidgets.QTreeWidgetItem(tree)

            
            child.setText(0, item['name'])
            child.setData(0, 1, attr)

            child.setSelected(attr == str(self.json[parentName][childName]))

            if 'children' in item:
                self.setTreeItems(child, item['children'], parentName, childName)

    # TEXTFIELD
    def setUpTextField(self, objectName, parentName, childName, objectValues = None, schema = None, onUpdate = None):
        """Set up a text field."""

        if hasattr(self, objectName):
            element = getattr(self, objectName)
        else:
            QgsMessageLog.logMessage("Element " + childName + " not found in " + parentName, 'FIM')
            return
        
        if schema is None: # if root schema
            schema = self.schema['properties'][parentName]['properties'][childName]        
        
        if objectValues is not None:
            if childName not in objectValues or objectValues[childName] is None:
                objectValues[childName] = self.getDefault(schema)
                
            tempValue = objectValues[childName]
            if tempValue is not None:
                tempValue = str(tempValue)

            if hasattr(element, 'setText'):
                element.setText(tempValue)
            elif hasattr(element, 'setPlainText'):
                element.setPlainText(tempValue)

        else:
            if childName not in self.json[parentName] or self.json[parentName][childName] is None:
                self.json[parentName][childName] = self.getDefault(schema)

            tempValue = self.json[parentName][childName]
            if tempValue is not None:
                tempValue = str(tempValue)

            if hasattr(element, 'setText'):
                element.setText(tempValue)
            elif hasattr(element, 'setPlainText'):
                element.setPlainText(tempValue)

        if self.isSetup == True:
            return


        if hasattr(self, objectName + 'Label'):
            getattr(self, objectName + 'Label').setText(schema['title'])

        def update_json(text = None):
            if hasattr(element, 'text'):
                value = element.text()
            elif hasattr(element, 'toPlainText'):
                value = element.toPlainText()

            if self.shouldBeNumber(schema) and self.isfloat(value):
                value = float(value)
            elif self.shouldBeInteger(schema) and value.isnumeric():
                value = int(value)
            elif value == '':
                value = None

            errors = self._validate(schema, value)

            if hasattr(self, objectName + 'Error'):
                errorObject = getattr(self, objectName + 'Error')
                if len(errors) > 0:
                    if 'description' in schema and (value == '' or value is None):
                        errorObject.setStyleSheet("QLabel {\n color:black;}")
                        errorObject.setText(schema['description'])
                        #errorObject.setText(str(errors[0].message))
                    else:
                        errorObject.setStyleSheet("QLabel {\n color:red;}")
                        errorObject.setText(str(errors[0].message))

                    element.setStyleSheet("QLineEdit {\n border: 2px solid red;}")
                else:
                    errorObject.setText('')
                    element.setStyleSheet("QLineEdit {\n border: 2px solid green;}")
            

            if objectValues is not None:
                objectValues[childName] = value
            else:
                self.json[parentName][childName] = value

            if onUpdate is not None:
                onUpdate()
            else:
                self.save_json()
            
        try:
            element.textChanged.disconnect()
        except:
            pass

        element.textChanged.connect(update_json)
        element.setPlaceholderText(schema['title'])

        if self.shouldBeNumeric(schema):
            element.setAlignment(Qt.AlignRight)

        update_json()
            
    def setTableHeaders(self, element, data, schema):

        headers = []

        for attr, value in schema['items']['properties'].items():
            headers.append(value['title'])

        headers.append('')
        headers.append('')
        headers.append('')

        element.setColumnCount(len(headers))
        element.setRowCount(len(data))

        element.setHorizontalHeaderLabels(headers)
        #element.horizontalHeader().setStretchLastSection(True)
        #element.horizontalHeader().setStretchFirstSection(True)
        for i in range(0, len(headers)):
            element.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        

        element.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        #element.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

    def fillTable(self, parentName, childName, schema):
        """Fill a table."""

        table = getattr(self, childName + 'Table')

        self.setTableHeaders(table, self.json[parentName][childName], schema)

        
        table.setRowCount(0)

        for element in self.json[parentName][childName]:
            rowPosition = table.rowCount()
            table.insertRow(rowPosition)

            for i, child in enumerate(schema['items']['properties']):
                value = ''

                if schema['items']['properties'][child]['type'] == 'boolean':
                    value = 'Ja' if element[child] else 'Nein'
                elif 'enumLabels' in schema['items']['properties'][child]:
                    index = schema['items']['properties'][child]['enum'].index(element[child])
                    value = str(schema['items']['properties'][child]['enumLabels'][index])
                else:
                    value = str(element[child])
                
                if 'unitShort' in schema['items']['properties'][child]:
                    value = value + ' ' + schema['items']['properties'][child]['unitShort']

                table.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(value))

            deleteBtn = QtWidgets.QPushButton('Löschen')
            deleteBtn.clicked.connect(self.deleteTableRow(parentName, childName, schema, element))
            table.setCellWidget(rowPosition, len(schema['items']['properties']), deleteBtn)

            editBtn = QtWidgets.QPushButton('Bearbeiten')
            editBtn.clicked.connect(self.editTableRow(parentName, childName, schema, element))
            table.setCellWidget(rowPosition, len(schema['items']['properties']) +1, editBtn)

            copyBtn = QtWidgets.QPushButton('Duplizieren')
            copyBtn.clicked.connect(self.copyTableRow(parentName, childName, schema, element))
            table.setCellWidget(rowPosition, len(schema['items']['properties']) +2, copyBtn)
    
    def copyTableRow(self, parentName, childName, schema, element):
        def copyRow():
            self.copyRow(parentName, childName, schema, element)
        return copyRow
    
    def editTableRow(self, parentName, childName, schema, element):
        def editRow():
            self.editRow(parentName, childName, schema, element)
        return editRow
    
    def copyRow(self, parentName, childName, schema, element):
            
        self.defaultValue = copy.deepcopy(element)

        if hasattr(self, parentName+'_collapsable'):
            getattr(self, parentName+'_collapsable').setCollapsed(False)

        for child in schema['items']['properties']:

            if child == 'azimut' or child == 'distanz':
                continue

            if child in element and element[child] is not None:

                if 'enumLabels' in schema['items']['properties'][child]:
                    index = schema['items']['properties'][child]['enum'].index(element[child])
                    getattr(self, parentName+'_'+child).setCurrentIndex(index)
                elif schema['items']['properties'][child]['type'] == 'boolean':
                    getattr(self, parentName+'_'+child).setChecked(element[child])
                elif self.shouldBeNumeric(schema['items']['properties'][child]):
                    getattr(self, parentName+'_'+child).setText(str(element[child]))
                elif self.shouldBeInteger(schema['items']['properties'][child]):
                    getattr(self, parentName+'_'+child).setText(str(element[child]))
                else:
                    getattr(self, parentName+'_'+child).setText(element[child])
        
        self.fillTable(parentName, childName, schema)
        self.validation_t_bestockung()

    def editRow(self, parentName, childName, schema, element):
        
        self.defaultValue = copy.deepcopy(element)

        if hasattr(self, parentName+'_collapsable'):
            getattr(self, parentName+'_collapsable').setCollapsed(False)

        for child in schema['items']['properties']:
            if child in element and element[child] is not None:

                if 'enumLabels' in schema['items']['properties'][child]:
                    index = schema['items']['properties'][child]['enum'].index(element[child])
                    getattr(self, parentName+'_'+child).setCurrentIndex(index)
                elif schema['items']['properties'][child]['type'] == 'boolean':
                    getattr(self, parentName+'_'+child).setChecked(element[child])
                elif self.shouldBeNumeric(schema['items']['properties'][child]):
                    getattr(self, parentName+'_'+child).setText(str(element[child]))
                elif self.shouldBeInteger(schema['items']['properties'][child]):
                    getattr(self, parentName+'_'+child).setText(str(element[child]))
                else:
                    getattr(self, parentName+'_'+child).setText(element[child])
        
        self.json[parentName][childName].remove(element)
        self.fillTable(parentName, childName, schema)
        self.validation_t_bestockung()
    
    def deleteTableRow(self, parentName, childName, schema, element):
        def removeRow():
            self.removeRow(parentName, childName, schema, element)
        return removeRow
    
    def removeRow(self, parentName, childName, schema, element):

        res = Utils.confirmDialog(self, 'Zeile löschen', 'Möchtest du die Zeile wirklich löschen?')
        if res == QtWidgets.QMessageBox.Yes:

            self.json[parentName][childName].remove(element)

            self.fillTable(parentName, childName, schema)
            self.validation_t_bestockung()

        
    def validation_t_bestockung(self):
        """Show an error if the bestockung is not valid."""

        label_errors = self.lfbLayers()

        if len(label_errors) > 0:
            self.t_bestockungError.show()
            self.t_bestockungError.setText(str(label_errors[0].message))
            self.vwmTabs.setTabIcon(11, QtGui.QIcon(':icons/red_rect.png'))
        else:
            self.t_bestockungError.hide()
            self.vwmTabs.setTabIcon(11, QtGui.QIcon())

        self.validateAll()
    
    def lfbLayers(self):

        # https://github.com/b-lack/qgis-fim-plugin/issues/25

        # 0 = Plenter
        # 1 = Hauptbestand
        # 2 = Unterstand
        # 3 = Oberstand

        json = self.json

        label_errors = []

        rules_type = {
            1: [ # es
                [3, 1, 36, 9],
                [31, 36, 9]
            ],
            2: [ # zs
                [3, 1, 2, 4, 36, 9],
                [2, 4, 31, 36, 9]
            ],
            3: [ # ms
                [3, 1, 25, 2, 4, 31, 36, 9]
            ],
            4: [ # zsv
                [3, 1, 2, 4, 36, 9]
            ],
            5: [ # zsu
                [3, 1, 2, 4, 36, 9]
            ],
            6: [ # pl
                [0]
            ],
            7: [ # 3
                [3, 1, 25, 2, 4, 36, 9],
                [3, 2, 4, 31, 36, 9]
            ]
        }
        rules_length = {
            1: {
                "min": 1,
                "max": 1
            },
            2: {
                "min": 2,
                "max": 2
            },
            3: {
                "min": 3,
                "max": 10
            },
            4: {
                "min": 2,
                "max": 2
            },
            5: {
                "min": 2,
                "max": 2
            },
            6: {
                "min": 1,
                "max": 10
            },
            7: {
                "min": 1,
                "max": 10
            }
        }


        elements = [d['schicht_id'] for d in json['t_bestockung']['t_bestockung']]
        elements_unique = list(set(elements))
        #elements_unique.sort()

        if 'bestandnschichtigid' not in json['bestandsbeschreibung']:
            return []
        
        schicht_id = json['bestandsbeschreibung']['bestandnschichtigid']

        if rules_length.get(schicht_id) != None:

            

            if (len(elements_unique) < rules_length[schicht_id]['min'] or len(elements_unique) > rules_length[schicht_id]['max']):
                label_errors.append(exceptions.ValidationError(
                    message='Anzahl an Bestockungsschichten entspricht nicht der n-Schichtigkeit der Bestandesbeschreibung.',
                    validator='minItems',
                    validator_value=rules_length[schicht_id]['min'],
                    instance=elements_unique,
                    schema_path=['allOf', 3, 'then', 'properties', 't_bestockung', 'properties', 't_bestockung', 'minItems']
                ))
        
        if rules_type.get(schicht_id) != None:
            for i in rules_type[schicht_id]:
                
                if(all(x in i for x in elements)):
                    break
                else:
                    label_errors.append(exceptions.ValidationError(
                        message='Falsche Schichtenkombination',
                        validator='minItems',
                        validator_value=rules_length[schicht_id]['min'],
                        instance=elements_unique,
                        schema_path=['allOf', 3, 'then', 'properties', 't_bestockung', 'properties', 't_bestockung', 'minItems']
                    ))
        
        return label_errors