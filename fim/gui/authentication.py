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

from qgis.core import QgsMessageLog, QgsProject, QgsWkbTypes, QgsVectorFileWriter, QgsFeature, QgsGeometry, QgsPointXY
from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtCore import QDateTime, QJsonDocument
from PyQt5.QtNetwork import  QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtCore import QCoreApplication, QUrl


#from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui

#from ...utils.helper import Utils


UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'authentication.ui'))

LOGIN_ENDPOINT = "https://db01.simplex4data.de/projekte/lfb/postgrest/rpc/login"
EXPORT_HOST = "http://localhost:3000/rpc/import_geojson"

class Authentication(QDialog, UI_CLASS):

    token_changed = QtCore.pyqtSignal(str)
    set_email = QtCore.pyqtSignal(str)

    def __init__(self, parent=None, email=None, password=None):
        """Constructor."""

        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.token = None

        self.auth_btn_send.clicked.connect(self.auth_send_btn_clicked)
        self.auth_input_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.auth_input_pass.setPlaceholderText("Password")
        self.auth_input_email.setPlaceholderText("Username")
        self.auth_input_email.setText(email)

        self.auth_error_label.setText("")
        self.auth_error_label.setStyleSheet("color: red")


    def set_token(self, token=None):
        self.token = token
        self.token_changed.emit(self.token)

    def enable_send_btn(self, reset=False):
        self.auth_btn_send.setEnabled(True)
        self.auth_btn_send.setText("Login")
        self.auth_btn_send.repaint()

        if reset:
            self.auth_input_pass.setText("")
        
    def handleResponse(self, reply):
        """
        Handle the response from the server.
        """
        
        if reply.error():
            self.auth_error_label.setText(f'Login failed: {reply.errorString}')
            self.enable_send_btn(True)
            return
        
        response = json.loads(reply.readAll().data().decode())
        if 'message' in response.keys():
            self.auth_error_label.setText(response['message'])
            self.enable_send_btn(True)
            return

        if 'token' in response.keys():
            self.set_token(response['token'])

            self.auth_error_label.setText("")
            self.enable_send_btn(True)
            self.close()
        else:
            self.auth_error_label.setText("Login failed")
            self.enable_send_btn(True)


    def auth_send_btn_clicked(self):
        self.auth_error_label.setText("")

        password = self.auth_input_pass.text()
        email = self.auth_input_email.text()

        if email == "" or password == "":
            self.auth_error_label.setText("email or password is empty")
            return
        
        # Disable the button
        self.auth_btn_send.setEnabled(False)
        self.auth_btn_send.setText("Loading...")
        self.auth_btn_send.repaint()

        # Make a request to the server
        try:

            json = {'email': email, 'pass': password}
            document = QJsonDocument(json)

            request = QNetworkRequest(QUrl(LOGIN_ENDPOINT))
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")


            self.nam = QNetworkAccessManager()
            self.nam.finished.connect(self.handleResponse)
            self.nam.post(request, document.toJson())

            self.set_email.emit(email)

        except Exception as e:
            self.auth_error_label.setText("An request error occurred")
            self.enable_send_btn(True)

    def handleSyncResponse(self, reply):
        """
        Handle the response from the server.
        """

        response = json.loads(reply.readAll().data().decode())


        if reply.error():
            QgsMessageLog.logMessage(f'Error: {reply.errorString()}')
            return

    def add_geojson_from_host(self, host = None, token = None):
        """
        Get the geojson data from the host.
        """
        
        try:

            json = {
                "los_ids":[1]
            }
            document = QJsonDocument(json)

            request = QNetworkRequest(QUrl(EXPORT_HOST))
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")


            self.nam = QNetworkAccessManager()
            self.nam.finished.connect(self.handleSyncResponse)
            self.nam.post(request, document.toJson())

        except Exception as e:
            QgsMessageLog.logMessage(e)
    