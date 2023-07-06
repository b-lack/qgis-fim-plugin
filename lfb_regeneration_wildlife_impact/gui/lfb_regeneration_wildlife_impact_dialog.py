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

from .draft.draft_selection import DraftSelection
from .setup.folder_selection import FolderSelection
from .db_connection.db_widget import DBWidget

from .form.saveBar import SaveBar

from jsonschema import Draft7Validator

from ..utils.helper import Utils

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
        self.currentTab = 0

        self.inheritedErrors = {}

        self.previousGeneral  = None

        filename = os.path.realpath(os.path.join(dirname, '..', 'schema', 'default.json'))

        with open(filename) as f:
            schema = json.load(f)
            self.defaultJson = schema['properties']

        self.json = copy.deepcopy(self.defaultJson)

        self.state = state

        scroll = QScroller.scroller(self.lfbHomeScreen.viewport())
        scroll.grabGesture(self.lfbHomeScreen.viewport(), QScroller.LeftMouseButtonGesture)
 
        filename = os.path.realpath(os.path.join(dirname, '..', 'schema', 'schema_vwm.json'))

        with open(filename) as f:
            schema = json.load(f)
            self.schema = schema['properties']['properties']
        
        self.addFolderSelection()
        self.addDraft()
        #self.addDbConnection()

        #self.lfbNewEntry.clicked.connect(self.newEntry)
        self.lfbNewEntry.hide()

        self.lfbTabWidget.currentChanged.connect(self.tabChange)
        tabNr = 1
        
        for attr, value in self.schema['properties'].items():

            self.inheritedErrors[attr] = []

            tab = Tabs(self.iface, self.json[attr], self.schema['properties'][attr], attr, self.inheritedErrors[attr])
            tab.nextTab.connect(self.nextTab)
            tab.inputChanged.connect(self.inputChanged)
            #self.lfbTabWidget.addWidget(tab)
            #newTab = QWidget(myTabWidget)
            
            self.tabsArray.append(
                {
                    'tabNr': tabNr,
                    'setJson': tab.setJson,
                    'attr': attr,
                    'inheritedErrors': self.inheritedErrors[attr]
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

        self.saveBar.toHome.connect(self.formToDefault)
        self.saveBar.devButton.connect(self.openState)

        self.resetForm(False)
        self.setPosition(1)

    def nextTab(self, nextTab):
        if nextTab:
            indexToSet = min(self.currentTab + 1, len(self.tabsArray) - 1)
        else:
           indexToSet = max(self.currentTab - 1, 0)

        if self.lfbTabWidget.isTabEnabled(indexToSet):
            self.lfbTabWidget.setCurrentIndex(indexToSet)

    def update(self):
        self.draft.update()

    def saveFeature(self, json, status=False):

        self.draft.setStatus(status)
        self.openHome()
        self.draft.readDrafts()
        self.draft.readDone(True)

    def tabChange(self, index):
        
        self.currentTab = int(index)

        tab = self.lfbTabWidget.currentWidget()
        self.updateLinearButtons()

    def updateLinearButtons(self):   
        indexToSet = min(self.currentTab + 1, len(self.tabsArray) - 1)
        tab = self.lfbTabWidget.currentWidget()

        if self.currentTab < len(self.tabsArray)-1 and self.lfbTabWidget.isTabEnabled(indexToSet):
            tab.lfbTabBtnFwd.setEnabled(True)
        else:
            tab.lfbTabBtnFwd.setEnabled(False)

        indexToSet = max(self.currentTab - 1, 0)
        if self.currentTab > 0 and self.lfbTabWidget.isTabEnabled(indexToSet):
            tab.lfbTabBtnBack.setEnabled(True)
        else:
            tab.lfbTabBtnBack.setEnabled(False)

    def resetForm(self, setFields = True):

        QgsMessageLog.logMessage('resetForm', 'LFB')

        for tab in self.tabsArray:
            if tab['attr'] in self.json:
                tab['setJson'](self.json[tab['attr']], setFields)
            else:
                cpy = copy.deepcopy(self.defaultJson[tab['attr']])
                tab['setJson'](cpy, setFields)


    def newEntry(self):
        return
        self.json = copy.deepcopy(self.defaultJson)
        self.changeState(False)
        self.setPosition(2)
        self.resetForm(True)
        self.draft.resetCurrentDraft(None)
        self.lfbTabWidget.setCurrentIndex(0)
        self.tabChange(0)

    def inputChanged(self, save, attr, forceUpdate = False):
        if attr in self.json:
            self.json[attr].update(save)
        else:
            self.json[attr] = save

        if forceUpdate:
            for tab in self.tabsArray:
                if tab['attr'] in self.json:
                    tab['setJson'](self.json[tab['attr']], True)

        self.changeState()

        if self.validateTabs(True):
            self.draft.saveFeature(self.json)

            if self.previousGeneral == None:
                self.previousGeneral = copy.deepcopy(self.json['general'])

            if self.json['general']['spaufsucheaufnahmetruppkuerzel'] != self.previousGeneral['spaufsucheaufnahmetruppkuerzel']:
                self.previousGeneral['spaufsucheaufnahmetruppkuerzel'] = self.json['general']['spaufsucheaufnahmetruppkuerzel']
            if self.json['general']['spaufsucheaufnahmetruppgnss'] != self.previousGeneral['spaufsucheaufnahmetruppgnss']:
                self.previousGeneral['spaufsucheaufnahmetruppgnss'] = self.json['general']['spaufsucheaufnahmetruppgnss']
            
    def formToDefault(self, setFields = True):
        self.json = copy.deepcopy(self.defaultJson)
        self.resetForm()

    def openHome(self):
        self.json = copy.deepcopy(self.defaultJson)
        self.changeState(False)
        self.setPosition(1)
        self.lfbTabWidget.setCurrentIndex(0)
        self.tabChange(0)

        Utils.deselectFeature()

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
            self.draft.update()
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

    #def imported(self):
    #    self.draft.readDrafts()
    #    self.draft.readDone(True)
    
    def importSelected(self, id):
        self.draft.importSelected(id)


    def addDraft(self):
        self.draft = DraftSelection(self.iface, self.schema)

        try:
            self.draft.draftSelected.disconnect()
            self.draft.folderSelected.disconnect()
        except:
            pass

        self.draft.draftSelected.connect(self.draftSelected)
        self.draft.folderSelected.connect(self.folderSelected)
        self.lfbHomeInputs.addWidget(self.draft)

        self.draft.setupDraftLayer()

    def addPreviousGeneral(self, newJson):
        if 'general' in newJson and self.previousGeneral != None:
            if 'spaufsucheaufnahmetruppkuerzel' in self.previousGeneral and newJson['general']['spaufsucheaufnahmetruppkuerzel'] == None:
                newJson['general']['spaufsucheaufnahmetruppkuerzel'] = self.previousGeneral['spaufsucheaufnahmetruppkuerzel']
            if 'spaufsucheaufnahmetruppgnss' in self.previousGeneral and newJson['general']['spaufsucheaufnahmetruppgnss'] == None:
                newJson['general']['spaufsucheaufnahmetruppgnss'] = self.previousGeneral['spaufsucheaufnahmetruppgnss']

    
    def draftSelected(self, newJson, id, feature):
        self.json = copy.deepcopy(self.defaultJson)

        self.addPreviousGeneral(newJson)

        self.json = newJson
        self.changeState()
        QgsMessageLog.logMessage('draftSelected', 'LFB')
        self.resetForm(True)
        self.setPosition(2)
        self.saveBar.setAttributes(feature, 'los_id')
        self.draft.resetCurrentDraft(id)

        Utils.focusFeature(self.iface, feature, True, 15000)

    def changeState(self, validate = True):        
        self.state.change_state(self.json)
       
        QgsMessageLog.logMessage('changeState', 'LFB')
        self.resetForm(False)

        if validate:
            self.validateTabs()
            self.saveBar.validate(self.state.state)

    def openState(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(json.dumps(self.state.state))
        msgBox.exec()

    def validateTabs(self, minimumToDraft = False):

        tabNr = 0

        for tab in self.tabsArray:

            attr = tab['attr']            

            if attr in self.json:
                v = Draft7Validator(self.schema['properties'][attr])
                errors = sorted(v.iter_errors(self.json[attr]), key=lambda e: e.path)
            else:
                errors = [{'message': 'No data available'}]


            if len(errors) == 0 and len(tab['inheritedErrors']) == 0:
                self.lfbTabWidget.setTabText(tabNr, '')
                self.lfbTabWidget.setTabIcon(tabNr, QtGui.QIcon(':icons/green_rect.png'))
            else:
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


        #self.lfbTabWidget.setTabEnabled(0, True)
        for i in range(0, 16):
            self.lfbTabWidget.setTabEnabled(i, True)

        self.lfbNotAccessable(self.json, gErrors)
        self.lfbCoordinates(self.json, cErrors)

        
        self.updateLinearButtons()
        return len(gErrors) == 0

    def lfbNotAccessable(self, json, taberrors):

        if json['general']['spaufsuchenichtbegehbarursacheid'] != 1 or json['general']['spaufsuchenichtwaldursacheid'] != 0 or len(taberrors) > 0:

            for i in self.tabsArray:
                if i['attr'] != 'general':
                    if i['attr'] in json:
                        del self.json[i['attr']]

            for i in range(1, 16):
                self.lfbTabWidget.setTabEnabled(i, False)
            
            
            return False
        else:
            newValue = False
            for i in self.tabsArray:
                if i['attr'] not in self.json:
                    newValue = True
                    self.json[i['attr']] = copy.deepcopy(self.defaultJson[i['attr']])
                    i['setJson'](self.json[i['attr']], True)

            if newValue:
                self.resetForm(True)

        return True
    
    def lfbCoordinates(self, json, taberrors):
        if len(taberrors) > 0:
            for i in range(2, 16):
                self.lfbTabWidget.setTabEnabled(i, False)
            return False
        return True