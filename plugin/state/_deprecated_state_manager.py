from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import QgsProject, QgsMessageLog
from PyQt5 import QtCore

class StateManager(object):
    stateChange = QtCore.pyqtSignal(object)

    def __init__(self):
        self._state = None
    
    @property
    def state(self):
        return self._state

    def change_state(self, state):
        self._state = state

        self.stateChange.emit(self._state)
