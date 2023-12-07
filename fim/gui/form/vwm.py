import os
import threading

from qgis.core import QgsMessageLog, QgsPointXY, QgsPoint
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog, QScroller, QWidget, QFormLayout, QVBoxLayout, QGroupBox
from PyQt5.QtCore import Qt

from jsonschema import Draft7Validator, exceptions


UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'vwm.ui'))


class VWM(QtWidgets.QWidget, UI_CLASS):

    def __init__(self, interface, json, schema):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.interface = interface
        self.json = json
        self.schema = schema

        QgsMessageLog.logMessage("--------------setUp------------", 'FIM')
        self.setUp()

        self.show()

    


    def setUp(self):
        """Set up the form."""

        # General
        self.setUpTextField('general', 'spaufsucheaufnahmetruppkuerzel')
        self.setUpTextField('general', 'spaufsucheaufnahmetruppgnss')
        self.setUpGeneralComboBox('general', 'spaufsuchenichtbegehbarursacheid')
        self.setUpGeneralComboBox('general', 'spaufsuchenichtwaldursacheid')

        # Coordinates
        
        self.setUpGeneralComboBox('coordinates', 'spaufsucheverschobenursacheid')
        self.setUpGeneralComboBox('coordinates', 's_perma')
        self.setUpTextField('coordinates', 'istgeom_y')
        self.setUpTextField('coordinates', 'istgeom_x')
        self.setUpTextField('coordinates', 'istgeom_elev')
        self.setUpTextField('coordinates', 'istgeom_sat')
        self.setUpTextField('coordinates', 'istgeom_hdop')
        self.setUpTextField('coordinates', 'istgeom_vdop')

        # Baumplot
        self.setUpTextField('baumplot1', 'azimuttransektploteins')
        self.setUpArray('baumplot1', 'baumplot1')


        #Transekt
        self.setUpGeneralComboBox('transekt', 'schutzmassnahmeid')
        self.setUpTextField('transekt', 'transektstoerungursache')


        # Weiserpflanzen
        self.setUpTextField('weiserpflanzen', 'krautanteil')
        self.setUpObject('weiserpflanzen', 'kraut')

    # UTILS
    def _validate(self, schema, value):
        """Validate the json."""

        v = Draft7Validator(schema)

        return sorted(v.iter_errors(value), key=lambda e: e.path)
    
    def getDefault(self, schema):
        """Set the default value."""

        if "default" in schema:
            return schema['default']
        
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
                parentName,
                child,
                self.json[parentName][childName],
                schema['properties'][child], onUpdate)

    # ARRAY
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
            

            #objectValues = {}
        def refresh_fields():
            self.setUpTextField(
                'baumplot1',
                'azimut',
                objectValues,
                schema['items']['properties']['azimut'])
            self.setUpTextField(
                'baumplot1',
                'distanz',
                objectValues,
                schema['items']['properties']['distanz'])
        
        self.baumplotAdd.clicked.connect(update_json)
        refresh_fields()

    # COMBOBOX
    def setUpGeneralComboBox(self, parentName, childName):
        """Set up a combo box."""

        if hasattr(self, childName):
            element = getattr(self, childName)
        else:
            return



        schema = self.schema['properties'][parentName]['properties'][childName]

        if hasattr(self, childName + 'Label'):
            getattr(self, childName + 'Label').setText(schema['title'])

        element.addItems(schema['enumLabels'])

        def update_json(index):
            self.json[parentName][childName] = schema['enum'][index]

        element.currentIndexChanged.connect(update_json)


    # TEXTFIELD
    def setUpTextField(self, parentName, childName, objectValues = None, schema = None, onUpdate = None):
        """Set up a text field."""

        if hasattr(self, childName):
            element = getattr(self, childName)
        else:

            QgsMessageLog.logMessage("Element " + childName + " not found in " + parentName, 'FIM')
            return
        
        if schema is None: # if root schema
            schema = self.schema['properties'][parentName]['properties'][childName]


        if childName not in self.json[parentName]:
            self.json[parentName][childName] = self.getDefault(schema)
        
        if hasattr(element, 'setText'):
            element.setText(str(self.json[parentName][childName]))
        elif hasattr(element, 'setPlainText'):
            element.setPlainText(str(self.json[parentName][childName]))

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
                if hasattr(self, childName + 'Error'):
                    getattr(self, childName + 'Error').setText(str(errors[0].message))
                element.setStyleSheet("QLineEdit {\n border: 2px solid red;}")
            else:
                if hasattr(self, childName + 'Error'):
                    getattr(self, childName + 'Error').setText('')
                element.setStyleSheet("QLineEdit {\n border: 2px solid green;}")
            
            if objectValues is not None:
                objectValues[childName] = value
            else:
                self.json[parentName][childName] = value

            if onUpdate is not None:
                onUpdate()
            

        element.textChanged.connect(update_json)
        element.setPlaceholderText(schema['title'])

        if self.shouldBeNumeric(schema):
            element.setAlignment(Qt.AlignRight)

        update_json()
            
        

        
