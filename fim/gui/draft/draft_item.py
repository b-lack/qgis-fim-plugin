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

from qgis.core import QgsMessageLog, QgsPointXY
from qgis.PyQt import QtWidgets, uic, QtGui
from qgis.PyQt.QtWidgets import QDialog, QMessageBox

from PyQt5.uic import loadUi
from PyQt5 import QtCore

from ...utils.helper import Utils


UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'draft_item.ui'))


class DraftItem(QtWidgets.QWidget, UI_CLASS):
    """Implementation of the DraftItem widget."""

    featureSelected = QtCore.pyqtSignal(int)
    removeFeature = QtCore.pyqtSignal(int)

    def __init__(self, interface, feature):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())

        self.setupUi(self)

        self.interface = interface
        self.feature = feature
        self.properties = json.loads(feature['form'])

        self.lfbDraftIconBtn.clicked.disconnect()
        self.lfbDraftIconBtn.clicked.connect(self.on_lfbDraftIconBtn_clicked)

        self.lfbDraftIconRemoveBtn.clicked.disconnect()
        self.lfbDraftIconRemoveBtn.clicked.connect(self.on_lfbDraftIconRemoveBtn_clicked)

        self.lfbFocusBtn.clicked.connect(self.focusFeature)

        self.lfbDraftModifiedByBtn.setText(feature['modified'].toString() if feature['modified'] else '-')
        self.lfbDraftModifiedBtn.setText(feature['created'].toString() if feature['created'] else '-')

        if 'general' in self.properties:
            self.lfbDraftAufnahmetruppLabel.setText(self.properties['general']['spaufsucheaufnahmetruppkuerzel'] if self.properties['general']['spaufsucheaufnahmetruppkuerzel'] is not None else '-')
            self.lfbDraftAufnahmegeraetLabel.setText(self.properties['general']['spaufsucheaufnahmetruppgnss'] if self.properties['general']['spaufsucheaufnahmetruppgnss'] is not None else '-')

        self.lfbItemTypeLabel.setText(self.typeMap(type))

        losId = feature['id']
        if feature['los_id'] is not None:
            losId =feature['los_id']

        self.lfbItemIdLabel.setText(losId)

        self.show()
    
    def typeMap(self, type):
        """Map the type to a human readable string."""

        if(type == 'wze'):
            return 'WZE' # - Waldzustandserhebung
        
        return 'VWM' # - Verjüngungs- und Wildeinflussmonitoring

    def focusFeature(self):
        """Focus the feature in the map canvas."""
        Utils.focusFeature(self.interface, self.feature, False, None)

    def on_lfbDraftIconBtn_clicked(self):
        """Emit the featureSelected signal."""
        self.featureSelected.emit(self.feature.id())
    
    def on_lfbDraftIconRemoveBtn_clicked(self):
        """Remove the feature from the layer."""

        msgBox = QMessageBox()
        msgBox.setText("Möchtest du den Stichprobenpunkt einschließlich der aufgenommenen Daten wirklich löschen?")
        msgBox.setWindowTitle("Stichprobenpunkt löschen")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.removeFeature.emit(self.feature.id())

        
 