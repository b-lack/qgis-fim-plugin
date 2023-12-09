import os
import threading

from qgis.core import QgsMessageLog, QgsPointXY, QgsPoint
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog, QScroller, QWidget, QFormLayout, QVBoxLayout, QGroupBox
from PyQt5.QtCore import Qt

from jsonschema import Draft7Validator, exceptions


UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'vwm.ui'))


class VWM(QtWidgets.QWidget, UI_CLASS):

    def __init__(self, interface, schema):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.interface = interface
        self.schema = schema

        #self.setUp()

        self.show()

    def updateJson(self, json):
        """Update the json."""

        self.json = json
        self.setUp()


    def setUp(self):
        """Set up the form."""

        QgsMessageLog.logMessage("--------------setUp new------------", 'FIM')

        # General
        self.setUpTextField('spaufsucheaufnahmetruppkuerzel', 'general', 'spaufsucheaufnahmetruppkuerzel')
        self.setUpTextField('spaufsucheaufnahmetruppgnss', 'general', 'spaufsucheaufnahmetruppgnss')
        self.setUpGeneralComboBox('spaufsuchenichtbegehbarursacheid', 'general', 'spaufsuchenichtbegehbarursacheid')
        self.setUpGeneralComboBox('spaufsuchenichtwaldursacheid', 'general', 'spaufsuchenichtwaldursacheid')

        # Coordinates
        
        self.setUpGeneralComboBox('spaufsucheverschobenursacheid', 'coordinates', 'spaufsucheverschobenursacheid')
        self.setUpGeneralComboBox('s_perma', 'coordinates', 's_perma')
        self.setUpTextField('istgeom_y', 'coordinates', 'istgeom_y')
        self.setUpTextField('istgeom_x', 'coordinates', 'istgeom_x')
        self.setUpTextField('istgeom_elev', 'coordinates', 'istgeom_elev')
        self.setUpTextField('istgeom_sat', 'coordinates', 'istgeom_sat')
        self.setUpTextField('istgeom_hdop', 'coordinates', 'istgeom_hdop')
        self.setUpTextField('istgeom_vdop', 'coordinates', 'istgeom_vdop')

        # Baumplot
        self.setUpTextField('azimuttransektploteins', 'baumplot1', 'azimuttransektploteins')
        self.setUpArray('baumplot1', 'baumplot1')


        #Transekt
        self.setUpGeneralComboBox('schutzmassnahmeid', 'transekt', 'schutzmassnahmeid')
        self.setUpTextField('transektstoerungursache', 'transekt', 'transektstoerungursache')


        # Weiserpflanzen
        self.setUpTextField('krautanteil', 'weiserpflanzen', 'krautanteil')
        self.setUpObject('weiserpflanzen', 'kraut')

        # Bestandsbeschreibung
        self.setUpGeneralComboBox('bestandbetriebsartid', 'bestandsbeschreibung', 'bestandbetriebsartid')
        self.setUpGeneralComboBox('bestandkronenschlussgradid', 'bestandsbeschreibung', 'bestandkronenschlussgradid')
        self.setUpGeneralComboBox('bestandschutzmassnahmenid', 'bestandsbeschreibung', 'bestandschutzmassnahmenid')
        self.setUpGeneralComboBox('bestandnschichtigid', 'bestandsbeschreibung', 'bestandnschichtigid')
        self.bestandnschichtigid.currentIndexChanged.disconnect()
        self.bestandnschichtigid.currentIndexChanged.connect(self.validation_t_bestockung)
        self.setUpGeneralComboBox('bestandbiotopid', 'bestandsbeschreibung', 'bestandbiotopid')

        self.setUpTextField('bestandbedeckungsgradunterstand', 'bestandsbeschreibung', 'bestandbedeckungsgradunterstand')
        self.setUpTextField('bestandbedeckungsgradgraeser', 'bestandsbeschreibung', 'bestandbedeckungsgradgraeser')
        self.setUpTextField('bestandheterogenitaetsgradid', 'bestandsbeschreibung', 'bestandheterogenitaetsgradid')

        # Bestockung
        self.setUpArrayBestockung('t_bestockung', 't_bestockung')

        # Störung
        self.setUpCheckBox('thinning', 'stoerung', 'thinning')
        self.setUpCheckBox('sanitaryStrokes', 'stoerung', 'sanitaryStrokes')
        self.setUpCheckBox('wildfire', 'stoerung', 'wildfire')
        self.setUpCheckBox('storm', 'stoerung', 'storm')
        self.setUpCheckBox('soilCultivation', 'stoerung', 'soilCultivation')
        self.setUpTextField('note', 'stoerung', 'note')


    # UTILS
    def _validate(self, schema, value):
        """Validate the json."""

        v = Draft7Validator(schema)

        return sorted(v.iter_errors(value), key=lambda e: e.path)
    
    def getDefault(self, schema):
        """Set the default value."""

        if "default" in schema:
            return schema['default']
        elif schema['type'] == "boolean":
            return False
        elif schema['type'] == "string":
            return ''
        elif schema['type'] == "number":
            return 0
        
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

            if percentTotal > 100:
                self.krautError.show()
            else:
                self.krautError.hide()
        
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

        self.addBestockungBtn.clicked.disconnect()
        self.addBestockungBtn.clicked.connect(update_json)
        refresh_fields()

    def setUpArray(self, parentName, childName):
        """Set up an array."""

        self.baumplotAddError.hide()
        
        schema = self.schema['properties'][parentName]['properties'][childName]
        objectValues = {}

        def reset_error():
            self.baumplotAddError.hide()

        def update_json():
            arrayElements = self.json[parentName][childName]
            foundSame = False
            for element in arrayElements:
                if objectValues['distanz'] == element['distanz'] and objectValues['azimut'] == element['azimut']:
                    foundSame = True
                    break
            
            if foundSame == False:
                self.json[parentName][childName].append(objectValues.copy())
                self.baumplotAddError.hide()
                refresh_fields()
            else:
                self.baumplotAddError.show()
                self.validationTimer = threading.Timer(3, reset_error)
                self.validationTimer.start()

            self.fillTable(parentName, childName, schema)
            

            #objectValues = {}
        def refresh_fields():
            self.setUpGeneralComboBox(
                'baumplot1_icode_ba',
                parentName,
                'icode_ba',
                objectValues,
                schema['items']['properties']['icode_ba'])
            self.setUpTextField(
                'baumplot1_azimut',
                parentName,
                'azimut',
                objectValues,
                schema['items']['properties']['azimut'])
            self.setUpTextField(
                'baumplot1_distanz',
                parentName,
                'distanz',
                objectValues,
                schema['items']['properties']['distanz'])
            self.setUpTextField(
                'baumplot1_bhd',
                parentName,
                'bhd',
                objectValues,
                schema['items']['properties']['bhd'])
            self.setUpTextField(
                'baumplot1_messhoehebhd',
                parentName,
                'messhoehebhd',
                objectValues,
                schema['items']['properties']['messhoehebhd'])
            self.setUpCheckBox(
                'baumplot1_schaele',
                parentName,
                'schaele',
                objectValues,
                schema['items']['properties']['schaele'])
            self.setUpCheckBox(
                'baumplot1_fege',
                parentName,
                'fege',
                objectValues,
                schema['items']['properties']['fege'])
        
        self.baumplotAdd.clicked.disconnect()
        self.baumplotAdd.clicked.connect(update_json)
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


        element.setText(schema['title'])

        

        def update_json(state):
            if objectValues is not None:
                objectValues[childName] = state == 2
            else:
                self.json[parentName][childName] = state == 2

            if onUpdate is not None:
                onUpdate()

        element.stateChanged.disconnect()
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
            if childName not in objectValues:
                objectValues[childName] = self.getDefault(schema)
        else:
            if childName not in self.json[parentName]:
                self.json[parentName][childName] = self.getDefault(schema)

        if hasattr(self, objectName + 'Label'):
            getattr(self, objectName + 'Label').setText(schema['title'])

        element.addItems(schema['enumLabels'])
        

        def update_json(index):
            value = schema['enum'][index]

            if objectValues is not None:
                objectValues[childName] = value
            else:
                self.json[parentName][childName] = value

            if onUpdate is not None:
                onUpdate()


        element.currentIndexChanged.disconnect()
        element.currentIndexChanged.connect(update_json)


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
            if childName not in objectValues:
                objectValues[childName] = self.getDefault(schema)

            if hasattr(element, 'setText'):
                element.setText(str(objectValues[childName]))
            elif hasattr(element, 'setPlainText'):
                element.setPlainText(str(objectValues[childName]))

        else:
            if childName not in self.json[parentName]:
                self.json[parentName][childName] = self.getDefault(schema)
        
            if hasattr(element, 'setText'):
                element.setText(str(self.json[parentName][childName]))
            elif hasattr(element, 'setPlainText'):
                element.setPlainText(str(self.json[parentName][childName]))

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
            
        element.textChanged.disconnect()
        element.textChanged.connect(update_json)
        element.setPlaceholderText(schema['title'])

        if self.shouldBeNumeric(schema):
            element.setAlignment(Qt.AlignRight)

        update_json()
            
    def setTableHeaders(self, element, data, schema):

        headers = []

        for attr, value in schema['items']['properties'].items():
            headers.append(value['title'])

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
        
    def validation_t_bestockung(self):
        """Show an error if the bestockung is not valid."""

        label_errors = self.lfbLayers()

        if len(label_errors) > 0:
            self.t_bestockungError.show()
            self.t_bestockungError.setText(str(label_errors[0].message))
        else:
            self.t_bestockungError.hide()

    
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
                #label_errors.append({
                #    "message": 'Falsche Anzahl an Bestockungsschichten',
                #    "relative_schema_path": ['allOf', 3, 'then', 'properties', 't_bestockung', 'properties', 't_bestockung', 'minItems']
                #})
                label_errors.append(exceptions.ValidationError(
                    message='Falsche Anzahl an Bestockungsschichten',
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
                    #label_errors.append({
                    #    "message": 'Falsche Schichtenkombination',
                    #    "relative_schema_path": ['properties','t_bestockung', 'properties','t_bestockung']
                    #})
                    label_errors.append(exceptions.ValidationError(
                        message='Falsche Schichtenkombination',
                        validator='minItems',
                        validator_value=rules_length[schicht_id]['min'],
                        instance=elements_unique,
                        schema_path=['allOf', 3, 'then', 'properties', 't_bestockung', 'properties', 't_bestockung', 'minItems']
                    ))
        
        return label_errors