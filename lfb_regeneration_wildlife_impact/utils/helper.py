import os
import json

from qgis.core import QgsProject, QgsExpressionContextUtils, QgsMapLayer
from qgis.core import QgsMessageLog

# GNSS plugin
from qgis import qgis

LFB_NAME = 'LFB-Regeneration-Wildlife-Impact-Monitoring'

class Utils(object):

    @staticmethod    
    def enumLabel(a,b):
        idx = b['enum'].index(a)
        return str(b['enumLabels'][idx])
    
    def getFeatureAttribute(feature, key):

        layer = Utils.getLayerByName()
        fields = layer.fields()
        idx = fields.indexFromName(key)
        return feature.attributes()[idx]

    def loadDefaultJson():
        dirname = os.path.dirname(__file__)
        filename = os.path.realpath(os.path.join(dirname, '..', 'schema', 'default.json'))
        fd = open(filename, 'r')
        return json.load(fd)

    def focusFeature(interface, feature, select = False, zoom = 150000):
        geom = feature.geometry()
        coordinates = geom.asPoint()

        interface.mapCanvas().setCenter(coordinates)
        
        current_scale =  interface.mapCanvas().scale()
        interface.mapCanvas().zoomScale(min(zoom, current_scale))

        if select:
            Utils.deselectFeature()
            Utils.selectFeature(feature)

    def selectFeature(feature):
        layer = Utils.getLayerByName(LFB_NAME)
        if layer is not None:
            layer.selectByIds([feature.id()])
    
    def deselectFeature(feature = None):
        layer = Utils.getLayerByName(LFB_NAME)
        if layer is not None:
            if feature is None:
                layer.removeSelection()
            else:
                layer.deselect(feature.id())

    def getLayerByName(lfbName = None, lfbVersion = None):

        if lfbName is None:
            lfbName = LFB_NAME

        names = [layer for layer in QgsProject.instance().mapLayers().values()]

        for i in names:
            if QgsExpressionContextUtils.layerScope(i).variable('LFB-NAME') == lfbName :
                return i
            
        return None
    
    def getSelectedFeatures(interface, lfbName, removeSelection = False):

        selected_features = []
        selected_layers = []

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
            if len(selected_features) == 0:
                continue

            if removeSelection:
                layer.removeSelection()

            selected_layers.append({
                'layer': layer,
                'features': selected_features
            })

                # Now we have a layer without geometry

        return selected_layers

        layer = interface.activeLayer()

        selected_features = layer.selectedFeatures()
        return selected_features
    
    #GNSS PLUGIN
    def getPluginByName(plugin_name):
        return qgis.utils.plugins[plugin_name]

    def checkPluginExists(plugin_name):
        return plugin_name in qgis.utils.plugins