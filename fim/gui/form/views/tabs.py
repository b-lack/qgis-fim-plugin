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

from qgis.core import QgsMessageLog
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog, QScroller

from PyQt5 import QtCore

from qgis.utils import plugins

from ...form.textfield import TextField
from ..textarea import TextArea
from ..dropdown import DropDown
from ..array_field import ArrayField
from ..boolean import Boolean
from ..views.object_view import ObjectView
from ....utils.helper import Utils

from ...plugins.find_position.setup_device import SetupDevice

UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'tab_default.ui'))


class Tabs(QtWidgets.QWidget, UI_CLASS):
    inputChanged = QtCore.pyqtSignal(object, str, bool)
    nextTab = QtCore.pyqtSignal(bool)

    def __init__(self, interface, json, schema, attr, inheritedErrors = [], schemaErrors = []):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.interface = interface
        self.json = json
        self.attr = attr
        self.schema = schema
        self.inheritedErrors = inheritedErrors
        self.schemaErrors = schemaErrors

        self.infoTitle = ""

        self.fieldArray = []

        scroll = QScroller.scroller(self.lfbTabScroll.viewport())
        scroll.grabGesture(self.lfbTabScroll.viewport(), QScroller.LeftMouseButtonGesture)
        
        try:
            self.lfbTabBtnBack.clicked.disconnect()
            self.lfbTabBtnFwd.clicked.disconnect()
        except:
            pass
        self.lfbTabBtnBack.clicked.connect(self.on_lfbTabBtnBack_clicked)
        self.lfbTabBtnFwd.clicked.connect(self.on_lfbTabBtnFwd_clicked)

        #if 'title' in schema:
        #    self.lfbObjectHeadeline.setText(schema['title'])
        #else:
        #    self.lfbObjectHeadeline.hide()

        self.lfbInfoButton.clicked.connect(self.tabInfoBoxClicked)
        self.lfbTabDescription.hide()
        if 'description' in schema:
            #self.lfbObjectDescription.setText(schema['description'])
            self.lfbInfoButton.show()
        else:
            #self.lfbObjectDescription.hide()
            self.lfbInfoButton.hide()

        if 'properties' in schema:
            items = schema['properties'].items()
        else:
            items = schema['items'].items()

        for attr, value in items:

            field = None
            
            valueType = value['type']

            if valueType == 'array':
                field = ArrayField(interface, self.json, value, attr, schemaErrors)
            elif valueType == 'object':
                if '$plugin' in value:
                    
                    if Utils.pluginAvailable(value['$plugin']):
                        # https://gis.stackexchange.com/questions/403501/using-qgis-plugin-from-another-plugin

                        from gnavs.gui.recording.recording import Recording
                        field = Recording(self.interface)
                        field.aggregatedValuesChanged.connect(self.aggregatedValuesChanged)

                    else:
                        QgsMessageLog.logMessage("Plugin not available: " + value['$plugin'], 'LFB')
                        field = SetupDevice(interface, self.json, value, attr, self.inheritedErrors)
                else:        
                    field = ObjectView(interface, self.json, value, attr, self.inheritedErrors)
            elif valueType == 'boolean':
                field = Boolean(interface, self.json, value, attr)
                field.lfbInfoBox.connect(self.infoBoxClicked)
            elif 'enum' in value:
                field = DropDown(interface, self.json, value, attr)
                field.lfbInfoBox.connect(self.infoBoxClicked)
            elif 'maxLength' in value and value['maxLength'] >= 1000:
                field = TextArea(interface, self.json, value, attr)
                field.lfbInfoBox.connect(self.infoBoxClicked)
            else:
                field = TextField(interface, self.json, value, attr)
                field.lfbInfoBox.connect(self.infoBoxClicked)
            
            
            if(field is not None):
                self.lfbTabLayout.addWidget(field)
                invert_op = getattr(field, "inputChanged", None)
                if callable(invert_op):
                    field.inputChanged.connect(self.onInputChanged)

                self.fieldArray.append(field)

        self.lfbTabInfoWidget.hide()

        self.show()

    def aggregatedValuesChanged(self, gpsInfos):
        """Update the aggregated values"""
        from gnavs.gui.measurement.aggregation import Aggregation

        aggregation = Aggregation(self.interface)
        aggregated = aggregation.aggregate(gpsInfos)

        self.json['istgeom_x'] = aggregated['latitude']
        self.json['istgeom_y'] = aggregated['longitude']
        self.json['istgeom_elev'] = aggregated['elevation']
        self.json['istgeom_hdop'] = aggregated['hdop']
        self.json['istgeom_vdop'] = aggregated['vdop']
        #self.json['istgeom_pdop'] = aggregated['pdop']
        self.json['istgeom_sat'] = int(aggregated['satellitesUsed'])

        self.inputChanged.emit(self.json, self.attr, True)

        #self.onInputChanged(self, self.json)

    def tabInfoBoxClicked(self):

        self.lfbInfoBoxTitle.setText(self.schema['title'])
        self.lfbInfoBox.setText(self.schema['description'])

        if self.lfbTabInfoWidget.isVisible():
            self.lfbTabInfoWidget.hide()
        else:
            self.lfbTabInfoWidget.show()

    def on_lfbTabBtnBack_clicked(self):
        self.nextTab.emit(False)

    def on_lfbTabBtnFwd_clicked(self):
        self.nextTab.emit(True)

    def infoBoxClicked(self, info):

        if self.infoTitle == info['title']:
            if self.lfbTabInfoWidget.isVisible():
                self.lfbTabInfoWidget.hide()
            else:
                self.lfbTabInfoWidget.show()
        else:
            self.lfbInfoBox.setText(info['description'])
            self.lfbTabInfoWidget.show()

        self.infoTitle = info['title']


    def setJson(self, newJson, setFields = True):
        self.json.update(newJson)
        #self.json = newJson

        for field in self.fieldArray :
            invert_op = getattr(field, "setJson", None)
            if callable(invert_op):
                field.setJson(self.json, setFields)

    def onInputChanged(self, json, attr=None, forceUpdate = False):
        """Update the json object"""
        self.inputChanged.emit(self.json, self.attr, forceUpdate)