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

#import json

from qgis.core import QgsMessageLog, QgsProject, QgsVectorLayer, QgsJsonUtils, QgsField, QgsFields, QgsVectorFileWriter, QgsCoordinateTransformContext
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import QCoreApplication, QSettings, QTranslator
from qgis.PyQt.QtWidgets import QDialog

from PyQt5.uic import loadUi
from PyQt5 import QtCore

from ...form.textfield import TextField
from ..dropdown import DropDown
from ..array_field import ArrayField
from ..boolean import Boolean
from .object_view import ObjectView

UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'array_default.ui'))


class ArrayView(QtWidgets.QWidget, UI_CLASS):
    inputChanged = QtCore.pyqtSignal(object, int)

    def __init__(self, interface, json, schema, attr, schemaErrors = []):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.json = json
        self.editRow = None
        self.attr = attr

        self.show()

        self.fieldArray = []
        
        items = schema['properties'].items()

        row = 0
        column = 0
        columnSpan = 1

        for attr, value in items:

            valueType = value['type']

            if 'enum' in value:
                field = DropDown(interface, self.json, value, attr)
            elif valueType == 'boolean':
                field = Boolean(interface, self.json, value, attr)
                #field.lfbInfoBox.connect(self.infoBoxClicked)
            elif valueType == 'object':
                field = ObjectView(interface, self.json, value, attr, schemaErrors)
            else:
                field = TextField(interface, self.json, value, attr, schemaErrors)


            if '$FIMColumn' in value:
                column = value['$FIMColumn']
                if column == 0:
                    row += 1
                columnSpan = 1
            else:
                row += 1
                column = 0
                columnSpan = -1
                
                


            self.lfbTabLayout.addWidget(field, row, column, 1, columnSpan)
            field.inputChanged.connect(self.emitText)
            
            self.fieldArray.append(field)

    def setJson(self, newJson, setFields = True, editRow = None):
        
        self.json = newJson
        self.editRow = editRow

        for field in self.fieldArray:
            field.setJson(self.json, setFields)

    def emitText(self, childJson = None, key = None):
        self.inputChanged.emit(self.json, self.editRow)

    def triggerErrors(self, errors):
        for field in self.fieldArray:
            field.setSchemaErrors(errors)