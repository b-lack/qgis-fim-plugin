from qgis.core import QgsProject, QgsExpressionContextUtils, QgsMapLayer
from qgis.core import QgsMessageLog

class Utils(object):

    @staticmethod    
    def enumLabel(a,b):
        idx = b['enum'].index(a)
        return str(b['enumLabels'][idx])
    

    def getLayerByName(lfbName, lfbVersion = None):
        names = [layer for layer in QgsProject.instance().mapLayers().values()]

        for i in names:
            if QgsExpressionContextUtils.layerScope(i).variable('LFB-NAME') == lfbName :
                return i
            
        return None
    
    def getSelectedFeatures(interface, lfbName):
        for layer in QgsProject.instance().mapLayers().values():

            if not layer.isSpatial():
                continue

            if QgsExpressionContextUtils.layerScope(layer).variable('LFB-NAME') == lfbName :
                continue
            
            if layer.type() != QgsMapLayer.VectorLayer:
                continue

            if layer.wkbType() != 1: # POINT LAYER
                continue
            
            selected_features = layer.selectedFeatures()
            return selected_features

                # Now we have a layer without geometry
        return []

        layer = interface.activeLayer()

        
        
        selected_features = layer.selectedFeatures()
        return selected_features