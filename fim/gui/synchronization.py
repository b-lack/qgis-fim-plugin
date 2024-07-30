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
from PyQt5.QtCore import QCoreApplication, QUrl, QUrlQuery, QByteArray
from ..utils.helper import Utils


#from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui

#from ...utils.helper import Utils


UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'synchronization.ui'))

LOGIN_ENDPOINT = "https://db01.simplex4data.de/projekte/lfb/postgrest/rpc/login"
EXPORT_HOST = "https://db01.simplex4data.de/projekte/lfb/postgrest/rpc/export_geojson"

IMPORT_HOST = "https://db01.simplex4data.de/projekte/lfb/postgrest/rpc/import_geojson"
#IMPORT_HOST = "http://localhost:3000/rpc/import_geojson"

class Synchronization(QtWidgets.QWidget, UI_CLASS):

    geojson_received = QtCore.pyqtSignal(object)

    def __init__(self, interface):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())
        self.setupUi(self)

        self.nam_get = QNetworkAccessManager()
        self.nam_get.finished.connect(self.handle_get_response)

        self.nam_set = QNetworkAccessManager()
        self.nam_set.finished.connect(self.handle_set_response)


    def handle_set_response(self, reply):
        """
        Handle the response from the server.
        """
        data = reply.readAll()
        data_str = bytes(data).decode('utf-8')
        #response = json.loads(reply.readAll().data().decode())

        if reply.error():
            QgsMessageLog.logMessage(f'Error: {reply.errorString()}')
            return
        else:
            try:
                # Parse the string as JSON
                json_data = json.loads(data_str)
                Utils.set_workflow()
            except json.JSONDecodeError as e:
                QgsMessageLog.logMessage(f"Failed to decode JSON: {e}")
                return None
            

    def add_geojson_from_host(self, host = None, token = None):
        """
        Get the geojson data from the host.
        """
        
        try:

            json = {
                #"los_ids":[68]
            }
            document = QJsonDocument(json)

            QgsMessageLog.logMessage('GET: ' + token)

            request = QNetworkRequest(QUrl(EXPORT_HOST))
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            request.setRawHeader(QByteArray(b"Authorization"), QByteArray(f"Bearer {token}".encode('utf-8')))


            #self.nam = QNetworkAccessManager()
            #self.nam.finished.connect(self.handleSyncResponse)

            post_data = QUrlQuery()

            self.nam_get.post(request, document.toJson()) # , document.toJson()

        except Exception as e:
            QgsMessageLog.logMessage(e)
            QgsMessageLog.logMessage("An request error occurred")
    

    def handle_get_response(self, reply):
        """
        Handle the response from the server.
        """
        data = reply.readAll()
        data_str = bytes(data).decode('utf-8')

        #response = json.loads(reply.readAll().data().decode())

        if reply.error():
            QgsMessageLog.logMessage(f'Import Error: {reply.errorString()}', 'FIM')
            return
        else:
            try:
                # Parse the string as JSON
                json_data = json.loads(data_str)
                self.geojson_received.emit(json_data)
            except json.JSONDecodeError as e:
                QgsMessageLog.logMessage(f"Failed to decode JSON: {str(e)}", 'FIM')
                return None
            

    def send_geojson_to_host(self, geojson = None, token = None):
        """
        Send the geojson data to the host.
        """        

        if geojson is None or token is None:
            QgsMessageLog.logMessage("No geojson or token provided", 'FIM')
            return
        
        try:

            json_data = {
                "geojson_data": geojson
            }
            json_str = json.dumps(json_data)
            byte_array = QByteArray(json_str.encode('utf-8'))

            request = QNetworkRequest(QUrl(IMPORT_HOST))
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            request.setRawHeader(QByteArray(b"Authorization"), QByteArray(f"Bearer {token}".encode('utf-8')))

            self.nam_set.post(request, byte_array) # , document.toJson()

        except Exception as e:
            QgsMessageLog.logMessage(e)
            QgsMessageLog.logMessage("An request error occurred")