import os
import copy
import json
from PyQt5.QtCore import QTimer

from qgis.core import QgsMessageLog, QgsPointXY, QgsPoint
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog, QScroller, QWidget, QFormLayout, QVBoxLayout, QGroupBox
from PyQt5.QtCore import Qt, pyqtSignal

from jsonschema import Draft7Validator, exceptions

from PyQt5 import QtGui

from ...utils.helper import Utils


UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'vwm.ui'))


class VWM(QtWidgets.QWidget, UI_CLASS):

    save = pyqtSignal(object)

    def __init__(self, interface, schema):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.interface = interface
        self.schema = schema

        self.isSetup = False

        self.validationTimer = None

        #self.setUp()
        #QScroller.grabGesture(self.scrollArea_4, QScroller.LeftMouseButtonGesture)
        
        self.show()

    def updateJson(self, json):
        """Update the json."""

        self.json = json
        self.setUp()

    def gnavs_default_settings(self):
        return {
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
    def aggregatedValuesChanged(self, gpsInfos):
        """Update the aggregated values"""

        from gnavs.gui.measurement.aggregation import Aggregation

        from gnavs.utils.utils import Utils as ganvs_utils

        aggregation = Aggregation(self.interface, self.gnavs_default_settings())
        aggregated = aggregation.aggregate(gpsInfos)

        #self.precisionNote.updateIndicator(gpsInfos)
        self.precisionNote.update(aggregated)

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

        QgsMessageLog.logMessage("--------------setUp new------------", 'FIM')

        from gnavs.gui.recording.recording import Recording
        from gnavs.gui.measurement.precision import PrecisionNote

        # General

        nav = Recording(self.interface)
        nav.toggleButtonsChanged('navigation')
        nav.toggleFocus(True)
        self.gnavs_navigation.addWidget(nav)

        self.setUpTextField('spaufsucheaufnahmetruppkuerzel', 'general', 'spaufsucheaufnahmetruppkuerzel', None, None, lambda: self.validateTab('general', 0))
        self.setUpTextField('spaufsucheaufnahmetruppgnss', 'general', 'spaufsucheaufnahmetruppgnss', None, None, lambda: self.validateTab('general', 0))
        self.setUpGeneralComboBox('spaufsuchenichtbegehbarursacheid', 'general', 'spaufsuchenichtbegehbarursacheid', None, None, lambda: self.generalValidation())
        self.setTreeWidget('spaufsuchenichtwaldursacheidTreeWidget', 'general', 'spaufsuchenichtwaldursacheid', None, None, lambda: self.generalValidation())
        self._validateTab('general', 0)
        
        # Coordinates
        rec = Recording(self.interface, True, self.gnavs_default_settings())
        rec.aggregatedValuesChanged.connect(self.aggregatedValuesChanged)
        self.gnavs_recording.addWidget(rec)
        self.precisionNote = PrecisionNote(self.interface)
        self.gnavs_recording.addWidget(self.precisionNote)

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


        # Weiserpflanzen
        self.setUpTextField('krautanteil', 'weiserpflanzen', 'krautanteil')
        self.setUpObject('weiserpflanzen', 'moos')
        self.setUpObject('weiserpflanzen', 'kraut')
        self.setUpObject('weiserpflanzen', 'grass')
        self.setUpObject('weiserpflanzen', 'farne')
        self.setUpObject('weiserpflanzen', 'doldengewaechse')
        self.setUpObject('weiserpflanzen', 'beerenstraucher')
        self.setUpObject('weiserpflanzen', 'grosstraucher')

        # Transektinfo
        self.setUpCheckBox('transektfrassmaus', 'transektinfo', 'transektfrassmaus')
        self.setUpCheckBox('transektfrasshase', 'transektinfo', 'transektfrasshase')
        self.setUpCheckBox('transektfrassbieber', 'transektinfo', 'transektfrassbieber')

        # Bestandsbeschreibung
        self.setUpGeneralComboBox('bestandbetriebsartid', 'bestandsbeschreibung', 'bestandbetriebsartid')
        self.setUpGeneralComboBox('bestandkronenschlussgradid', 'bestandsbeschreibung', 'bestandkronenschlussgradid', None, None, lambda: self.validateTab('bestandsbeschreibung', 10))
        self.setUpGeneralComboBox('bestandschutzmassnahmenid', 'bestandsbeschreibung', 'bestandschutzmassnahmenid')
        self.setUpGeneralComboBox('bestandnschichtigid', 'bestandsbeschreibung', 'bestandnschichtigid')
        
        try:
            self.bestandnschichtigid.currentIndexChanged.disconnect()
        except:
            pass

        self.bestandnschichtigid.currentIndexChanged.connect(self.validation_t_bestockung)
        self.setUpGeneralComboBox('bestandbiotopid', 'bestandsbeschreibung', 'bestandbiotopid')

        self.setUpTextField('bestandbedeckungsgradunterstand', 'bestandsbeschreibung', 'bestandbedeckungsgradunterstand')
        self.setUpTextField('bestandbedeckungsgradgraeser', 'bestandsbeschreibung', 'bestandbedeckungsgradgraeser')
        self.setUpTextField('bestandheterogenitaetsgradid', 'bestandsbeschreibung', 'bestandheterogenitaetsgradid')

        # Bestockung
        self.setUpArrayBestockung('t_bestockung', 't_bestockung')

        # Bodenvegetation
        self.setUpArray('t_bodenvegetation', 't_bodenvegetation', self.t_bodenvegetationAdd, self.t_bodenvegetationAddError)


        # Störung
        self.setUpCheckBox('thinning', 'stoerung', 'thinning')
        self.setUpCheckBox('sanitaryStrokes', 'stoerung', 'sanitaryStrokes')
        self.setUpCheckBox('wildfire', 'stoerung', 'wildfire')
        self.setUpCheckBox('storm', 'stoerung', 'storm')
        self.setUpCheckBox('soilCultivation', 'stoerung', 'soilCultivation')
        self.setUpTextField('note', 'stoerung', 'note')

        # next time update values only
        self.isSetup = True

    def coordinatesValidation(self):
        """Validate the coordinates tab."""

        if self.json['coordinates']['spaufsucheverschobenursacheid'] != None:
            for i in range(2, 13):
                if self.vwmTabs.isTabEnabled(i):
                    self.vwmTabs.setTabEnabled(i, False)
        else:
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
            return ''
        elif schema['type'] == "number":
            return ''
        
        return ''
    
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

        def onUpdate():
            percentTotal = 0
            for child in self.json[parentName][childName]:
                childPercent = self.json[parentName][childName][child]
                if isinstance(childPercent, int):
                    percentTotal += childPercent

            if hasattr(self, childName + 'Error'):
                if percentTotal > 100:
                    getattr(self, childName + 'Error').show()
                    #self.krautError.show()
                else:
                    getattr(self, childName + 'Error').hide()
                    #self.krautError.hide()
        
        self.json[parentName][childName] = {}
        for child in schema['properties']:

            self.json[parentName][childName][child] = 0
            
            self.setUpTextField(
                child,
                parentName,
                child,
                self.json[parentName][childName],
                schema['properties'][child], onUpdate)

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

    def setUpArray(self, parentName, childName, addElementBtn, addElementError):
        """Set up an array."""

        addElementError.hide()
        
        schema = self.schema['properties'][parentName]['properties'][childName]
        objectValues = {}

        def reset_error():
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
            else:
                addElementError.show()
                QTimer.singleShot(3000, reset_error)

        
        def validateArray():
            errors = self._validate(schema['items'], objectValues)

            if len(errors) > 0:
                addElementBtn.setEnabled(False)
            else:
                addElementBtn.setEnabled(True)

        def refresh_fields():
            if parentName == 'baumplot1' or parentName == 'baumplot2':
                self.refresh_baumplot(parentName, objectValues, schema, validateArray)
            elif parentName == 'landmarken1' or parentName == 'landmarken2':
                self.refresh_landmarken(parentName, objectValues, schema, validateArray)
            elif parentName == 't_bodenvegetation':
                self.refresh_t_bodenvegetation(parentName, objectValues, schema, validateArray)
        
        try:
            addElementBtn.clicked.disconnect()
        except:
            pass

        addElementBtn.clicked.connect(update_json)
        refresh_fields()

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

        if hasattr(self, objectName + 'Description') and 'description' in schema:
            getattr(self, objectName + 'Description').setText(schema['description'])
        

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

        

        if self.isSetup == True:
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

        try:
            element.currentIndexChanged.disconnect()
        except:
            pass

        element.currentIndexChanged.connect(update_json)
        validate()

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

            if hasattr(element, 'setText'):
                element.setText(str(objectValues[childName]))
            elif hasattr(element, 'setPlainText'):
                element.setPlainText(str(objectValues[childName]))

        else:
            if childName not in self.json[parentName] or self.json[parentName][childName] is None:
                self.json[parentName][childName] = self.getDefault(schema)
        
            if hasattr(element, 'setText'):
                element.setText(str(self.json[parentName][childName]))
            elif hasattr(element, 'setPlainText'):
                element.setPlainText(str(self.json[parentName][childName]))

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

            errors = self._validate(schema, value)

            if len(errors) > 0:
                if hasattr(self, objectName + 'Error'):
                    getattr(self, objectName + 'Error').setText(str(errors[0].message))
                element.setStyleSheet("QLineEdit {\n border: 2px solid red;}")
            else:
                if hasattr(self, objectName + 'Error'):
                    getattr(self, objectName + 'Error').setText('')
                element.setStyleSheet("QLineEdit {\n border: 2px solid green;}")
            
            if objectValues is not None:
                objectValues[childName] = value
            else:
                self.json[parentName][childName] = value

            if onUpdate is not None:
                onUpdate()
            
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

        #headers.append('')
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
                table.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(element[child])))

            deleteBtn = QtWidgets.QPushButton('Löschen')
            deleteBtn.clicked.connect(lambda: self.deleteTableRow(parentName, childName, schema, element))
            table.setCellWidget(rowPosition, len(schema['items']['properties']), deleteBtn)

            editBtn = QtWidgets.QPushButton('Bearbeiten')
            editBtn.clicked.connect(lambda: self.editTableRow(parentName, childName, schema, element))
            #table.setCellWidget(rowPosition, len(schema['items']['properties']) +1, editBtn)
    
    def editTableRow(self, parentName, childName, schema, element):


        #self.json[parentName][childName].remove(element)
        #self.defaultValue = copy.deepcopy(self.json[self.key][row])
        pass

    def deleteTableRow(self, parentName, childName, schema, element):

        res = Utils.confirmDialog(self, 'Zeile löschen', 'Möchtest du die Zeile wirklich löschen?')
        if res == QtWidgets.QMessageBox.Yes:
            #del self.json[self.key][row]
            #self.setTableData(self.json[self.key])
            #self.inputChanged.emit(self.json)

            self.json[parentName][childName].remove(element)
            self.fillTable(parentName, childName, schema)

        
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

    
    def lfbLayers(self):

        json = self.json

        label_errors = []

        rules_type = {
            1: [ # es
                [3, 36, 9],
                [31, 36, 9]
            ],
            2: [ # zs
                [3, 2, 4, 36, 9],
                [2, 4, 31, 36, 9]
            ],
            3: [ # ms
                [3, 25, 2, 4, 31, 36, 9]
            ],
            4: [ # zsv
                [3, 2, 4, 36, 9]
            ],
            5: [ # zsu
                [3, 2, 4, 36, 9]
            ],
            6: [ # pl
                [0]
            ],
            7: [ # 3
                [3, 25, 2, 4, 36, 9],
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
                "max": 3
            },
            4: {
                "min": 3,
                "max": 3
            },
            5: {
                "min": 3,
                "max": 3
            },
            6: {
                "min": 1,
                "max": 100
            },
            7: {
                "min": 1,
                "max": 100
            }
        }


        elements = [d['schicht_id'] for d in json['t_bestockung']['t_bestockung']]
        elements_unique = list(set(elements))
        #elements_unique.sort()
        
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
        
        isSublist = False
        if rules_type.get(schicht_id) != None:
            for i in rules_type[schicht_id]:
                if(all(x in i for x in elements)):
                    isSublist = True
                    break
                else:
                    isSublist = False
                    label_errors.append(exceptions.ValidationError(
                        message='Falsche Schichtenkombination',
                        validator='minItems',
                        validator_value=rules_length[schicht_id]['min'],
                        instance=elements_unique,
                        schema_path=['allOf', 3, 'then', 'properties', 't_bestockung', 'properties', 't_bestockung', 'minItems']
                    ))
        
        return label_errors