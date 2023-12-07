import os
import threading

from qgis.core import QgsMessageLog, QgsPointXY, QgsPoint
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog, QScroller, QWidget, QFormLayout, QVBoxLayout, QGroupBox


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

    def _validate(self, schema, value):
        """Validate the json."""

        v = Draft7Validator(schema)

        return sorted(v.iter_errors(value), key=lambda e: e.path)


    def setUp(self):
        """Set up the form."""

        # General
        self.setUpGeneralTextField(self.spaufsucheaufnahmetruppkuerzel, 'spaufsucheaufnahmetruppkuerzel')
        self.setUpGeneralTextField(self.spaufsucheaufnahmetruppgnss, 'spaufsucheaufnahmetruppgnss')
        self.setUpGeneralComboBox(self.spaufsuchenichtbegehbarursacheid, 'spaufsuchenichtbegehbarursacheid')
        self.setUpGeneralComboBox(self.spaufsuchenichtwaldursacheid, 'spaufsuchenichtwaldursacheid')


    
    def setUpGeneralComboBox(self, element, childName):
        """Set up a combo box."""

        schema = self.schema['properties']['general']['properties'][childName]

        if hasattr(self, childName + 'Label'):
            getattr(self, childName + 'Label').setText(schema['title'])

        element.addItems(schema['enumLabels'])

        def update_json(index):
            self.json['general'][childName] = schema['enum'][index]

        element.currentIndexChanged.connect(update_json)

    def setUpGeneralTextField(self, element, childName):
        """Set up a text field."""

        schema = self.schema['properties']['general']['properties'][childName]

        element.setText(self.json['general'][childName])

        def update_json(text):
            errors = self._validate(schema, text)

            if len(errors) > 0:
                element.setStyleSheet("QLineEdit {\n border: 1px solid red;}")
            else:
                element.setStyleSheet("QLineEdit {\n border: 1px solid green;}")
            
            self.json['general'][childName] = text
            

        element.textChanged.connect(update_json)
        element.setPlaceholderText(schema['title'])

        
