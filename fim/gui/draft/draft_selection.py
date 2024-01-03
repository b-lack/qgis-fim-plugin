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
import datetime
import uuid


from qgis.core import QgsFeature, QgsExpressionContextUtils, QgsSimpleMarkerSymbolLayer, QgsPalLayerSettings, QgsTextFormat, QgsTextBufferSettings, QgsVectorLayerSimpleLabeling, QgsMessageLog, QgsProject, QgsVectorLayer, QgsSymbol, QgsRendererRange, QgsGraduatedSymbolRenderer, QgsMarkerSymbol, QgsJsonUtils, QgsMapLayer, QgsField, QgsFields, QgsVectorFileWriter, QgsCoordinateTransformContext
from qgis.PyQt import QtWidgets, uic, QtGui
from qgis.PyQt.QtCore import QDateTime, QVariant, QCoreApplication, QSettings, QTranslator
from PyQt5.QtGui import QColor, QFont

from qgis.PyQt.QtWidgets import QDialog, QTableWidgetItem, QScroller

from PyQt5.uic import loadUi
from PyQt5 import QtCore

from .io_btn import IoBtn
from .draft_item import DraftItem
from ...utils.helper import Utils

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'draft_selection.ui'))


class DraftSelection(QtWidgets.QWidget, UI_CLASS):
    # https://forum.qt.io/topic/133959/example-of-calling-a-function-to-parent/6
    draftSelected = QtCore.pyqtSignal(object, int, object)
    folderSelected = QtCore.pyqtSignal(str)

    def __init__(self, interface):
        """Constructor."""

        # super(LfbRegenerationWildlifeImpactDialog, self).__init__(parent)
        QDialog.__init__(self, interface.mainWindow())

        

        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.LAYER_PREFIX = Utils.getLayerName()
        self.LAYER_VERSION = Utils.getLayerVersion()

        # QGIS interface
        self.iface = interface

        self.vl = None

        self.fields = QgsFields()
        #self.fields.append(QgsField("fid", QVariant.DateTime))
        self.fields.append(QgsField("id", QVariant.String))
        self.fields.append(QgsField("los_id", QVariant.String))
        self.fields.append(QgsField("status", QVariant.Bool))

        self.fields.append(QgsField("type", QVariant.String))
        self.fields.append(QgsField("version", QVariant.String))
        #self.fields.append(QgsField("geometry", QVariant.Map))
        
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

        self.show()

    def update(self):
        """Update the feature lists"""

        visibleFeatures = 0
        if self.vl is not None:
            draftCount = self.readDrafts()
            visibleFeatures += draftCount
            self.tabWidget.setTabText(1, 'Entwürfe (' + str(draftCount) + ')')
            
            
            selectedCount = self.readSelected()
            visibleFeatures += selectedCount
            self.tabWidget.setTabText(0, 'Ausgewählt (' + str(selectedCount) + ')')

            doneCount = self.readDone(True)
            visibleFeatures += doneCount
            self.tabWidget.setTabText(2, 'Abgeschlossen (' + str(doneCount) + ')')
            
            self.ioBtn.update()

        if visibleFeatures == 0:
            self.empty_draft_label.show()
        else:
            self.empty_draft_label.hide()

    def imported(self, path):
        self.update()
        self.tabWidget.setCurrentIndex(1)

    def addIoButton(self):
        self.ioBtn = IoBtn(self.iface)
        self.ioBtn.imported.connect(self.imported)
        #exportButton.importSelected.connect(self.draft.importSelected)
        self.lfbIoWidget.addWidget(self.ioBtn)

    def addLists(self):
        columnCount = 2

        tableHeaders = ['Name', 'Unterlos']
        self.lfbDraftTableView.setColumnCount(columnCount)
        self.lfbDraftTableView.setHorizontalHeaderLabels(tableHeaders)
        self.lfbDraftTableView.horizontalHeader().setStretchLastSection(True)

        self.addListRows()

    def addListRows(self):
        properties = self.readLayer()

        self.lfbDraftTableView.clear()
        self.lfbDraftTableView.setRowCount(len(properties))

        for rowNr, id in enumerate(properties):
            idx = 0
            
            for columnNr, column in id.items():
                self.lfbDraftTableView.setItem(rowNr, idx, QTableWidgetItem(str(id[columnNr])))
                idx += 1

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
            #self.readDrafts(False)
            #self.readSelected()
            #self.readDone(True)
            return

        #names = [layer for layer in QgsProject.instance().mapLayers().values()]

        #for i in names:
        #    if QgsExpressionContextUtils.layerScope(i).variable('LFB-NAME') == self.LAYER_PREFIX :
                
        #        eslf.vl = i

        #        folder = os.path.dirname(self.vl.dataProvider().dataSourceUri())
        #        self.folderSelected.emit(str(folder))

        #        self.readDrafts(False)
        #        self.readDone(True)
        #        return

        # https://anitagraser.com/pyqgis-101-introduction-to-qgis-python-programming-for-non-programmers/pyqgis101-creating-editing-a-new-vector-layer/
        self.vl = QgsVectorLayer("Point", self.LAYER_PREFIX + '-' + self.LAYER_VERSION, "memory")
        self.vl.setName(self.LAYER_PREFIX)
        QgsExpressionContextUtils.setLayerVariable(self.vl, 'LFB-NAME', self.LAYER_PREFIX)
        QgsExpressionContextUtils.setLayerVariable(self.vl, 'LFB-VERSION', self.LAYER_VERSION)

        #self.vl.setFlags(QgsMapLayer.Private)
        
        self.setupSymbols()

        pr = self.vl.dataProvider()

        # add fields
        pr.addAttributes(self.fields)
        self.vl.updateFields() # tell the vector layer to fetch changes from the provider

        QgsProject.instance().addMapLayer(self.vl)
    
        
    def setDraftPath(self, path):
        pathToBeSet = os.path.join(path, self.LAYER_PREFIX + '.gpkg')
        writer = QgsVectorFileWriter.writeAsVectorFormatV3(self.vl, pathToBeSet, QgsCoordinateTransformContext(), QgsVectorFileWriter.SaveVectorOptions())

        if writer[0] == QgsVectorFileWriter.NoError:
            self.vl.setDataSource(pathToBeSet, self.vl.name(), 'ogr')
            self.vl.triggerRepaint() 
        else:
            print("error")

    
    def listWidgetClicked(self, item):
        featureList = self.vl.getFeatures()
        for feat in featureList:
            
            if(feat.id() == item):
                json_object = json.loads(feat['form'])
                self.currentFeatureId = feat.id()
                self.draftSelected.emit(json_object, self.currentFeatureId, feat)
                break
    
    def setupSymbols2(self):
        symbol = QgsMarkerSymbol.createSimple(
            {'name': 'circle', 'color': 'grey'})

        # Delete first default symbollayer:
        symbol.deleteSymbolLayer(0)

        # Create and insert multiple symbollayers (Example):
        colors = ['red', 'green', 'blue']
        for i, color in enumerate(colors):
            new_symbollayer = QgsSimpleMarkerSymbolLayer()
            new_symbollayer.setSize(40 - i*10)
            new_symbollayer.setFillColor(QColor(color))
            # See QgsSimpleMarkerSymbolLayer for more parameters...

            # Add symbollayer to the symbol:
            symbol.appendSymbolLayer(new_symbollayer)
        self.vl.renderer().setSymbol(symbol)

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
        # create a category for each item in values
        #ranges = []
        #for label, lower, upper, color in values:
        #    symbol = QgsSymbol.defaultSymbol(self.vl.geometryType())
        #    symbol.setColor(QColor(color))
        #    rng = QgsRendererRange(lower, upper, symbol, label)
        #    ranges.append(rng)

        # create the renderer and assign it to a layer
        #expression = 'workflow' # field name
        #renderer = QgsGraduatedSymbolRenderer(expression, ranges)
        #self.vl.setRenderer(renderer)
        #self.addLabel(self.vl)
        
        dirname = os.path.dirname(__file__)
        filename = os.path.realpath(os.path.join(dirname, '../..', 'layerstyles', 'express_2.qml'))

        self.vl.loadNamedStyle(filename)

        

        self.vl.triggerRepaint()

    def addLabel(self, layer):
        layer_settings  = QgsPalLayerSettings()
        text_format = QgsTextFormat()

        #text_format.setFont(QFont("Arial", 12))
        text_format.setSize(12)

        buffer_settings = QgsTextBufferSettings()
        buffer_settings.setEnabled(True)
        buffer_settings.setSize(0.10)
        buffer_settings.setColor(QColor("black"))

        text_format.setBuffer(buffer_settings)
        layer_settings.setFormat(text_format)

        layer_settings.fieldName = "los_id"
        #layer_settings.placement = 4

        layer_settings.enabled = True

        layer_settings = QgsVectorLayerSimpleLabeling(layer_settings)
        layer.setLabelsEnabled(True)
        layer.setLabeling(layer_settings)
        

    def readLayer(self):
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
        #filtered = filter(lambda c: c['status'] == status, sorted_featureList)
        #sorted_filtered_featureList = list(filtered)

        selectedFeatures = Utils.getSelectedFeaturesFim()
        
        for feature in sorted_featureList:

            isSelected = feature in selectedFeatures
            #if feature in selectedFeatures:
            #    selected = True

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

            selected = False
            if feature in selectedFeatures:
                selected = True

            item = DraftItem(self.iface, feature)
            item.featureSelected.connect(self.listWidgetClicked)
            item.removeFeature.connect(self.removeFeature)

            item.setStyleSheet("QFrame#lfbItemFrame{ background-color: rgba(0,0,0,0.1);  border: 2px solid #ddd; padding: 10px 10px 0; }")

            #if selected:
            #    item.setStyleSheet("QFrame#lfbItemFrame{ background-color: rgba(0,0,0,0.3); border: 2px solid #ff0; border-radius: 5px; padding: 10px 10px 0; }")

            self.lfbDraftList.addWidget(item)

            countFeatures += 1

        self.ioBtn.setExportLength(len(sorted_featureList))

        return countFeatures 

    def readDone(self, status = False):

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
        self.vl.startEditing()
        self.vl.deleteFeature(featureId)
        self.vl.commitChanges()
        self.vl.endEditCommand()
        QgsProject.instance().write()

        self.update()
        #self.readDrafts(False)
        #self.readSelected()
        #self.readDone(True)
    
    def setStatus(self, newState):
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

        if jsonObj is None:
            return
        
        currentDateTime = QDateTime.currentDateTime()

        self.vl.startEditing()

        # check if feature exists
        if self.currentFeatureId is not None:

            for tFeature in self.vl.getFeatures():

                if tFeature.id() == self.currentFeatureId:
                    
                    tFeature.setAttribute('modified', currentDateTime)
                    feature = tFeature
                    #geometry = QgsGeometry.fromPointXY(QgsPointXY(x, y))
                    #feature.setGeometry(geometry)
                    
        else:
            feature = QgsFeature()

            # inform the feature of its fields
            feature.setFields(self.vl.fields())

            #geometry = QgsGeometry.fromPointXY(QgsPointXY(x, y))
            #feature.setGeometry(geometry)

            #for attr, value in jsonObj.items():
            #    feature.setAttribute(attr, value)
            
            feature.setAttribute('id', str(uuid.uuid4()))
            feature.setAttribute('created', currentDateTime)
            feature.setAttribute('modified', currentDateTime)
            feature.setAttribute('status', 0)
            
            self.vl.addFeature(feature)
                
        # SET META DATA
        #feature.setAttribute('workflow', jsonObj['general']['workflow'])
        feature.setAttribute('form', json.dumps(jsonObj))

        self.vl.updateFeature(feature)

        self.vl.commitChanges()
        self.vl.endEditCommand()
        QgsProject.instance().write()
        self.vl.updateExtents()

        for feature in self.vl.getFeatures():
            if feature['modified'] == currentDateTime:
                self.currentFeatureId = feature.id()

        self.update()
        #self.readDrafts(False)
        #self.readDone(True)
        #self.readSelected()


        



