import math
import os

from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog
from PyQt5 import QtCore

from ....utils.helper import Utils

from qgis.core import QgsSettings, QgsApplication, QgsMessageLog, QgsGpsDetector, QgsGpsConnection

UI_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'setup_device.ui'))

PLUGIN_NAME = "lfb_regeneration_wildlife_impact" #lfb_regeneration_wildlife_impact/pb_tool.cfg

class SetupDevice(QtWidgets.QWidget, UI_CLASS):
    inputChanged = QtCore.pyqtSignal(object, str, bool)

    def __init__(self, interface, json, value, attr, inheritedErrors):
        """Constructor."""

        QDialog.__init__(self, interface.mainWindow())
        self.setupUi(self)

        self.json = json
        self.attr = attr

        self.lfbGetCoordinatesGtn.clicked.connect(self.test)
        self.lfbGPSError.setText("")

        s=QgsSettings()
        val=s.value(PLUGIN_NAME+"/layername_fieldname_a")

        # https://gis.stackexchange.com/questions/307209/accessing-gps-via-pyqgis

        
        #GPSInfo = connectionList[0].currentGPSInformation()

        #s.setValue(PLUGIN_NAME+"/layername_fieldname_a", 66)


        
        self.gpsCon = None
        self.portPositionChecked = None
        self.availablePorts = self.autoSelectPort()
        self.tryNextPort()
    
    def tryNextPort(self):

        if self.portPositionChecked is not None:
            self.portPositionChecked = self.portPositionChecked + 1
        else:
            self.portPositionChecked = 0
        
        if self.portPositionChecked < len(self.availablePorts):
            self.detectGPS(self.availablePorts[self.portPositionChecked])
    
    def autoSelectPort(self):
        return QgsGpsDetector.availablePorts()

    def detectGPS(self, port):
        self.gpsDetector = QgsGpsDetector(port[0])

        self.gpsDetector.detected[QgsGpsConnection].connect(self.connection_succeed)
        self.gpsDetector.detectionFailed.connect(self.connection_failed)
        #self.gpsDetector.advance()
        
        return

        connectionRegistry = QgsApplication.gpsConnectionRegistry()
        connectionList = connectionRegistry.connectionList()
        if len(connectionList) > 0:
            # QgsGpsConnection
            self.gpsCon = connectionList[0]
            self.gpsCon.stateChanged.connect(self.status_changed)
            
            QgsMessageLog.logMessage(str('state.change'), "FindLocation")

        else:
            QgsMessageLog.logMessage(str('no.gps'), "FindLocation")

    def connection_succeed(self, connection):
        try:
            self.gpsCon = connection
        except Exception as e:
             QgsMessageLog.logMessage(str(e), "FindLocation")

    def connection_failed(self):
        self.tryNextPort()



    def findPlugin(self):
        if Utils.checkPluginExists(PLUGIN_NAME):
            self.geSetupLabel.setText("Plugin FOUND")
            plugin = Utils.getPluginByName(PLUGIN_NAME)

            results = plugin.tr('fromm')

            #results = plugin.run()
            
        else:
            self.geSetupLabel.setText("Plugin NOT FOUND")


    def status_changed(self, gpsInfo):

        try:
            if self.gpsCon.status() == 3: #data received
                if 'istgeom_y' in self.json and hasattr(gpsInfo, 'latitude'):
                    self.json['istgeom_y'] = gpsInfo.latitude
                if 'istgeom_x' in self.json and hasattr(gpsInfo, 'longitude'):
                    self.json['istgeom_x'] = gpsInfo.longitude
                if 'istgeom_elev' in self.json and hasattr(gpsInfo, 'elevation'):
                    
                    if math.isnan(gpsInfo.elevation):
                        self.json['istgeom_elev'] = None
                    else:
                        self.json['istgeom_elev'] = gpsInfo.elevation
                if 'istgeom_hdop' in self.json and hasattr(gpsInfo, 'hdop'):
                    self.json['istgeom_hdop'] = gpsInfo.hdop
                if 'istgeom_vdop' in self.json and hasattr(gpsInfo, 'vdop'):
                    self.json['istgeom_vdop'] = gpsInfo.vdop
                if 'istgeom_sat' in self.json and hasattr(gpsInfo, 'satellitesUsed'):
                    self.json['istgeom_sat'] = gpsInfo.satellitesUsed

                self.inputChanged.emit(self.json, self.attr, True)
                self.lfbGPSError.setText('')
        except Exception as e:
            self.lfbGPSError.setText('Status:' + str(e))

           

    def test(self):
        # https://qgis.org/pyqgis/3.2/core/Gps/QgsGpsInformation.html
        # https://gis.stackexchange.com/questions/307209/accessing-gps-via-pyqgis

        connectionRegistry = QgsApplication.gpsConnectionRegistry()
        connectionList = connectionRegistry.connectionList()
        if len(connectionList) > 0:
            # QgsGpsConnection
            self.gpsCon = connectionList[0]
            self.gpsCon.stateChanged.connect(self.status_changed)
            
            self.lfbGPSError.setText("")

        else:
            self.lfbGPSError.setText("Es konnte keine aktive Verbindung gefunden verden.")

    def setJson(self, newJson, setFields = True):
        self.json = newJson
    