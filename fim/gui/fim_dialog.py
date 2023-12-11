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
import time
import threading

from PyQt5 import QtGui, QtCore
from qgis.core import QgsMessageLog
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog, QScroller
from PyQt5.QtCore import Qt

import json
import copy


from .form.views.tabs import Tabs
from .form.vwm import VWM

from .draft.draft_selection import DraftSelection
from .setup.folder_selection import FolderSelection
#from .db_connection.db_widget import DBWidget

from .form.saveBar import SaveBar

from collections import deque
from jsonschema import Draft7Validator, exceptions

from ..utils.helper import Utils

from .. import resources

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'fim_dialog.ui'))


class FimDialog(QtWidgets.QDialog, FORM_CLASS):
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

        # QGIS interface
        self.iface = interface

        Utils.updateToC(self.update)

        self.tabsArray = []
        self.currentTab = 0

        self.inheritedErrors = {}
        self.schemaErrors = []

        self.previousGeneral  = None

        self.validationTimer = None

        #filename = os.path.realpath(os.path.join(dirname, '..', 'schema', 'default.json'))

        #with open(filename) as f:
        schema = Utils.loadDefaultJson() #json.load(f)
        self.defaultJson = schema['properties']

        self.json = copy.deepcopy(self.defaultJson)

        self.state = state

        scroll = QScroller.scroller(self.lfbHomeScreen.viewport())
        scroll.grabGesture(self.lfbHomeScreen.viewport(), QScroller.LeftMouseButtonGesture)
        
        #self.addFolderSelection()
        self.addDraft()

        #self.lfbNewEntry.clicked.connect(self.newEntry)
        self.lfbNewEntry.hide()

        
        self.lfbTabWidget.currentChanged.connect(self.tabChange)
        self.lfbTabWidget.hide()
        

        #self.lfbTabWidget.setProperty("class", "my-label-style")

        self.saveBar = SaveBar(self.iface, self.json)
        self.saveBar.saveFeature.connect(self.saveFeature)
        self.saveBar.setContentsMargins(0,0,0,0)
        self.lfbMain.addWidget(self.saveBar)

        self.saveBar.toHome.connect(self.formToDefault)
        self.saveBar.devButton.connect(self.openState)

        self.resetForm(False)
        self.setPosition(1)

        self.buildVwmForm()

    def loadSchema(self, type='vwm', version='1.0.0'):
        dirname = os.path.dirname(__file__)
        filename = os.path.realpath(os.path.join(dirname, '..', 'schema', type, version+'.json'))

        with open(filename) as f:
            schema = json.load(f)
            self.schemaType = schema['$type']
            self.schema = schema['properties']['properties']

        return self.schema

    def buildForm(self):
        self.lfbTabWidget.clear()
        self.tabsArray = []

        tabNr = 0
        for attr, value in self.schema['properties'].items():

            self.inheritedErrors[attr] = []

            tab = Tabs(self.iface, self.json[attr], self.schema['properties'][attr], attr, self.inheritedErrors[attr], self.schemaErrors)
            #tab.nextTab.connect(self.nextTab)
            #tab.inputChanged.connect(self.inputChanged)
            
            self.tabsArray.append(
                {
                    'tabNr': tabNr,
                    'setJson': tab.setJson,
                    'update_errors': tab.update_errors,
                    'attr': attr,
                    'inheritedErrors': self.inheritedErrors[attr]
                }
            )
            self.lfbTabWidget.addTab(tab, '') # value['title']

            #self.lfbTabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            tabNr += 1
        
        self.lfbTabWidget.tabBar().setCursor(QtCore.Qt.PointingHandCursor)


    def buildVwmForm(self):

        version = self.json['versions'] if 'versions' in self.json else '1.0.0'
        schema = self.loadSchema('vwm', version)

        self.vwmFormWidget = VWM(self.iface, schema)
        self.vwmFormWidget.save.connect(self.save)
        self.lfbVwmLayout.addWidget(self.vwmFormWidget)
        self.vwmFormWidget.hide()

    def updateVwmForm(self):
        self.vwmFormWidget.updateJson(self.json)
        self.vwmFormWidget.show()

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
        
        QgsMessageLog.logMessage(str('SAVE'), 'FIM')
        QgsMessageLog.logMessage(str(self.json), 'FIM')
        #self.saveDelay()
        self.save()
        
        #self.lfbVwmLayout.removeWidget(self.formWidget)
        #self.formWidget.deleteLater()
        #self.formWidget = None

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

        if tab is None:
            return

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

        for tab in self.tabsArray:
            if tab['attr'] in self.json:
                tab['setJson'](self.json[tab['attr']], setFields)
            else:
                cpy = copy.deepcopy(self.defaultJson[tab['attr']])
                tab['setJson'](cpy, setFields)

    def update_tab_errors(self, errors):
        for tab in self.tabsArray:
            tab['update_errors'](errors)

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
        return

        if attr in self.json:
            self.json[attr].update(save)
        else:
            self.json[attr] = save

        if forceUpdate:
            for tab in self.tabsArray:
                if tab['attr'] in self.json:
                    tab['setJson'](self.json[tab['attr']], True)

        self.changeState()

        
        self.validateTabs(True)
    
    def updateSaveBtn(self):
        self.saveBar.validate(self.state.state, self.schemaErrors)

    def save(self):

        QgsMessageLog.logMessage(str('SAVE'), 'FIM')
        
        self.draft.saveFeature(self.json)
        
        if self.previousGeneral == None:
            self.previousGeneral = copy.deepcopy(self.json['general'])

        if self.json['general']['spaufsucheaufnahmetruppkuerzel'] != None and self.json['general']['spaufsucheaufnahmetruppkuerzel'] != self.previousGeneral['spaufsucheaufnahmetruppkuerzel']:
            self.previousGeneral['spaufsucheaufnahmetruppkuerzel'] = self.json['general']['spaufsucheaufnahmetruppkuerzel']
        if self.json['general']['spaufsucheaufnahmetruppgnss'] != None and self.json['general']['spaufsucheaufnahmetruppgnss'] != self.previousGeneral['spaufsucheaufnahmetruppgnss']:
            self.previousGeneral['spaufsucheaufnahmetruppgnss'] = self.json['general']['spaufsucheaufnahmetruppgnss']

    def formToDefault(self, setFields = True):
        self.json = copy.deepcopy(self.defaultJson)
        self.resetForm()

    def openHome(self):
        #self.json = copy.deepcopy(self.defaultJson)
        self.changeState(False)
        self.setPosition(1)
        self.lfbTabWidget.setCurrentIndex(0)
        self.tabChange(0)

        Utils.deselectFeature()

    def setPosition(self, position):

        self.userPosition = position

        if self.userPosition == 2:
            self.lfbHeadline.hide()
            self.lfbFormWidget.show()

            self.saveBar.show()
            self.draft.hide()
            #self.folderSelection.hide()

            #self.lfbHomeBtn.setEnabled(True)
            #self.lfbHomeBtn.show()
            self.lfbHomeScreen.hide()
        else:
            self.lfbHeadline.show()
            self.lfbFormWidget.hide()
            self.saveBar.hide()
            self.draft.show()
            self.draft.update()
            #self.folderSelection.show()

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
        
        #self.folderSelection.setFolder(folderPath)


    
    def importSelected(self, id):
        self.draft.importSelected(id)


    def addDraft(self):
        self.draft = DraftSelection(self.iface)

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

        self.addPreviousGeneral(newJson)

        self.json = newJson
        

        self.changeState()


        type = self.json['types'] if 'types' in self.json else 'vwm'
        version = self.json['versions'] if 'versions' in self.json else '1.0.0'
        self.schema = self.loadSchema(type, version) 

        #self.buildForm()
        if self.schemaType == 'vwm':
            self.updateVwmForm()

        self.resetForm(True)
        self.setPosition(2)
        self.saveBar.setAttributes(feature, 'los_id')
        self.draft.resetCurrentDraft(id)

        Utils.focusFeature(self.iface, feature, True, 15000)

    def changeState(self, validate = True):        
        self.state.change_state(self.json)
       
        #self.resetForm(False)

        if validate and self.schemaErrors != None:
            self.saveBar.validate(self.state.state, self.schemaErrors)

    def openState(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(json.dumps(self.state.state))
        msgBox.exec()

    def validateTabs(self, save = False):

        if self.validationTimer != None:
            self.validationTimer.cancel()
            self.validationTimer = None

        self.validationTimer = threading.Timer(1, lambda: self._validateTabs())
        self.validationTimer.start()
    
        if save:
            self.save()

    def _validateTabs(self):
        QgsMessageLog.logMessage('validateTabs', 'FIM')
       
       
        isValidToSave = False

        v = Draft7Validator(self.schema)

        errors = sorted(v.iter_errors(self.json), key=lambda e: e.path)

        lfbErrors = self.lfbLayers(self.json)


        #self.lfbUniquePosition(self.json)
       
        
        for tab in self.tabsArray:

            attr = tab['attr']

            errorFound = False

            
            for error in errors:
                if attr in error.relative_schema_path:
                    errorFound = True
                    self.lfbTabWidget.setTabIcon(tab['tabNr'], QtGui.QIcon(':icons/red_rect.png'))
                    break

            for error in lfbErrors:
                if attr in error.relative_schema_path:
                    errorFound = True
                    self.lfbTabWidget.setTabIcon(tab['tabNr'], QtGui.QIcon(':icons/red_rect.png'))
                    break

            if not errorFound:
                self.lfbTabWidget.setTabIcon(tab['tabNr'], QtGui.QIcon(':icons/green_rect.png'))
        

        

        if self.schemaType == 'vwm':
            isValidToSave = self.VWMValidation(errors)
        else:
            isValidToSave = len(errors) == 0
        
        self.schemaErrors.clear()
        for error in errors:
            self.schemaErrors.append(error)

        for error in lfbErrors:
            self.schemaErrors.append(error)

        # Triggers errors
        self.update_tab_errors(self.schemaErrors)
        
        #self.updateSaveBtn()

        QgsMessageLog.logMessage(str(self.schemaErrors), 'FIM')

        return isValidToSave
    
    def VWMValidation(self, errors):
        accessable = []
        hasCoordinates = []

        for error in errors:
            if 'general' in error.relative_schema_path:
                accessable.append(error)

            if 'coordinates' in error.relative_schema_path:
                hasCoordinates.append(error)

        for tab in self.tabsArray:
            self.lfbTabWidget.setTabEnabled(tab['tabNr'], True)
        
        # Due to performance issues
        #isAccessable = self.lfbNotAccessable(self.json, accessable)
        #if isAccessable :
            #self.lfbCoordinates(self.json, hasCoordinates)

        return len(accessable) == 0 and len(hasCoordinates) == 0


    def lfbNotAccessable(self, json, taberrors):
        
        if json['general']['spaufsuchenichtbegehbarursacheid'] != 1 or json['general']['spaufsuchenichtwaldursacheid'] != 0 or len(taberrors) > 0:

            #for i in self.tabsArray:
            #    if i['attr'] != 'general':
            #        if i['attr'] in json:
            #            del self.json[i['attr']]

            #for tab in self.tabsArray:
            #    self.lfbTabWidget.setTabEnabled(tab['tabNr'], False)

            for i in range(1, 16):
                if self.lfbTabWidget.isTabEnabled(i):
                    self.lfbTabWidget.setTabEnabled(i, False)

            
            
            return False
        else:
            newValue = False
            for i in self.tabsArray:
                if i['attr'] not in self.json:
                    newValue = True
                    self.json[i['attr']] = copy.deepcopy(self.defaultJson[i['attr']])
                    i['setJson'](self.json[i['attr']], True)

        

        return True
    
    def lfbCoordinates(self, json, taberrors):
        
        if len(taberrors) > 0:

            for i in range(2, 16):
                if self.lfbTabWidget.isTabEnabled(i):
                    self.lfbTabWidget.setTabEnabled(i, False)
            return False
       
        return True
    
    def lfbUniquePosition(self, json):

        label_errors = []

        findunique = json['baumplot1']['baumplot1']
        QgsMessageLog.logMessage(str(findunique), 'FIM')


        return label_errors

    def lfbLayers(self, json):

        label_errors = []

        rules_type = {
            1: [ # es
                [3, 36, 9],
                [31, 36, 9]
            ],
            2: [ # zs
                [3, 2, 4, 36, 9],
                [2, 4, 31, 36, 9]
            ],
            3: [ # ms
                [3, 25, 2, 4, 31, 36, 9]
            ],
            4: [ # zsv
                [3, 2, 4, 36, 9]
            ],
            5: [ # zsu
                [3, 2, 4, 36, 9]
            ],
            6: [ # pl
                [0]
            ],
            7: [ # 3
                [3, 25, 2, 4, 36, 9],
                [3, 2, 4, 31, 36, 9]
            ]
        }
        rules_length = {
            1: {
                "min": 1,
                "max": 1
            },
            2: {
                "min": 2,
                "max": 2
            },
            3: {
                "min": 3,
                "max": 3
            },
            4: {
                "min": 3,
                "max": 3
            },
            5: {
                "min": 3,
                "max": 3
            },
            6: {
                "min": 1,
                "max": 100
            },
            7: {
                "min": 1,
                "max": 100
            }
        }


        elements = [d['schicht_id'] for d in json['t_bestockung']['t_bestockung']]
        elements_unique = list(set(elements))
        #elements_unique.sort()
        
        schicht_id = json['bestandsbeschreibung']['bestandnschichtigid']

        if rules_length.get(schicht_id) != None:
            if (len(elements_unique) < rules_length[schicht_id]['min'] or len(elements_unique) > rules_length[schicht_id]['max']):
                #label_errors.append({
                #    "message": 'Falsche Anzahl an Bestockungsschichten',
                #    "relative_schema_path": ['allOf', 3, 'then', 'properties', 't_bestockung', 'properties', 't_bestockung', 'minItems']
                #})
                label_errors.append(exceptions.ValidationError(
                    message='Falsche Anzahl an Bestockungsschichten',
                    validator='minItems',
                    validator_value=rules_length[schicht_id]['min'],
                    instance=elements_unique,
                    schema_path=['allOf', 3, 'then', 'properties', 't_bestockung', 'properties', 't_bestockung', 'minItems']
                ))
        
        isSublist = False
        if rules_type.get(schicht_id) != None:
            for i in rules_type[schicht_id]:
                if(all(x in i for x in elements)):
                    isSublist = True
                    break
                else:
                    isSublist = False
                    #label_errors.append({
                    #    "message": 'Falsche Schichtenkombination',
                    #    "relative_schema_path": ['properties','t_bestockung', 'properties','t_bestockung']
                    #})
                    label_errors.append(exceptions.ValidationError(
                        message='Falsche Schichtenkombination',
                        validator='minItems',
                        validator_value=rules_length[schicht_id]['min'],
                        instance=elements_unique,
                        schema_path=['allOf', 3, 'then', 'properties', 't_bestockung', 'properties', 't_bestockung', 'minItems']
                    ))
        
        return label_errors