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
import uuid
import json

from qgis.core import QgsMessageLog, QgsProject, QgsWkbTypes, QgsVectorFileWriter, QgsFeature, QgsGeometry, QgsPointXY, QgsPoint
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtCore import QDateTime

from PyQt5.uic import loadUi
from PyQt5 import QtCore

from osgeo import ogr


from ...utils.helper import Utils


UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'io_btn.ui'))


class IoBtn(QtWidgets.QWidget, UI_CLASS):

    exported = QtCore.pyqtSignal(bool)
    imported = QtCore.pyqtSignal(bool)
    importSelected = QtCore.pyqtSignal(bool)

    def __init__(self, interface):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.fieldsToBeMapped = ['los_id', 'created', 'modified', 'workflow', 'status', 'form', 'losnr']

        self.lfbExportBtn.clicked.connect(self.exportBtnClicked)
        self.lfbImportBtn.clicked.connect(self.importBtnClicked)
        self.lfbImportSelectedBtn.clicked.connect(self.importSelectedBtnClicked)

        self.exportLength = 0

        self.interface = interface

        #self.defaultJson = defaultJson

        self.lfbExportFeedback.setText('')

        self.exportOptions = QgsVectorFileWriter.SaveVectorOptions()
        self.exportOptions.driverName = 'GeoJson'
        self.exportOptions.includeZ = False
        self.exportOptions.overrideGeometryType = QgsWkbTypes.Point
        self.exportOptions.layerName = 'LFB-Regeneration-Wildlife-Impact-Monitoring'

        self.show()

    def update(self):
        selectedFeatures  = Utils.getSelectedFeatures(self.interface, 'LFB-Regeneration-Wildlife-Impact-Monitoring')

        if len(selectedFeatures) > 0:
            self.lfbImportSelectedBtn.setEnabled(True)
            self.lfbImportSelectedBtn.setText('IMPORTIERE AUSGEWÄHLTE PUNKTE')
        else:
            self.lfbImportSelectedBtn.setText('IMPORTIERE AUSGEWÄHLTE PUNKTE')
            self.lfbImportSelectedBtn.setEnabled(False)

        return selectedFeatures

    def setExportLength(self, length):
        self.exportLength = length

        if self.exportLength > 0:
            self.lfbExportBtn.setEnabled(True)
        else:
            self.lfbExportBtn.setEnabled(False)

    def setFeedback(self, feedback, error=False):

        self.lfbExportFeedback.setText(feedback)

        if error:
            self.lfbExportFeedback.setStyleSheet('color: red;')

    def importSelectedBtnClicked(self):

        currentDateTime = QDateTime.currentDateTime()

        selectedFeatures  = Utils.getSelectedFeatures(self.interface, 'LFB-Regeneration-Wildlife-Impact-Monitoring', True)
        self.update()

        layer = Utils.getLayerById()
        if not layer:
            return
        fields = layer.fields()

        layer.startEditing()


        defaultJson = Utils.loadDefaultJson()
        

        for selectedLayer in selectedFeatures:
            for feature in selectedLayer['features']:

                geom = feature.geometry()
                coordinates = geom.asPoint()

                #attrs = i.attributeMap()
                layerFields = selectedLayer['layer'].fields()
                attributes = feature.attributes()
                defaultAttributes = {
                    'los_id': str(uuid.uuid4()),
                    'created': currentDateTime,
                    'modified': currentDateTime,
                    'workflow': 4,
                    'status': False,
                    'form': json.dumps(defaultJson['properties']),
                    'losnr': ''
                }

                ## SAVE FEATURES
                qgsFeature = QgsFeature()
                qgsFeature.setFields(fields)
                geometry = QgsGeometry.fromPointXY(QgsPointXY(coordinates))
                qgsFeature.setGeometry(geometry)


                for fieldName in self.fieldsToBeMapped:
                    idx = layerFields.indexFromName(fieldName)
                    if idx >= 0 and attributes[idx]:
                        qgsFeature.setAttribute(fieldName, attributes[idx])
                    else:
                        qgsFeature.setAttribute(fieldName, defaultAttributes[fieldName])


                if hasattr(qgsFeature, 'los_id'):
                    qgsFeature.setAttribute('id', qgsFeature['los_id'])
                else:
                    qgsFeature.setAttribute('id', defaultAttributes['los_id'])
                #qgsFeature.setAttribute('created', currentDateTime)
                #qgsFeature.setAttribute('modified', currentDateTime)
                #qgsFeature.setAttribute('workflow', 4)
                #qgsFeature.setAttribute('status', False)
                #qgsFeature.setAttribute('form', json.dumps(defaultJson['properties']))


                layer.addFeature(qgsFeature)
                layer.removeSelection()

        layer.commitChanges()
        layer.endEditCommand()

        self.imported.emit(True)

    def importBtnClicked(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select File')

        if fileName:
            self.importFromFile(fileName)

    def importFromFile(self, fileName):

            with open(fileName, 'r') as f:
                data = json.load(f)
    
            if not data:
                self.setFeedback('Fehler beim Import', True)
                return
    
            if not 'features' in data:
                self.setFeedback('Fehler beim Import', True)
                return
    
            layer = Utils.getLayerById()
    
            if not layer:
                self.setFeedback('Layer nicht gefunden', True)
                return
    
            layer.startEditing()

            currentDateTime = QDateTime.currentDateTime()
    
            fields = layer.fields()

            newFeaturesCount = 0
            for feature in data['features']:
                

                qgsFeature = QgsFeature()
                qgsFeature.setFields(fields)
                geometry = QgsGeometry.fromPointXY(QgsPointXY(
                    feature['geometry']['coordinates'][0], 
                    feature['geometry']['coordinates'][1]
                ))
                qgsFeature.setGeometry(geometry)
                qgsFeature.setAttribute('created', currentDateTime)
                qgsFeature.setAttribute('modified', currentDateTime)




                for field in fields:
                    name = field.displayName()
                    if name in feature['properties']:
                        qgsFeature.setAttribute(name, feature['properties'][name])

                if 'properties' in feature:
                    if 'form' in feature['properties']:
                        qgsFeature.setAttribute('form', json.dumps(feature['properties']['form']))

                layer.addFeature(qgsFeature)
                newFeaturesCount += 1
    
            layer.commitChanges()
    
            self.setFeedback(str(newFeaturesCount) + ' Punkt(e) hinzugefügt')
    
            self.imported.emit(True)

    def exportBtnClicked(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        
        if folder:
            self.exportToFolder(folder)

    def exportToFolder(self, folder):

        currentDateTime = QDateTime.currentDateTime()
        fileName = folder + '/FIM-' + currentDateTime.toString("yyyy-M-d_hh-mm") + '.geojson'

        layer = Utils.getLayerById()

        if not layer:
            self.setFeedback('Layer nicht gefunden', True)
            return
        
        try:
            res = QgsVectorFileWriter.writeAsVectorFormatV3(
                layer,
                fileName,
                QgsProject.instance().transformContext(),
                self.exportOptions
            )
        except Exception as e:
            self.setFeedback('Fehler beim Export', True)
            return

        self.lfbExportFeedback.setText('letzte Export: ' + fileName)

        self.exported.emit(True)