# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LfbRegenerationWildlifeImpactDialog
                                 A QGIS plugin
 Lfb Regeneration and Wildlife Impact Monitoring
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-05-08
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Grünecho
        email                : support@grunecho.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

import json

from qgis.core import QgsMessageLog, QgsProject, QgsVectorLayer, QgsJsonUtils, QgsField, QgsFields, QgsVectorFileWriter, QgsCoordinateTransformContext
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import QCoreApplication, QSettings, QTranslator
from qgis.PyQt.QtWidgets import QDialog

from PyQt5.uic import loadUi
from PyQt5 import QtCore

from jsonschema import Draft7Validator


from PyQt5.QtGui import QDoubleValidator

from ...utils.helper import Utils


UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'textfield.ui'))


class TextField(QtWidgets.QWidget, UI_CLASS):
    inputChanged = QtCore.pyqtSignal(object, str)
    lfbInfoBox = QtCore.pyqtSignal(object)

    def __init__(self, interface, json, schema, key, schemaErrors = []):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        if(key not in json):
            json[key] = None

        self.json = json
        self.internJson = json.copy()
        self.schema = schema
        self.key = key
        self.defaultValue = self.json[self.key]
        self.isValid = False
        self.schemaErrors = schemaErrors
        self.errors = []
        self.validationErrors = []

        placeholderText = QCoreApplication.translate("FormFields", self.schema['title'])

        self.lfbTextFieldLabel.setText(QCoreApplication.translate("FormFields", self.schema['title']))

        self.lfbTextField.setPlaceholderText(placeholderText) 
        self.lfbTextField.setToolTip(placeholderText)

        try:
            self.lfbTextField.returnPressed.disconnect()
            self.lfbTextField.textChanged.disconnect()
            self.lfbTextField.editingFinished.disconnect()
            self.lfbTextFieldDescriptionBtn.clicked.disconnect()
        except:
            pass

        
        
        
        

        if self.lfbTextFieldHelp is not None and 'description' in self.schema:
            self.lfbTextFieldHelp.setText(self.schema['description'])
        else:
            self.lfbTextFieldHelp.setText('')

        self.lfbTextField.undoAvailable = True

        if self.lfbTextFieldDescriptionBtn is not None and 'description' in self.schema:
            self.lfbTextFieldDescriptionBtn.hide()

            self.lfbTextFieldDescriptionBtn.clicked.connect(self.triggerInfoBox)

        if "readOnly" in self.schema:
            self.lfbTextField.setReadOnly(self.schema['readOnly'])
            self.lfbTextField.setStyleSheet("background-color: #e0e0e0;")

        if "unit" in self.schema:
            self.lfbTextFieldUnit.setText(self.schema['unit'])

        if self.shouldBeNumeric():
            #self.lfbTextField.setValidator(QDoubleValidator())
            self.lfbTextField.setAlignment(QtCore.Qt.AlignRight)


        self.setDefaultValue()

        self.validate()
        self.displayErrors(False)

        self.lfbTextField.returnPressed.connect(self.onEnter)
        self.lfbTextField.textChanged.connect(self.setInputText)
        self.lfbTextField.editingFinished.connect(self.editingFinished)

        self.show()

    def onEnter(self):
        self.focusNextChild()

    def shouldBeNumeric(self):
        return (type(self.schema['type']) == str and (self.schema['type'] == "number" or self.schema['type'] == "integer") or (hasattr(self.schema['type'], "__len__") and ("integer" in self.schema['type'] or "number" in self.schema['type'])))
    def shouldBeNumber(self):
        return (type(self.schema['type']) == str and (self.schema['type'] == "number") or (hasattr(self.schema['type'], "__len__") and ("number" in self.schema['type'])))
    def shouldBeInteger(self):
        return (type(self.schema['type']) == str and (self.schema['type'] == "integer") or (hasattr(self.schema['type'], "__len__") and ("integer" in self.schema['type'])))

    def setDefaultValue(self):

        

        if not Utils.isAttributeRequired(self.schema, self.key):
            del self.json[self.key]# = null
            return

        #self.lfbTextField.setText("")

        if "default" not in self.schema:
            return
        
        self.json[self.key] = self.schema['default']

        if self.json[self.key] is not None:
            self.lfbTextField.setText(str(self.json[self.key]))
        else:
            self.lfbTextField.setText('')

    def triggerInfoBox(self):
        self.lfbInfoBox.emit(self.schema)

    def setJson(self, newJson, setFields = True):

        self.json = newJson

        #if self.key not in self.json:
        #    self.json[self.key] = None
        #elif self.key is newJson:
        #    self.json[self.key] = newJson[self.key]
        #else:
        #    self.json[self.key] = None
        
        
        #if self.key not in self.json or self.json is None or self.json[self.key] is None:
        #    self.setDefaultValue()

        if self.key in self.json and self.json[self.key] is not None:
            self.lfbTextField.setText(str(self.json[self.key]))
        else:
            self.lfbTextField.setText('')

    def isfloat(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
        
    def setInputText(self, text):
        valueStr = self.lfbTextField.text()

        if valueStr == "":
            value = None
        elif self.shouldBeNumber() and self.isfloat(valueStr):
            value = float(valueStr)
        elif self.shouldBeInteger() and valueStr.isnumeric():
            value = int(valueStr)
        else:
            value = valueStr

        self.internJson[self.key] = value

        self.validate()
        self.mergeErrors()
        self.displayErrors(True)

    def editingFinished(self):
        self.validate()
        self.mergeErrors()
        self.displayErrors(True)

    def setSchemaErrors(self, schemaErrors):
        self.schemaErrors = schemaErrors
        
        self.validate()
        self.mergeErrors()
        self.displayErrors(False)

    def mergeErrors(self):

        self.errors = []

        for error in self.schemaErrors:
            if hasattr(error, 'relative_schema_path') == False:
                continue

            if self.key in error.relative_schema_path:
                self.errors.append(error)

        for error in self.validationErrors:
            self.errors.append(error)

    def validate(self):

        v = Draft7Validator(self.schema)
        self.validationErrors = sorted(v.iter_errors(self.internJson[self.key]), key=lambda e: e.path)
        

    def displayErrors(self, emit = False):

        #jsonCpy = self.json.copy()
        #jsonCpy['name'] = self.lfbTextField.text()

        # https://python-jsonschema.readthedocs.io/en/stable/validate/
        #v = Draft7Validator(self.schema)
        #errors = sorted(v.iter_errors(self.internJson[self.key]), key=lambda e: e.path)

        self.json[self.key] = self.internJson[self.key]

        isValid = False

        if self.json[self.key] is None and not Utils.schemaTypeHasNull(self.schema):
            self.lfbTextFieldError.hide()
            self.lfbTextFieldSuccess.hide()
            self.lfbTextFieldHelp.show()
            self.lfbTextField.setStyleSheet("QLineEdit {\n	border: 2px solid red;\n	padding: 4px;\n}")
        elif len(self.errors) == 0:
            self.lfbTextFieldError.hide()
            self.lfbTextFieldSuccess.hide()
            self.lfbTextFieldHelp.show()
            self.lfbTextField.setStyleSheet("QLineEdit {\n	border: 2px solid green;\n	padding: 4px;\n}")
            isValid = True
        else:
            self.lfbTextFieldError.show()
            self.lfbTextFieldSuccess.hide()
            self.lfbTextFieldHelp.hide()
            self.lfbTextField.setStyleSheet("QLineEdit {\n	border: 2px solid red;\n	padding: 4px;\n}")

            for error in self.errors:
                self.lfbTextFieldError.setText(error.message)

        if emit: # and self.isValid != isValid
            self.inputChanged.emit(self.json[self.key], self.key)

        self.isValid = isValid
