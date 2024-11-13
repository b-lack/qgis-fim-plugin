# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FindLocationDockWidget
                                 A QGIS plugin
 Navigate to location
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-30
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Torsten Wiebke, Gerrit Balindt
        email                : support@gruenecho.de
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
import copy
from jsonschema import Draft7Validator

from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtCore import pyqtSignal
from qgis.PyQt.QtWidgets import QScroller
from qgis.core import QgsMessageLog, QgsProject
from PyQt5.QtCore import QTimer

from .form.vwm import VWM
from .draft.draft_selection import DraftSelection
from .form.saveBar import SaveBar
from .form.views.tabs import Tabs
from ..utils.helper import Utils

from .unterlosnr_dialog import UnterlosnrDialog


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'fim_dockwidget_base.ui'))

class FimDockWidget(QtWidgets.QDockWidget, FORM_CLASS):
    """
    DockWidget class. 
    """

    closingPlugin = pyqtSignal()

    def __init__(self, interface, parent=None):
        """Constructor."""

        QtWidgets.QDockWidget.__init__(self, interface.mainWindow())

        self.setupUi(self)
        
        # QGIS interface
        self.iface = interface

        

        self.tabsArray = []
        self.currentTab = 0
        self.inheritedErrors = {}
        self.schemaErrors = []
        self.saveTimer = None

        self.userPosition = 0

        self.previousGeneral  = None

        schema = Utils.loadDefaultJson()
        self.json = schema['properties']

        scroll = QScroller.scroller(self.lfbHomeScreen.viewport())
        scroll.grabGesture(self.lfbHomeScreen.viewport(), QScroller.LeftMouseButtonGesture)
        
        self.lfbTabWidget.hide()

        # SAVE BAR
        self.saveBar = SaveBar(self.iface, self.json)
        self.saveBar.saveFeature.connect(self.saveFeature)
        self.saveBar.setContentsMargins(0,0,0,0)
        self.lfbMain.addWidget(self.saveBar)

        
        # Change TABS
        self.form_previous_btn.clicked.connect(lambda: self.moveTab(-1))
        self.form_next_btn.clicked.connect(lambda: self.moveTab(1))

        # Toggle INFO Dialog
        self.info_btn.clicked.connect(self.toggle_info_dialog)
        self.info_browser.hide()

        self.addDraft()
        self.buildVwmForm()
        self.setPosition(1)

        self.create_FIM_layer_widget.hide()
        self.create_fim_layer_btn.clicked.connect(self.create_new_FIM_layer)

        QgsProject.instance().layerWasAdded.connect(self.update_toc)
        QgsProject.instance().layerRemoved.connect(self.check_fim_layer_exists)
        self.update_toc()

    def check_fim_layer_exists(self):
        """Check if the FIM layer was removed"""

        if not Utils.getLayerById():
            self.setPosition(0)
        elif self.userPosition == 0:
            self.setPosition(1)

        

    def update_toc(self):
        """Update the TOC"""

        Utils.updateToC(self.update)
        self.check_fim_layer_exists()

    def toggle_info_dialog(self):
        '''Toggle the info dialog on press info Btn'''

        self.info_browser.setVisible(not self.info_browser.isVisible())

    def loadSchema(self, type='vwm', version='1.0.0'):
        """Load the schema from file"""

        dirname = os.path.dirname(__file__)
        filename = os.path.realpath(os.path.join(dirname, '..', 'schema', type, version+'.json'))

        with open(filename) as f:
            schema = json.load(f)
            self.schemaType = schema['$type']
            self.schema = schema['properties']['properties']

        return self.schema

    def buildDynamicForm(self):
        """Build the dynamic form from schema"""

        self.lfbTabWidget.clear()
        self.tabsArray = []

        tabNr = 0
        for attr, value in self.schema['properties'].items():

            self.inheritedErrors[attr] = []

            tab = Tabs(self.iface, self.json[attr], self.schema['properties'][attr], attr, self.inheritedErrors[attr], self.schemaErrors)
            
            self.tabsArray.append(
                {
                    'tabNr': tabNr,
                    'setJson': tab.setJson,
                    'update_errors': tab.update_errors,
                    'attr': attr,
                    'inheritedErrors': self.inheritedErrors[attr]
                }
            )
            self.lfbTabWidget.addTab(tab, '') 

            tabNr += 1
        
        self.lfbTabWidget.tabBar().setCursor(QtCore.Qt.PointingHandCursor)



    # Build the VWM schema form
    def buildVwmForm(self):
        """Build the static VWM form"""

        version = self.json['versions'] if 'versions' in self.json else '1.0.0'
        schema = self.loadSchema('vwm', version)

        self.vwmFormWidget = VWM(self.iface, schema, self.info_browser)
        self.vwmFormWidget.save_data.connect(self.updateSaveBtn)
        self.vwmFormWidget.save.connect(self.save_json)
        self.lfbVwmLayout.addWidget(self.vwmFormWidget)
        self.vwmFormWidget.hide()

    def updateVwmForm(self):
        self.vwmFormWidget.updateJson(self.json)        
        self.vwmFormWidget.show()

    #def updateSelectionList(self):
    #    """Update the selection"""
