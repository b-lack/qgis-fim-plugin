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

from ...utils.helper import Utils
from ..setup.errors import ErrorsWidget


UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'saveBar.ui'))


class SaveBar(QtWidgets.QWidget, UI_CLASS):
    saveFeature = QtCore.pyqtSignal(object, bool)
    toHome = QtCore.pyqtSignal(bool)
    devButton = QtCore.pyqtSignal(bool)

    def __init__(self, interface, json, schema):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.interface = interface
        self.json = json
        self.schema = schema

        self.isValidating = True
        self.isValid = False

        self.maxErrors = 0
        self.currentErrors = 0

        self.currentFeature = None

        self.customErrors = []

        self.lfbSaveBtn.setDisabled(True)
        self.lfbSaveBtn.clicked.connect(self.saveBtnClicked)

        self.lfbDevBtn.clicked.connect(self.openState)
        #self.lfbDevBtn.hide()
        
        self.lfbHomeBtn.clicked.connect(self.openHome)
        self.lfbSchemaBtn.clicked.connect(self.openSchema)
        self.lfbSchemaBtn.hide()

        self.lfbErrorDialogBtn.hide()
        self.lfbErrorDialogBtn.clicked.connect(self.openErrorDialog)
        #self.errorsWidget = ErrorsWidget(self.interface, self.schema)
        #self.lfbErrorsLayout.addWidget(self.errorsWidget)
        

        self.lfbProgressBar.setValue(100)

        self.lfbActionRow.setContentsMargins(0,0,0,0)
        self.lfbProgressBar.setContentsMargins(0,0,0,0)

        self.lfbFokusFeature.hide()
        self.lfbFokusFeature.clicked.connect(self.focusFeature)

        self.validate(self.json)
        self.showMetaData()

        self.show()

    def showMetaData(self):
        metaData = Utils.getMetaData()
        self.lfbPluginVersion.setText('Version: ' + str(metaData['version']))

    def focusFeature(self):
        Utils.focusFeature(self.interface, self.currentFeature, True, 15000)

    def openSchema(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(json.dumps(self.schema))
        msgBox.exec()

    def openState(self):
        self.toHome.emit(True)
        self.devButton.emit(True)
        
    def openHome(self):
        self.saveFeature.emit(self.json, False)
        #self.toHome.emit(True)

    def saveBtnClicked(self):
        self.saveFeature.emit(self.json, True)

    def setFeatureAttributes(self, feature, key):
        layer = Utils.getLayerByName()
        fields = layer.fields()
        idx = fields.indexFromName(key)
        self.lfbId.setText(str(feature.attributes()[idx]))

        self.lfbFokusFeature.show()

    def setAttributes(self,feature, key):
        self.currentFeature = feature
        self.setFeatureAttributes(feature, key)

    def checkMinimumSet(self, jsonToTest, errorLen):
        return True
    
        if errorLen == 0:
            self.lfbProgressBar.setStyleSheet("QProgressBar::chunk "
                  "{"
                    "background-color: green;"
                  "}")
            self.lfbProcessInfo.setText("Daten können jetzt gespeicher werden.")
            return True
        elif jsonToTest['coordinates']['latitude'] != None and jsonToTest['coordinates']['longitude'] != None and jsonToTest['general']['aufnahmetrupp'] != None and jsonToTest['general']['GNSSDevice'] != None:
            self.lfbProgressBar.setStyleSheet("QProgressBar::chunk "
                  "{"
                    "background-color: orange;"
                  "}")
            self.lfbProcessInfo.setText("Deine Daten werden automatisch als Entwurf gespeichert.")
            return True
        else:
            self.lfbProgressBar.setStyleSheet("QProgressBar::chunk "
                  "{"
                    "background-color: red;"
                  "}")
            self.lfbProcessInfo.setText("Fülle mindestens die rot markierten Felder aus um die Daten als Entwurf zu speichern.")
            return False
            
    
    def getNamedError(self, error):
        return True

    def openErrorDialog(self):

        for error in self.errors:
            QgsMessageLog.logMessage(str(error.message) + ' ' + str(error.relative_schema_path), 'LFB')

        return
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText('llll')
        msgBox.exec()

    def validate(self, jsonToTest):

        self.customErrors = []

        self.json = jsonToTest
        
        v = Draft7Validator(self.schema)
        self.errors = sorted(v.iter_errors(jsonToTest), key=lambda e: e.path)

        if self.maxErrors < len(self.errors):
            self.maxErrors = len(self.errors)

        self.currentErrors = len(self.errors)

        self.lfbProgressBar.setValue(int(100 - self.currentErrors * 100 / self.maxErrors))

        if len(self.errors) == 0:
            #self.isValid = True
            self.lfbErrorDialogBtn.setText('')
            self.lfbSaveBtn.setDisabled(False)
        else:
            self.lfbSaveBtn.setDisabled(True)
            #self.isValid = False
            self.lfbErrorDialogBtn.setText(str(len(self.errors)) + ' verbleibende Fehler.')
            
       
       
        #self.errorsWidget.updateErrors(self.errors)

        return len(self.errors) == 0


    def checkIsForest(self, jsonToTest):
        messages = []


        if jsonToTest['general']['spaufsuchenichtbegehbarursacheid'] is None or jsonToTest['general']['spaufsuchenichtbegehbarursacheid'] == 2: # begehbar
            messages += [
                {
                    'message': 'Der Waldtyp ist nicht gesetzt.',
                    'path': ['general', 'waldtyp'],
                    'level': 'error'
                }
            ]
        else:
            return messages
        
        return messages