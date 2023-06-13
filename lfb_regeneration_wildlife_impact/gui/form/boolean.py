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


UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'boolean.ui'))


class Boolean(QtWidgets.QWidget, UI_CLASS):
    inputChanged = QtCore.pyqtSignal(str)
    lfbInfoBox = QtCore.pyqtSignal(object)

    def __init__(self, interface, json, schema, key):
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

        self.lfbTextFieldLabel.setText(QCoreApplication.translate("FormFields", self.schema['title']))
        self.lfbCheckBox.stateChanged.connect(self.setInputText)

        self.lfbTextFieldDescriptionBtn.clicked.connect(self.triggerInfoBox)

        if "default" in self.schema and self.json[self.key] is None:
            self.setDefaultValue()

        self.validate() 

        self.show()

    def setDefaultValue(self):

        if "default" not in self.schema and self.json[self.key] is None:
            return
        
        self.json[self.key] = self.schema['default']
        #self.lfbTextField.setText(str(self.json[self.key]))

    def triggerInfoBox(self):
        self.lfbInfoBox.emit(self.schema)

    def setJson(self, newJson, setFields = True):
        
        self.json = newJson


        if setFields == False:
            return
        
        if self.key not in self.json:
            self.json[self.key] = None
        
        if self.json is not None and self.json[self.key] is not None:
            self.lfbCheckBox.setChecked(self.json[self.key])
            #self.lfbTextField.setText(str(self.json[self.key]))
        else:
            self.setDefaultValue()

        
    def setInputText(self, text):

        self.internJson[self.key] = text == 2

        self.validate()

    def validate(self):
        #jsonCpy = self.json.copy()
        #jsonCpy['name'] = self.lfbTextField.text()

        # https://python-jsonschema.readthedocs.io/en/stable/validate/
        v = Draft7Validator(self.schema)
        errors = sorted(v.iter_errors(self.internJson[self.key]), key=lambda e: e.path)

        self.json[self.key] = self.internJson[self.key]

        if self.json[self.key] is None:
            self.lfbTextFieldError.hide()
            self.lfbTextFieldHelp.hide()

        elif len(errors) == 0:
            self.lfbTextFieldError.hide()
            self.lfbTextFieldHelp.hide()
            #self.emitText()
        else:
            self.lfbTextFieldError.show()
            self.lfbTextFieldHelp.hide()
            for error in errors:
                self.lfbTextFieldError.setText(error.message)

        self.inputChanged.emit(str(self.json[self.key]))