#
    #    self.draft.update()
#
    def moveTab(self, direction = 1):
        if not hasattr(self, 'vwmFormWidget'):
            return
        
        if direction == -1:
            self.vwmFormWidget.previousTab()
        else:
            self.vwmFormWidget.nextTab()

    # deprecated
    #def update(self):
    #    '''Update feature list on select/deselect feature'''
#
    #    #if hasattr(self, 'userPosition') and self.userPosition == 2:
    #    #    return
#
    #    if hasattr(self, 'draft'):
    #        self.draft.update()

    def save_json(self, json):
        '''Save the json to the database'''        

        if self.saveTimer is not None and self.saveTimer.isActive(): 
            self.saveTimer.stop()

        self.saveTimer = QTimer(self)
        self.saveTimer.timeout.connect(lambda: self.save(json))
        self.saveTimer.setSingleShot(True)
        self.saveTimer.start(1000)


    def saveFeature(self, json, status=False):
        '''Save the json to the database and set the status'''

        self.save_json(self.json)

        #Temporaty disabled
        self.draft.setStatus(status)

        self.openHome()

        #self.draft.update()

    def updateSaveBtn(self, errors):
        """En-/Disable Save Button"""

        if (self.json['general']['spaufsuchenichtbegehbarursacheid'] != 1 or self.json['general']['spaufsuchenichtwaldursacheid'] != 0) and self.json['general']['spaufsucheaufnahmetruppkuerzel'] != None and len(self.json['general']['spaufsucheaufnahmetruppkuerzel']) > 2 and self.json['general']['spaufsucheaufnahmetruppgnss'] != None and len(self.json['general']['spaufsucheaufnahmetruppgnss']) > 2:
            self.saveBar.validate([])
        else:
            self.saveBar.validate(errors)

    def save(self, json):
        """Save the json to the database and temp save trupp-id und gnss"""

        self.draft.saveFeature(json)

        if self.previousGeneral == None:
            self.previousGeneral = copy.deepcopy(json['general'])

        if json['general']['spaufsucheaufnahmetruppkuerzel'] != None and json['general']['spaufsucheaufnahmetruppkuerzel'] != self.previousGeneral['spaufsucheaufnahmetruppkuerzel']:
            self.previousGeneral['spaufsucheaufnahmetruppkuerzel'] = json['general']['spaufsucheaufnahmetruppkuerzel']
        if json['general']['spaufsucheaufnahmetruppgnss'] != None and json['general']['spaufsucheaufnahmetruppgnss'] != self.previousGeneral['spaufsucheaufnahmetruppgnss']:
            self.previousGeneral['spaufsucheaufnahmetruppgnss'] = json['general']['spaufsucheaufnahmetruppgnss']
        
    def addPreviousGeneral(self, newJson):
        """Add previous temp saved general data to new json"""
        
        if 'general' in newJson and self.previousGeneral != None:
            if 'spaufsucheaufnahmetruppkuerzel' in self.previousGeneral and newJson['general']['spaufsucheaufnahmetruppkuerzel'] == None:
                newJson['general']['spaufsucheaufnahmetruppkuerzel'] = self.previousGeneral['spaufsucheaufnahmetruppkuerzel']
            if 'spaufsucheaufnahmetruppgnss' in self.previousGeneral and newJson['general']['spaufsucheaufnahmetruppgnss'] == None:
                newJson['general']['spaufsucheaufnahmetruppgnss'] = self.previousGeneral['spaufsucheaufnahmetruppgnss']


    def openHome(self):
        """Open the home screen"""

        self.setPosition(1)
        self.lfbTabWidget.setCurrentIndex(0)

        Utils.deselectFeature()

    def setPosition(self, position):
        """Set state of home screen"""

        if self.userPosition == position:
            return

        self.userPosition = position

        if self.userPosition == 2: # Form
            self.lfbFormWidget.show()
            self.saveBar.show()
            self.draft.hide()
            self.lfbHomeScreen.hide()
            self.create_FIM_layer_widget.hide()
        elif self.userPosition == 1: # Home Screen
            self.lfbFormWidget.hide()
            self.saveBar.hide()
            self.draft.show()
            self.draft.update()
            self.lfbHomeScreen.show()
            self.create_FIM_layer_widget.hide()
        else: # FIM Layer not found
            self.lfbFormWidget.hide()
            self.saveBar.hide()
            self.draft.hide()
            self.lfbHomeScreen.hide()
            self.create_FIM_layer_widget.show()


    def create_new_FIM_layer(self):
        """Create the FIM layer"""

        self.draft.setupDraftLayer()
        self.check_fim_layer_exists()


    def addDraft(self):
        """Build feature lists"""

        self.draft = DraftSelection(self.iface)

        try:
            self.draft.draftSelected.disconnect()
            #self.draft.unterlosSelected.disconnect()
        except:
            pass

        self.draft.draftSelected.connect(self.draftSelected)
        #self.draft.unterlosSelected.connect(self.unterlosSelected)
        self.lfbHomeInputs.addWidget(self.draft)

        self.create_new_FIM_layer()

    def unterlosSelected(self, feature):
        """Open the unterlos form dialog"""

        
        dialog = UnterlosnrDialog(None, feature)
        #dialog.token_changed.connect(self.set_token)
        #dialog.set_email.connect(self.set_email)

        #dialog.ui = Authentication()
        #dialog.ui.setupUi(dialog)
        #dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()


    def draftSelected(self, newJson, id, feature):
        """Load the selected feature"""

        self.addPreviousGeneral(newJson)

        self.json = newJson # Form Only        
        
        self.updateVwmForm()
        

        type = self.json['types'] if 'types' in self.json else 'vwm'
        version = self.json['versions'] if 'versions' in self.json else '1.0.0'
        self.schema = self.loadSchema(type, version) 
        
        self.setPosition(2)
        
        self.saveBar.setAttributes(feature, 'los_id')
        self.draft.resetCurrentDraft(id)

        Utils.focusFeature(self.iface, feature, True, 15000)

    # Deprecated
    #def validateTabs(self, save = False):
    #    """Validate the tabs & Save"""
    #
    #    self._validateTabs()
    #
    #    if save:
    #        self.save()

    def _validateTabs(self):
        """Validate the tabs and set errors of dynamic tabs"""
       
        isValidToSave = False

        v = Draft7Validator(self.schema)

        self.schemaErrors = sorted(v.iter_errors(self.json), key=lambda e: e.path)
       
        for tab in self.tabsArray:

            attr = tab['attr']

            errorFound = False

            for error in self.schemaErrors:
                if attr in error.relative_schema_path:
                    errorFound = True
                    self.lfbTabWidget.setTabIcon(tab['tabNr'], QtGui.QIcon(':icons/red_rect.png'))
                    break

            if not errorFound:
                self.lfbTabWidget.setTabIcon(tab['tabNr'], QtGui.QIcon(':icons/green_rect.png'))
        

        # Triggers errors
        self.update_tab_errors(self.schemaErrors)
        
        return isValidToSave
    
    def update_tab_errors(self, errors):
        """Update the errors of the dynamic tabs"""
        
        for tab in self.tabsArray:
            tab['update_errors'](errors)