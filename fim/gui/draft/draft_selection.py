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
import uuid


from qgis.core import QgsFeature, QgsExpressionContextUtils, QgsProject, QgsVectorLayer, QgsField, QgsFields, QgsMessageLog
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import QDateTime, QVariant, QItemSelection, QItemSelectionModel, Qt
from qgis.PyQt.QtWidgets import QDialog, QScroller, QPushButton, QMessageBox, QAbstractItemView
from PyQt5.QtGui import QCursor

from PyQt5.uic import loadUi
from PyQt5 import QtCore

from .io_btn import IoBtn
from .draft_item import DraftItem
from ...utils.helper import Utils

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'draft_selection.ui'))


class DraftSelection(QtWidgets.QWidget, UI_CLASS):
    """DraftSelection Plugin Implementation."""

    draftSelected = QtCore.pyqtSignal(object, int, object)
    folderSelected = QtCore.pyqtSignal(str)

    def __init__(self, interface):
        """Constructor."""

        # super(LfbRegenerationWildlifeImpactDialog, self).__init__(parent)
        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.LAYER_PREFIX = Utils.getLayerName()
        self.LAYER_VERSION = Utils.getLayerVersion()

        # QGIS interface
        self.iface = interface

        self.vl = None

        self.fields = QgsFields()
        self.fields.append(QgsField("id", QVariant.String))
        self.fields.append(QgsField("los_id", QVariant.String))
        self.fields.append(QgsField("status", QVariant.Bool))

        self.fields.append(QgsField("type", QVariant.String))
        self.fields.append(QgsField("version", QVariant.String))
        
        self.fields.append(QgsField("created", QVariant.DateTime))
        self.fields.append(QgsField("modified", QVariant.DateTime))
        self.fields.append(QgsField("workflow", QVariant.Int))
        self.fields.append(QgsField("losnr", QVariant.String))

        self.fields.append(QgsField("form", QVariant.String))
        self.fields.append(QgsField("valid", QVariant.Bool))
        
        self.currentFeatureId = None

        self.addIoButton()

        self.empty_draft_label.hide()

        QScroller.grabGesture(self.scrollArea, QtWidgets.QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_2, QtWidgets.QScroller.LeftMouseButtonGesture)
        QScroller.grabGesture(self.scrollArea_3, QtWidgets.QScroller.LeftMouseButtonGesture)

        QScroller.grabGesture(self.lfbDraftTableWidget, QtWidgets.QScroller.LeftMouseButtonGesture)

        self.tabWidget.hide()

        self.setup_table_widget()

        self.show()

    def createButton(self, parent, label, type = 'raised'):
        btn = QPushButton(parent)

        if type == 'text':
            btn.setStyleSheet("color: red; background: transparent; border: none;")
        else:
            btn.setStyleSheet("color: green;")

        btn.setText(label)
        btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        return btn
    
    def focusFeature(self, feature, select = False):
        """Focus the feature in the map canvas."""
        Utils.focusFeature(self.iface, feature, select, None)

    def _row_selected(self):
        """Select the row in the table widget"""

        self.vl = Utils.getLayerById()
        if self.vl is None:
            return
        
        featureList = self.vl.getFeatures()
        
        _selected_rows = self.lfbDraftTableWidget.selectionModel().selectedRows()

        features = []
        
        for idx, row in enumerate(_selected_rows):
            id_from_item = self.lfbDraftTableWidget.item(row.row(), 1).text()

            for feature in featureList:
                if feature['id'] == id_from_item:
                    features.append(feature)
                    self.focusFeature(feature, True)
                    break
        
        Utils.selectFeatures(features)
            
        return
        item = self.lfbDraftTableWidget.currentRow()
        id_from_item = self.lfbDraftTableWidget.item(item, 1).text()
        QgsMessageLog.logMessage(id_from_item, 'FIM')
        
        featureList = self.vl.getFeatures()
        feature = list(featureList)[item]

        self.focusFeature(feature, True)


    def setup_table_widget(self):
        """Setup the table widget"""
        #self.lfbDraftTableWidget.itemSelectionChanged.connect(self._row_selected)
        self.lfbDraftTableWidget.cellClicked.connect(self._row_selected)

    def set_selected_rows(self):
        """Set the selected rows in the table widget"""
        self.vl = Utils.getLayerById()
        if self.vl is None:
            return
        
        featureList = self.vl.getFeatures()
        selectedFeatures = Utils.getSelectedFeaturesFim()
        self.lfbDraftTableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        
        self.lfbDraftTableWidget.clearSelection()
                

        for idx, feature in enumerate(selectedFeatures):
            for row in range(self.lfbDraftTableWidget.rowCount()):
                _item = self.lfbDraftTableWidget.item(row, 1)
                if _item and _item.text() == feature['id']:
                    index = self.lfbDraftTableWidget.model().index(row, 1)
                    self.lfbDraftTableWidget.selectionModel().select(index, QItemSelectionModel.Select | QItemSelectionModel.Rows)


    def updateTableWidget(self):
        """Read the layer and lists features"""

        self.vl = Utils.getLayerById()
        

        if self.vl is None:
            return

        featureList = self.vl.getFeatures()

        headers = []
        headers.append('')
        headers.append('id')
        headers.append('Status')

        headers.append('Trupp')
        headers.append('GNSS-Gerät')
        
        headers.append('Geändert')
        #headers.append('FOKUS')
        headers.append('Erstellt')
        
        headers.append('Typ')
        headers.append('')

        self.lfbDraftTableWidget.setRowCount(self.vl.featureCount())
        self.lfbDraftTableWidget.setColumnCount(len(headers))
        self.lfbDraftTableWidget.setHorizontalHeaderLabels(headers)

        self.lfbDraftTableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        self.lfbDraftTableWidget.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.lfbDraftTableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.lfbDraftTableWidget.setStyleSheet("QTableWidget::item { margin: 2px }")

        #self.lfbDraftTableWidget.verticalHeader().setDefaultSectionSize(20)

        self.set_selected_rows()
        
        for idx, feature in enumerate(featureList):


            losId = feature['id']
            if feature['los_id'] is not None:
                losId = feature['los_id']
            
            self.lfbDraftTableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(losId))
            
            done = feature['status'] # False
            if done == False:
                doneText = 'ToDo'
            else:
                doneText = 'Abgeschlossen'
            self.lfbDraftTableWidget.setItem(idx, 2, QtWidgets.QTableWidgetItem(doneText))

            properties = json.loads(feature['form'])
            trupp_text = properties['general']['spaufsucheaufnahmetruppkuerzel'] if properties['general']['spaufsucheaufnahmetruppkuerzel'] is not None else '-'
            self.lfbDraftTableWidget.setItem(idx, 3, QtWidgets.QTableWidgetItem(trupp_text))
            gnss_text = properties['general']['spaufsucheaufnahmetruppgnss'] if properties['general']['spaufsucheaufnahmetruppgnss'] is not None else '-'
            self.lfbDraftTableWidget.setItem(idx, 4, QtWidgets.QTableWidgetItem(gnss_text))

            btn = self.createButton(self.lfbDraftTableWidget, 'BEARBEITEN')
            btn.clicked.connect(self._listWidgetClicked(feature))
            self.lfbDraftTableWidget.setCellWidget(idx, 0, btn)

            #btn = self.createButton(self.lfbDraftTableWidget, 'FOCUS')
            #btn.clicked.connect(self._focusFeature(feature))
            #self.lfbDraftTableWidget.setCellWidget(idx, 3, btn)

            self.lfbDraftTableWidget.setItem(idx, 5, QtWidgets.QTableWidgetItem(feature['created'].toString() if feature['created'] else '-'))
            self.lfbDraftTableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

            self.lfbDraftTableWidget.setItem(idx, 6, QtWidgets.QTableWidgetItem(feature['modified'].toString() if feature['modified'] else '-'))
            self.lfbDraftTableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

            self.lfbDraftTableWidget.setItem(idx, 7, QtWidgets.QTableWidgetItem(feature['type'].toString() if feature['type'] else 'VWM'))

            btn = self.createButton(self.lfbDraftTableWidget, 'LÖSCHEN', 'text')
            btn.clicked.connect(self._removeFeature(feature))
            self.lfbDraftTableWidget.setCellWidget(idx, 8, btn)

        

    def _focusFeature(self, feature):
        def focusFeature():
            self.focusFeature(feature)
        return focusFeature
    
    def _listWidgetClicked(self, feature):
        def listWidgetClicked():
            self.listWidgetClicked(feature)
        return listWidgetClicked
    
    def _removeFeature(self, feature):
        def removeFeature():
            self.removeRow(feature)
        return removeFeature
    
    def removeRow(self, feature):
        """Remove the feature from the layer."""

        msgBox = QMessageBox()
        msgBox.setText("Möchtest du den Stichprobenpunkt einschließlich der aufgenommenen Daten wirklich löschen?")
        msgBox.setWindowTitle("Stichprobenpunkt löschen")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.removeFeature(feature.id())

    def update(self):
        """Update the feature lists"""

        visibleFeatures = 0
        if self.vl is not None:

            self.updateTableWidget()
            self.ioBtn.update()
            return

            draftCount = self.readDrafts()

            if draftCount is None:
                draftCount = 0

            visibleFeatures += draftCount
            self.tabWidget.setTabText(1, 'Entwürfe (' + str(draftCount) + ')')
            
            
            selectedCount = self.readSelected()
            if selectedCount is None:
                selectedCount = 0
            visibleFeatures += selectedCount
            self.tabWidget.setTabText(0, 'Ausgewählt (' + str(selectedCount) + ')')

            doneCount = self.readDone(True)
            if doneCount is None:
                doneCount = 0
            visibleFeatures += doneCount
            self.tabWidget.setTabText(2, 'Abgeschlossen (' + str(doneCount) + ')')
            
            

        #if visibleFeatures == 0:
        #    self.empty_draft_label.show()
        #else:
        #    self.empty_draft_label.hide()

    def imported(self, path):
        """Imported a draft from a file"""

        self.update()
        #self.tabWidget.setCurrentIndex(1)

    def addIoButton(self):
        """Add the import/export button"""

        self.ioBtn = IoBtn(self.iface)
        self.ioBtn.imported.connect(self.imported)
        self.lfbIoWidget.addWidget(self.ioBtn)

    def resetCurrentDraft(self, featureId):
        self.currentFeatureId = featureId

    def setupDraftLayer(self):
        """Check if private layer exists"""
        
        layer = Utils.getLayerById()

        if layer is not None:
            self.vl = layer

            folder = os.path.dirname(self.vl.dataProvider().dataSourceUri())
            self.folderSelected.emit(str(folder))

            self.update()
            return

        # create new layer
        self.vl = QgsVectorLayer("Point", self.LAYER_PREFIX + '-' + self.LAYER_VERSION, "memory")
        self.vl.setName(self.LAYER_PREFIX)
        QgsExpressionContextUtils.setLayerVariable(self.vl, 'LFB-NAME', self.LAYER_PREFIX)
        QgsExpressionContextUtils.setLayerVariable(self.vl, 'LFB-VERSION', self.LAYER_VERSION)
        
        self.setupSymbols()

        pr = self.vl.dataProvider()

        # add fields
        pr.addAttributes(self.fields)
        self.vl.updateFields()

        QgsProject.instance().addMapLayer(self.vl)

    
    def listWidgetClicked(self, feature):
        """on widget clicked"""

        json_object = json.loads(feature['form'])
        self.currentFeatureId = feature.id()
        self.draftSelected.emit(json_object, self.currentFeatureId, feature)
        return

        featureList = self.vl.getFeatures()
        for feat in featureList:
            QgsMessageLog.logMessage(str(feat.id()), 'FIM')
            if(feat.id() == item):
                QgsMessageLog.logMessage("--------------listWidgetClicked------------"+ str(item), 'FIM')
                json_object = json.loads(feat['form'])
                self.currentFeatureId = feat.id()
                self.draftSelected.emit(json_object, self.currentFeatureId, feat)
                break
    
    
    def setupSymbols(self):
        """Setup symbols for the layer"""

        # https://gis.stackexchange.com/questions/380571/is-there-a-way-to-create-arrow-subsymbol-on-top-of-geometry-generated-symbol-usi

        values = (
            ('Von FU heruntergeladen - offline bei FU', 4, 4, '#decc44'),
            ('Sps', 1, 5, '#e62323'),
            ('bearbeitet oder hochgeladen', 5, 6, '#729b6f'),
            ('kontrolle', 7, 8, '#f3a6b2'),
            ('wiederholungsaufnahme', 11, 12, '#b80808'),
            ('sonstige', 13, 100, '#1228d1')
        )
        
        dirname = os.path.dirname(__file__)
        filename = os.path.realpath(os.path.join(dirname, '../..', 'layerstyles', 'express_4.qml'))

        self.vl.loadNamedStyle(filename)

        self.vl.triggerRepaint()
        

    # _deprecated
    def readLayer(self):
        pass
        """Read the layer and return the features"""
        featureList = self.vl.getFeatures()
        sorted_featureList = sorted(featureList, key=lambda x: x['created'], reverse=True)

        properties = []

        for feature in sorted_featureList:
            properties.append(json.loads(feature['properties']))

        return properties
    
    def readSelected(self):
        """Read the layer and lists the selected features"""

        self.vl = Utils.getLayerById()
        countFeatures = 0

        if self.vl is None:
            return

        for i in reversed(range(self.lfbSelectedList.count())):
            self.lfbSelectedList.itemAt(i).widget().setParent(None)

        featureList = self.vl.getFeatures()
        
        sorted_featureList = sorted(featureList, key=lambda x: x['created'], reverse=True)

        selectedFeatures = Utils.getSelectedFeaturesFim()
        
        for feature in sorted_featureList:

            isSelected = feature in selectedFeatures

            if isSelected == False:
                continue

            item = DraftItem(self.iface, feature)
            item.featureSelected.connect(self.listWidgetClicked)
            item.removeFeature.connect(self.removeFeature)

            item.setStyleSheet("QFrame#lfbItemFrame{ background-color: rgba(0,0,0,0.2);  border: 2px solid #ddd; padding: 10px 10px 0; }")

            if isSelected:
                item.setStyleSheet("QFrame#lfbItemFrame{ background-color: rgba(0,0,0,0.3); border: 2px solid #ff0; padding: 10px 10px 0; }")

            self.lfbSelectedList.addWidget(item)

            countFeatures += 1

        self.ioBtn.setExportLength(len(sorted_featureList))

        return countFeatures

    def readDrafts(self, status = False):
        """Read the layer and lists features"""

        self.vl = Utils.getLayerById()
        countFeatures = 0

        if self.vl is None:
            return

        for i in reversed(range(self.lfbDraftList.count())):
            self.lfbDraftList.itemAt(i).widget().setParent(None)

        
        featureList = self.vl.getFeatures()
        
        sorted_featureList = sorted(featureList, key=lambda x: x['created'], reverse=True)
        filtered = filter(lambda c: c['status'] == status, sorted_featureList)
        sorted_filtered_featureList = list(filtered)

        selectedFeatures = Utils.getSelectedFeaturesFim()
        
        for feature in sorted_filtered_featureList:

            item = DraftItem(self.iface, feature)
            item.featureSelected.connect(self.listWidgetClicked)
            item.removeFeature.connect(self.removeFeature)

            item.setStyleSheet("QFrame#lfbItemFrame{ background-color: rgba(0,0,0,0.1);  border: 2px solid #ddd; padding: 10px 10px 0; }")

            self.lfbDraftList.addWidget(item)

            countFeatures += 1

        self.ioBtn.setExportLength(len(sorted_featureList))

        return countFeatures 

    def readDone(self, status = False):
        """Read the layer and lists done features"""

        for i in reversed(range(self.lfbDoneList.count())):
            self.lfbDoneList.itemAt(i).widget().setParent(None)

        featureList = self.vl.getFeatures()
        countFeatures = 0
        
        sorted_featureList = sorted(featureList, key=lambda x: x['created'], reverse=True)
        filtered = filter(lambda c: c['status'] == status, sorted_featureList)
        sorted_featureList = list(filtered)
        
        for feature in sorted_featureList:
            item = DraftItem(self.iface, feature)
            item.featureSelected.connect(self.listWidgetClicked)
            item.removeFeature.connect(self.removeFeature)
            item.setStyleSheet("QFrame#lfbItemFrame{ background-color: rgba(0,0,0,0.2); border-radius: 5px; padding: 10px 10px 0; }")
            self.lfbDoneList.addWidget(item)

            countFeatures += 1

        return countFeatures

    def removeFeature(self, featureId):
        """Remove a selected feature"""

        self.vl.startEditing()
        self.vl.deleteFeature(featureId)
        self.vl.commitChanges()
        self.vl.endEditCommand()
        QgsProject.instance().write()

        self.update()
    
    def setStatus(self, newState):
        """Set the status and workflow of a feature"""

        if self.currentFeatureId is not None:
            for tFeature in self.vl.getFeatures():
                if tFeature.id() == self.currentFeatureId:
                    currentWorkflow = Utils.getFeatureAttribute(tFeature, 'workflow')
                    if currentWorkflow == 4 or currentWorkflow == 12:
                        currentWorkflow = currentWorkflow +1

                    self.vl.startEditing()
                    
                    tFeature.setAttribute('workflow', currentWorkflow)
                    tFeature.setAttribute('status', newState)

                    self.vl.updateFeature(tFeature)
                    self.vl.commitChanges()
                    self.vl.endEditCommand()


    def saveFeature(self, jsonObj):
        """Save a feature"""

        if jsonObj is None:
            return
        
        currentDateTime = QDateTime.currentDateTime()

        self.vl.startEditing()
        
        if self.currentFeatureId is not None:
            for tFeature in self.vl.getFeatures():

                if tFeature.id() == self.currentFeatureId:
                    
                    tFeature.setAttribute('modified', currentDateTime)
                    feature = tFeature
                    
        else:
            feature = QgsFeature()

            feature.setFields(self.vl.fields())
            
            feature.setAttribute('id', str(uuid.uuid4()))
            feature.setAttribute('created', currentDateTime)
            feature.setAttribute('modified', currentDateTime)
            feature.setAttribute('status', 0)
            
            self.vl.addFeature(feature)
        
        feature.setAttribute('form', json.dumps(jsonObj))

        self.vl.updateFeature(feature)

        self.vl.commitChanges()
        self.vl.endEditCommand()
        #QgsProject.instance().write()
        #self.vl.updateExtents()

        for feature in self.vl.getFeatures():
            if feature['modified'] == currentDateTime:
                self.currentFeatureId = feature.id()

        #self.update()


        



