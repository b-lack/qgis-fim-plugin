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
import copy
import json

from qgis.core import QgsMessageLog, QgsProject, QgsVectorLayer, QgsJsonUtils, QgsField, QgsFields, QgsVectorFileWriter, QgsCoordinateTransformContext
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import QCoreApplication, QSettings, QTranslator
from qgis.PyQt.QtWidgets import QDialog, QTableWidgetItem

from PyQt5.uic import loadUi
from PyQt5 import QtCore

from jsonschema import Draft7Validator




UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'array_field.ui'))


class ArrayField(QtWidgets.QWidget, UI_CLASS):
    inputChanged = QtCore.pyqtSignal(object)

    def __init__(self, interface, json, schema, key):
        """Constructor."""

        from .views.arrayView import ArrayView

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        if(key not in json):
            json[key] = None

        
        
        self.json = json
        self.schema = schema
        self.key = key

        
        self.defaultValue = {} #copy.deepcopy(self.json[self.key][0])
        #del self.json[self.key][0]

        self.lfbArrayGroup.setTitle(self.schema['title'])
        
        self.child = ArrayView(interface, self.defaultValue , schema['items'], key)
        self.child.inputChanged.connect(self.setInputText)
        self.lfbArrayInput.addWidget(self.child)

        self.lfbAddBtn.clicked.connect(self.addRow)
        self.lfbAddBtn.setEnabled(False)

        tableHeaders = []

        for attr, value in self.schema['items']['properties'].items():
            
            tableHeaders.append(value['title'])
        
        self.setTableHeaders(tableHeaders)

        self.validate() 

        self.setTableData(self.json[self.key])

        self.show()


    def setTableHeaders(self, headers):
        self.lfbArrayOutput.setColumnCount(len(headers))
        self.lfbArrayOutput.setHorizontalHeaderLabels(headers)
        self.lfbArrayOutput.horizontalHeader().setStretchLastSection(True)
        #self.lfbArrayOutput.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        #self.lfbArrayOutput.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        #self.lfbArrayOutput.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

    def setTableData(self, data):
        self.lfbArrayOutput.setRowCount(len(data))

        for row in range(0, len(data)):
            idx = 0
            for attr, column in data[row].items():
                self.lfbArrayOutput.setItem(row, idx, QTableWidgetItem(str(column)))
                idx += 1

    def addRow(self):

        self.json[self.key].append(self.defaultValue)
        
    
        #self.lfbArrayOutput.clear()

        rowCount = self.lfbArrayOutput.rowCount()
        columnCount = self.lfbArrayOutput.columnCount()
        self.lfbArrayOutput.insertRow(rowCount)

        idx = 0
        for attr, column in self.defaultValue.items():
            self.lfbArrayOutput.setItem(rowCount, idx, QTableWidgetItem(str(column)))
            idx += 1

        self.inputChanged.emit(self.json)
        

        #for column in range(0, columnCount):
        #    self.lfbArrayOutput.setItem(rowCount, column, QTableWidgetItem('First Name'))
        
    def setJson(self, newJson, setFields = True):
        self.json = newJson

        self.setTableData(self.json[self.key])

    def setInputText(self, value):
        
        self.validate()
        

    def validate(self):

        QgsMessageLog.logMessage('data' + str(self.defaultValue), "LFB")
        QgsMessageLog.logMessage('schema' + str(self.schema), "LFB")

        # https://python-jsonschema.readthedocs.io/en/stable/validate/
        v = Draft7Validator(self.schema)
        errors = sorted(v.iter_errors([self.defaultValue]), key=lambda e: e.path)

        

        if len(errors) == 0:
            self.lfbAddBtn.setEnabled(True)
        else:
            QgsMessageLog.logMessage('errors' + str(errors[0]), "LFB")
            self.lfbAddBtn.setEnabled(False)

        self.inputChanged.emit(self.json)
