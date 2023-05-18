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
        return self._observers.count()

    def change_state(self, state):
        # VALIDATE STATE
        QgsMessageLog.logMessage('change state', "LFB")
        self._state = state
        self.notify()

    def notify(self):

        for observer in self._observers:
            observer(self._state)
            QgsMessageLog.logMessage(type(observer).__name__, "LFB")

    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)
            print('Attached an observer')
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
            print('Detached an observer')
        except ValueError:
            pass
