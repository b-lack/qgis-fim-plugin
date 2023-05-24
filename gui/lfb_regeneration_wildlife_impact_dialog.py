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

from qgis.core import QgsMessageLog, QgsProject, QgsVectorLayer, QgsMapLayer
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import QCoreApplication, QSettings, QTranslator
from qgis.PyQt.QtWidgets import QDialog

from PyQt5.uic import loadUi



# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'lfb_regeneration_wildlife_impact_dialog_base.ui'))


class LfbRegenerationWildlifeImpactDialog(QtWidgets.QDialog, FORM_CLASS):
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

        # QGIS interface
        self.iface = interface

        # Connect up the buttons.
        self.lfbQuestionBtn.clicked.connect(self.openQuestionDialog)

        self.tabWidget.hide()
        
        # ONLY ONCE
        self.checkIfPrivateLayerExists()

        ui = loadUi("setupLayer.ui", self)


    # Move to seperate helper class
    def checkIfPrivateLayerExists(self):
        """Check if private layer exists"""
        QgsMessageLog.logMessage('checkIfPrivateLayerExists', "LFB")

        names = [layer.name() for layer in QgsProject.instance().mapLayers().values()]

        path_absolute = QgsProject.instance().readPath("./")
        #QgsMessageLog.logMessage('' + unicode(path_absolute), "LFB")

 # https://anitagraser.com/pyqgis-101-introduction-to-qgis-python-programming-for-non-programmers/pyqgis101-creating-editing-a-new-vector-layer/
        # add Vector Layer
        vl = QgsVectorLayer("Point", "temp", "memory")
        vl.setFlags(QgsMapLayer.Private)
        QgsProject.instance().addMapLayer(vl)

        #self.iface.addVectorLayer('/Users/b-mac/sites/lfb/raw/by_python/natural_earth_vector.gpkg|layername=foo', '', 'ogr')

        QgsMessageLog.logMessage('layer', "LFB")



    def openQuestionDialog(self):
        msg = self.tr('Infotext')

        QtWidgets.QMessageBox.information(
            self, "LFB Info", msg, QtWidgets.QMessageBox.Ok)
