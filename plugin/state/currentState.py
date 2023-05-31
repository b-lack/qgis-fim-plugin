from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction
from qgis.core import QgsProject, QgsMessageLog

class CurrentState(object):
    def __init__(self):
        self._state = None
        self._observers = []
        print('CurrentState object created')
        QgsMessageLog.logMessage('state init', "LFB")

    @property
    def observerCount(self):
        return len(self._observers)
    
    @property
    def state(self):
        return self._state

    def change_state(self, state):
        # VALIDATE STATE
        self._state = state
        self.notify()

    def notify(self):
        for observer in self._observers:
            observer(self._state)

    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
