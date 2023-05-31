import os
import sys
from qgis.core import QgsApplication

QgsApplication.setPrefixPath('/usr/bin/qgis', True)
qgs = QgsApplication([], True)
qgs.initQgis()

#from .gui.lfb_regeneration_wildlife_impact_dialog import LfbRegenerationWildlifeImpactDialog
from __lfb_regeneration_wildlife_impact import LfbRegenerationWildlifeImpact
main_window = LfbRegenerationWildlifeImpact()
main_window.show()
qgs.exec_()
qgs.exitQgis()