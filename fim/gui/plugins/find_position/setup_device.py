import math
import os

import pandas as pd

from qgis.PyQt import QtWidgets, uic
from qgis.PyQt.QtWidgets import QDialog
from PyQt5 import QtCore
from qgis.PyQt.QtCore import QSettings


from ....utils.helper import Utils

from qgis.core import QgsSettings, QgsApplication, QgsMessageLog, QgsGpsDetector, QgsGpsConnection, QgsNmeaConnection

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
        self.measures = []

        self.gpsCon = None

        try:
            self.lfbGetCoordinatesGtn.clicked.disconnect()
            self.lfbCancelCoordinatesBtn.clicked.disconnect()
            self.lfbSerialPortList.currentIndexChanged.disconnect()
        except:
            pass


        self.lfbGetCoordinatesGtn.clicked.connect(self.connect)
        self.lfbGPSError.setText("")
        self.lfbGPSState.setText("")

        self.lfbCancelCoordinatesBtn.clicked.connect(self.cancelConnection)
        self.lfbCancelCoordinatesBtn.setEnabled(False)

        self.lfbSerialPortList.currentIndexChanged.connect(self.onSerialPortChanged)

        #s=QgsSettings()
        #val=s.value(PLUGIN_NAME+"/layername_fieldname_a")
        # https://gis.stackexchange.com/questions/307209/accessing-gps-via-pyqgis
        #GPSInfo = connectionList[0].currentGPSInformation()
        #s.setValue(PLUGIN_NAME+"/layername_fieldname_a", 66)

        self.ports = self.getSerialPorts()
        self.updateSerialPortSelection(self.ports)

        serialSetting = self.getGPSSettings()
        
        if serialSetting is None:
            self.lfbGPSError = 'Wähle ein "Serielles Gerät" aus.'
        else:
            self.selectPort(serialSetting)
        
        #
        #self.portPositionChecked = None
        #self.availablePorts = self.autoSelectPort()
        #self.tryNextPort()

    def getSerialPorts(self):
        return QgsGpsDetector.availablePorts()
    
    def updateSerialPortSelection(self, ports):
        self.lfbSerialPortList.clear()
        for port in ports:
            self.lfbSerialPortList.addItem(port[0], port[0])

    def selectPort(self, port):
        index = self.lfbSerialPortList.findData(port)
        if index != -1 :
            self.lfbSerialPortList.setCurrentIndex(index)

    def getGPSSettings(self):
        return QgsSettings().value('gps/gpsd-serial-device')
    
    def onSerialPortChanged(self, index):
        self.port = self.lfbSerialPortList.itemData(index)
        QgsSettings().setValue('gps/gpsd-serial-device', self.port)
    
    def connect(self, port):
        if self.port is None:
            self.lfbGPSError.setText('Wähle ein "Serielles Gerät" aus.')
            return
        
        try:
            self.gpsDetector.detected[QgsGpsConnection].disconnect(self.connection_succeed)
            self.gpsDetector.detectionFailed.disconnect(self.connection_failed)
        except:
            pass
        
        self.lfbGetCoordinatesGtn.setEnabled(False)
        self.lfbGPSError.setText("")
        self.lfbGPSState.setText('Verbindung zum GPS-Gerät am Port "' + self.port + '" wird hergestellt...')

        self.gpsDetector = QgsGpsDetector(self.port)
        self.gpsDetector.detected[QgsGpsConnection].connect(self.connection_succeed) #
        self.gpsDetector.detectionFailed.connect(self.connection_failed)
        self.gpsDetector.advance()

    def cancelConnection(self):

        QgsMessageLog.logMessage(str(self.gpsCon), 'LFB')
        try:
            if self.gpsCon is not None:
                self.gpsCon.stateChanged.disconnect(self.status_changed)

                self.gpsCon.close()
                self.gpsCon = None

           

            self.gps_active = False
            #self.lfbGPSState.setText("Connection Cancelled")
            self.lfbCancelCoordinatesBtn.setEnabled(False)
            self.lfbGetCoordinatesGtn.setEnabled(True)
            self.measures = []
            self.setMeasurementsCount()
            #self.lfbGPSState.setText("Keine Verbindung die geschlossen werden könnte.")

        except Exception as e:
            self.lfbGPSError.setText(str(e))

    def connection_succeed(self, connection):

        if self.gpsCon is not None:
            self.cancelConnection()

        # https://python.hotexamples.com/examples/PyQt5.QtSerialPort/QSerialPort/setDataBits/python-qserialport-setdatabits-method-examples.html

        if not isinstance(connection, QgsNmeaConnection):
            QgsMessageLog.logMessage('is not QgsNmeaConnection', 'LFB')
            import sip
            gpsConnection = sip.cast(connection, QgsGpsConnection)
            self.gpsCon = gpsConnection

        elif isinstance(connection, QgsGpsConnection):
            self.gpsCon = gpsConnection
        else:
            self.lfbGPSState.setText("Es konnte keine Verbindung zum GPS-Gerät hergestellt werden.")
            return

        try:
            
            self.lfbCancelCoordinatesBtn.setEnabled(True)
            #self.gpsCon = connection
            self.gpsCon.stateChanged.connect(self.status_changed)
            #self.gpsCon.positionChanged.connect(self.position_changed)
            
            self.gps_active = True
            self.lfbGPSState.setText("Verbindung ist hergestellt.")
        except Exception as e:
             self.lfbGPSError.setText('connection_succeed:' + str(e))

    def connection_failed(self):
        self.lfbGPSState.setText("")
        self.lfbGPSError.setText('Es konnte keine Verbindung zum Port "' + self.port + '" hergestellt werden.')
        self.lfbGetCoordinatesGtn.setEnabled(True)

    def position_changed(self, gpsInfo):
        QgsMessageLog.logMessage('position_changed')
        QgsMessageLog.logMessage(str(gpsInfo))

    def status_changed(self, gpsInfo):
        
        QgsMessageLog.logMessage(str('fff'), 'LFB')
        

        try:
            self.lfbGPSState.setText('Daten wurden erfolgreich ermittelt.')
            self.lfbGPSError.setText('')
            self.emitAggregatedValues(gpsInfo)

        except Exception as e:
           self.lfbGPSError.setText(str(e))
        
    def setMeasurementsCount(self):
        self.lfbGPSCount.setText(str(len(self.measures)))

    def emitAggregatedValues(self, GPSInfo):
        

        lat = GPSInfo.latitude
        long = GPSInfo.longitude
        hdop = GPSInfo.hdop
        vdop = GPSInfo.vdop
        elevation = GPSInfo.elevation
        satellitesUsed = GPSInfo.satellitesUsed

        measure = [lat,long,elevation, hdop,vdop, satellitesUsed]
        self.measures.append(measure)
        self.setMeasurementsCount()

        df = pd.DataFrame(self.measures)
        #result = [str(df[0].mean()), str(df[1].mean()), str(df[2].mean()), str(df[3].mean()), str(df[4].mean()), str(df[5].mean())]

        

        self.json['istgeom_y'] = df[0].mean()
        self.json['istgeom_x'] = df[1].mean()
        
        self.json['istgeom_elev'] = df[2].mean()

        self.json['istgeom_hdop'] = df[3].mean()
        self.json['istgeom_vdop'] = df[4].mean()     

        self.json['istgeom_sat'] = df[5].mean()

        if len(self.measures) >= 5:
            self.inputChanged.emit(self.json, self.attr, True)
            self.cancelConnection()

    def setJson(self, newJson, setFields = True):
        self.json = newJson
