import os
import json
import collections.abc

from qgis.core import QgsProject, QgsExpressionContextUtils, QgsMapLayer, QgsCoordinateReferenceSystem, QgsCoordinateTransform
from qgis.core import QgsMessageLog
from PyQt5.QtWidgets import QMessageBox

# GNSS plugin
from qgis import qgis

LFB_NAME = 'LFB-Regeneration-Wildlife-Impact-Monitoring'

class Utils(object):

    @staticmethod    
    def enumLabel(a,b):
        idx = b['enum'].index(a)
        return str(b['enumLabels'][idx])
    
    def confirmDialog(interface, title, message):
        msg = QMessageBox()
        msg.setStyleSheet("text-color: rgb(0, 0, 0);")
        msg.setStyleSheet("background-color: rgb(255, 255, 255);")
        return msg.question(interface, title, message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)


    def getMetaData():
        return {
            'version': '0.0.30'
        }

    def schemaTypeHasNull(schema):

        if schema is None:
            return False
        
        if 'type' not in schema:
            return False
        
        if hasattr(schema, "__len__"):
            return 'null' in schema['type']
        else:
            return schema['type'] == 'null'
        
    def isAttributeRequired(schema, key):
        if 'required' in schema:
            return key in schema['required']
        else:
            return True

    def translateRelativeSchemaPath(schema, relative_schema_path):
        isProperties = False
        tab = None
        tabCount = None

        for path in relative_schema_path:

            if isProperties and not tab:
                tabCount = 0
                for key, value in schema['properties'].items():
                    if path  == key:
                        tab = schema['properties'][path]
                        break
                    tabCount += 1

            if path == 'properties':
                isProperties = True
            
           
        if tab is not None and 'title' in tab:
            return tab['title']
        
        return ''
    
    def getFeatureAttribute(feature, key):

        layer = Utils.getLayerByName()
        fields = layer.fields()
        idx = fields.indexFromName(key)
        return feature.attributes()[idx]

    def deepUpdate(d, u):
        for k, v in u.items():
            if isinstance(v, collections.abc.Mapping):
                d[k] = Utils.deepUpdate(d.get(k, {}), v)
            else:
                d[k] = v
        return d
    
    def loadDefaultJson():
        dirname = os.path.dirname(__file__)
        filename = os.path.realpath(os.path.join(dirname, '..', 'schema', 'default.json'))
        fd = open(filename, 'r')
        jsonObj = json.load(fd)
        fd.close()
        return jsonObj
    
    def getCrs():
        return QgsProject.instance().crs().authid()
    
    def transformCoordinates(geom):
        crs = Utils.getCrs()
    
        sourceCrs = QgsCoordinateReferenceSystem.fromEpsgId(4326)
        destCrs = QgsCoordinateReferenceSystem.fromProj(crs)
        tr = QgsCoordinateTransform(sourceCrs, destCrs, QgsProject.instance())
        geom.transform(tr)

    def focusFeature(interface, feature, select = False, zoom = 150000):
        geom = feature.geometry()
        coordinates = geom.asPoint()

        Utils.transformCoordinates(geom)

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