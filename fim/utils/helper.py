import os
import json
import collections.abc
import re

from qgis.core import QgsProject, QgsPointXY, QgsWkbTypes, QgsExpressionContextUtils, QgsMapLayer, QgsCoordinateReferenceSystem, QgsCoordinateTransform
from qgis.core import QgsMessageLog
from qgis.utils import *

from PyQt5.QtWidgets import QMessageBox

# GNSS plugin
from qgis import qgis

FIM_LAYER_NAME = 'FIM'
FIM_LAYER_VERSION = '1.0.0'
FIM_LAYER_ID = FIM_LAYER_NAME + '-' + FIM_LAYER_VERSION

class Utils(object):

    @staticmethod    
    def enumLabel(a,b):
        idx = b['enum'].index(a)
        return str(b['enumLabels'][idx])
    
    def getLayerName():
        return FIM_LAYER_NAME
    
    def getLayerVersion():
        return FIM_LAYER_VERSION
    
    def pluginAvailable(pluginName):
        if pluginName in available_plugins:
            return True
        return False
    
    def confirmDialog(interface, title, message):
        msg = QMessageBox()
        msg.setStyleSheet("text-color: rgb(0, 0, 0);")
        msg.setStyleSheet("background-color: rgb(255, 255, 255);")
        msg.setStyleSheet("QLabel{ color: white}")
        msg.setStyleSheet("background-color:  rgb(255, 255, 255);color: rgb(0, 0, 0);")


        return msg.question(interface, title, message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)


    def getMetaData():
        return {
            'version': '1.0.12'
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

        layer = Utils.getLayerById()
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
    
    def transformCoordinates(layer):
        crs = Utils.getCrs()

        crsFeature = layer.crs().authid()
        # GET
        
        srcCrsNr = int(crsFeature.split(":")[1])
        QgsMessageLog.logMessage(str(srcCrsNr), 'FIM')
        sourceCrs = QgsCoordinateReferenceSystem.fromEpsgId(3857) #srcCrsNr
        
        destCrsNr = int(crs.split(":")[1])
        QgsMessageLog.logMessage(str(destCrsNr), 'FIM')
        destCrs = QgsCoordinateReferenceSystem.fromEpsgId(destCrsNr) #fromProj(crs)

        return QgsCoordinateTransform(sourceCrs, destCrs, QgsProject.instance())

    def focusFeature(interface, feature, select = False, zoom = 150000):
        geom = feature.geometry()
        coordinates = geom.asPoint()


        map_pos = QgsPointXY(coordinates.x(), coordinates.y())

        xform = Utils.transformCoordinates(Utils.getLayerById())
        map_pos = xform.transform(map_pos)
        interface.mapCanvas().setCenter(map_pos)
        
        current_scale =  interface.mapCanvas().scale()
        interface.mapCanvas().zoomScale(min(zoom, current_scale))

        if select:
            Utils.deselectFeature()
            Utils.selectFeature(feature)

    def selectFeature(feature):
        layer = Utils.getLayerById()
        if layer is not None:
            layer.selectByIds([feature.id()])
    
    def deselectFeature(feature = None):
        layer = Utils.getLayerById()
        if layer is not None:
            if feature is None:
                layer.removeSelection()
            else:
                layer.deselect(feature.id())

    def getLayerById(layerId = None):
        """Get the layer by name."""

        if layerId is None:
            layerId = FIM_LAYER_ID

        layers = QgsProject.instance().mapLayers().values()

        layerId1 = re.sub('[^a-zA-Z0-9 ]', '_', layerId)
        #layerId2 = layerId.replace('-', '_')

        for layer in layers:
            if layer.id().startswith(layerId1) :
                return layer
        
        return None
    
    def getLayerByName(lfbName = None, lfbVersion = None):

        if lfbName is None:
            lfbName = FIM_LAYER_ID

        names = [layer for layer in QgsProject.instance().mapLayers().values()]

        for i in names:
            if QgsExpressionContextUtils.layerScope(i).variable('LFB-NAME') == lfbName :
                return i
            
        return None
    

    def updateToC(updateTocFn):
        """Update the Table of Contents"""

        layers = Utils.selectLayerByType(QgsWkbTypes.PointGeometry)

        for layer in layers:

            try:
                layer.selectionChanged.disconnect(updateTocFn)
            except:
                pass

            layer.selectionChanged.connect(updateTocFn)

        #Utils.getSelections()

    def selectLayerByType(geometryType):
        """List all layers with geometry type."""

        layerList = []

        layers = QgsProject.instance().mapLayers().values()

        for layer in layers:

            try:
                if layer.geometryType() == geometryType:
                    layerList.append(layer)
            except:
                pass
            
        return layerList
    
    def getSelectedFeaturesFim():
        for layer in QgsProject.instance().mapLayers().values():

            layerId1 = re.sub('[^a-zA-Z0-9 ]', '_', FIM_LAYER_ID)
            
            if layer.id().startswith(layerId1) :
                return layer.selectedFeatures()

        return []

    def getSelectedFeatures(interface, lfbName, removeSelection = False):

        selected_features = []
        selected_layers = []

        for layer in QgsProject.instance().mapLayers().values():

            if not layer.isSpatial():
                continue

            layerId1 = re.sub('[^a-zA-Z0-9 ]', '_', FIM_LAYER_ID)
            
            if layer.id().startswith(layerId1) :
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