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

from PyQt5 import QtGui, QtCore
from qgis.core import QgsMessageLog
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog, QScroller
from PyQt5.QtCore import Qt

import json
import copy


from .form.views.tabs import Tabs

from .draft.export_btn import ExportButton
from .draft.draft_selection import DraftSelection
from .setup.folder_selection import FolderSelection
from .db_connection.db_widget import DBWidget

from .form.saveBar import SaveBar

from jsonschema import Draft7Validator

from .. import resources

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'lfb_regeneration_wildlife_impact_dialog_base.ui'))


class LfbRegenerationWildlifeImpactDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, interface, state):
        """Constructor.

        :type state: CurrentState
        """

        # super(LfbRegenerationWildlifeImpactDialog, self).__init__(parent)
        QDialog.__init__(self, interface.mainWindow())

        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        dirname = os.path.dirname(__file__)

        # QGIS interface
        self.iface = interface

        self.tabsArray = []
        self.currentTab = None

        filename = os.path.realpath(os.path.join(dirname, '..', 'schema', 'default.json'))

        with open(filename) as f:
            self.defaultJson = json.load(f)

        self.json = copy.deepcopy(self.defaultJson)

        self.state = state

        qss = os.path.realpath(os.path.join(dirname, '..', 'styles', 'global.qss'))
        
        #with open(qss,"r") as fh:
            #self.setStyleSheet(fh.read())
            
            #self.setStyleSheet("QLineEdit { background-color: yellow }")


        #self.lfbDevBtn.clicked.connect(self.openState)

        #self.lfbHomeScreen
        #self.lfbHomeScreen.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.lfbHomeScreen.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        scroll = QScroller.scroller(self.lfbHomeScreen.viewport())
        scroll.grabGesture(self.lfbHomeScreen.viewport(), QScroller.LeftMouseButtonGesture)
 
        filename = os.path.realpath(os.path.join(dirname, '..', 'schema', 'schema_vwm.json'))

        with open(filename) as f:
            self.schema = json.load(f)
        
        self.addFolderSelection()
        self.addDraft()
        self.addExportButton()
        #self.addDbConnection()

        self.lfbNewEntry.clicked.connect(self.newEntry)

        self.lfbTabWidget.currentChanged.connect(self.tabChange)
        tabNr = 1
        for attr, value in self.schema['properties'].items():
            QgsMessageLog.logMessage(attr, 'LFB')
            tab = Tabs(self.iface, self.json[attr], self.schema['properties'][attr])
            tab.inputChanged.connect(self.inputChanged)
            #self.lfbTabWidget.addWidget(tab)
            #newTab = QWidget(myTabWidget)
            
            self.tabsArray.append(
                {
                    'tabNr': tabNr,
                    'setJson': tab.setJson,
                    'attr': attr
                }
            )
            self.lfbTabWidget.addTab(tab, '') # value['title']

            #self.lfbTabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            tabNr += 1
        
        self.lfbTabWidget.tabBar().setCursor(QtCore.Qt.PointingHandCursor)

        #self.lfbTabWidget.setProperty("class", "my-label-style")

        self.saveBar = SaveBar(self.iface, self.json, self.schema)
        self.saveBar.saveFeature.connect(self.saveFeature)
        self.saveBar.setContentsMargins(0,0,0,0)
        self.lfbMain.addWidget(self.saveBar)

        self.saveBar.toHome.connect(self.openHome)
        self.saveBar.devButton.connect(self.openState)

        self.resetForm(False)
        self.setPosition(1)

    def saveFeature(self, json):
        self.draft.setStatus(True)
        self.openHome()
        self.draft.readDrafts()
        self.draft.readDone(True)

    def tabChange(self, index):
        self.currentTab = index

        #if self.currentTab == None:
        #    self.lfbTitle.setText('LFB Regeneration and Wildlife Impact Monitoring')
        #else:
        #    self.lfbTitle.setText(self.schema['properties'][self.tabsArray[index]['attr']]['title'])

    def resetForm(self, setFields = True):
        for tab in self.tabsArray:
            if tab['attr'] in self.json:
                tab['setJson'](self.json[tab['attr']], setFields)
            else:
                tab['setJson'](self.defaultJson[tab['attr']], setFields)


    def newEntry(self):
        self.json = copy.deepcopy(self.defaultJson)
        self.changeState(False)
        self.setPosition(2)
        self.resetForm(True)
        self.draft.resetCurrentDraft(None)
        self.lfbTabWidget.setCurrentIndex(0)
        self.tabChange(0)

    def inputChanged(self, save):
        
        self.changeState()

        #if self.saveBar.validate(self.json) == True:
        if self.validateTabs(True):
            self.draft.saveFeature(self.json)
        # if self.json['coordinates']['latitude'] != None and self.json['coordinates']['longitude'] != None and self.json['aufnahmetrupp'] != None and self.json['GNSSDevice'] != None:
            

    def openHome(self):
        self.json = copy.deepcopy(self.defaultJson)
        self.changeState(False)
        self.setPosition(1)
        self.lfbTabWidget.setCurrentIndex(0)
        self.tabChange(None)


    def setPosition(self, position):

        self.userPosition = position

        if self.userPosition == 2:
            self.lfbHeadline.hide()
            self.lfbTabWidget.show()
            self.saveBar.show()
            self.draft.hide()
            self.folderSelection.hide()
            #self.lfbHomeBtn.setEnabled(True)
            #self.lfbHomeBtn.show()
            self.lfbHomeScreen.hide()
        else:
            self.lfbHeadline.show()
            self.lfbTabWidget.hide()
            self.saveBar.hide()
            self.draft.show()
            self.folderSelection.show()
            #self.lfbHomeBtn.setEnabled(False)
            #self.lfbHomeBtn.hide()
            self.lfbHomeScreen.show()

    def addFolderSelection(self):
        self.folderSelection = FolderSelection(self.iface)
        self.folderSelection.folderSelected.connect(self.folderSelected)
        self.lfbHomeInputs.addWidget(self.folderSelection)

    def folderSelected(self, folderPath):
        self.draftPath = folderPath
        self.draft.setDraftPath(folderPath)
        #self.folderSelection.hide()
        
        self.folderSelection.setFolder(folderPath)

    def addDbConnection(self):
        dbWidget = DBWidget(self.iface)
        #self.lfbMain.addWidget(dbWidget)

    def imported(self):
        self.draft.readDrafts()
        self.draft.readDone(True)
    
    def importSelected(self, id):
        self.draft.importSelected(id)

    def addExportButton(self):
        exportButton = ExportButton(self.iface, self.defaultJson, self.schema)
        exportButton.imported.connect(self.imported)
        #exportButton.importSelected.connect(self.draft.importSelected)
        self.lfbHomeInputs.addWidget(exportButton)

    def addDraft(self):
        self.draft = DraftSelection(self.iface, self.schema)
        self.draft.draftSelected.connect(self.draftSelected)
        self.draft.folderSelected.connect(self.folderSelected)
        self.lfbHomeInputs.addWidget(self.draft)

        self.draft.setupDraftLayer()
    
    def draftSelected(self, newJson, id):
        self.json = newJson
        self.resetForm(True)
        self.changeState()
        self.setPosition(2)
        self.draft.resetCurrentDraft(id)

    def changeState(self, validate = True):        
        self.state.change_state(self.json)
        self.saveBar.validate(self.state.state)
        
        self.resetForm(False)

        if validate:
            self.validateTabs()

    def openState(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(json.dumps(self.state.state))
        msgBox.exec()

    def validateTabs(self, minimumToDraft = False):

        tabNr = 0
        for attr, value in self.schema['properties'].items():

            

            if attr in self.json:
                v = Draft7Validator(value)

                errors = sorted(v.iter_errors(self.json[attr]), key=lambda e: e.path)
            else:
                errors = ['missing']

            if tabNr == 0:
                for error in errors:
                    QgsMessageLog.logMessage(str(error.message), 'LFB')
                

            if len(errors) == 0:
                self.lfbTabWidget.setTabEnabled(tabNr, True)
                self.lfbTabWidget.setTabText(tabNr, '')

                self.lfbTabWidget.setTabIcon(tabNr, QtGui.QIcon(':icons/green_rect.png'))
            else:
                #if tabNr != 0:
                    #self.lfbTabWidget.setTabEnabled(tabNr, False)
                self.lfbTabWidget.setTabIcon(tabNr, QtGui.QIcon(':icons/red_rect.png'))
                self.lfbTabWidget.setTabText(tabNr, '')

            if tabNr == 0:
                gErrors = errors
            elif tabNr == 1:
                cErrors = errors
            elif tabNr == 2:
                tErrors = errors

            tabNr += 1

        enableAll = len(gErrors) == 0 and len(cErrors) == 0 and len(tErrors) == 0

        for i in range(3, 14):
            if enableAll:
                self.lfbTabWidget.setTabEnabled(i, True)
            else:
                self.lfbTabWidget.setTabEnabled(i, True) #False

        
        return enableAll


