import os
import json
import collections.abc
import re

from jsonschema import Draft7Validator, exceptions

from qgis.core import QgsMessageLog, QgsProject, QgsPointXY, QgsWkbTypes, QgsExpressionContextUtils, QgsMapLayer, QgsCoordinateReferenceSystem, QgsCoordinateTransform
from qgis.utils import *

from PyQt5.QtWidgets import QMessageBox

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
        """Get the layer name."""
        return FIM_LAYER_NAME
    
    def getLayerVersion():
        """Get the layer version."""
        return FIM_LAYER_VERSION
    
    def confirmDialog(interface, title, message):
        """Show a confirmation dialog."""

        msg = QMessageBox()
        msg.setStyleSheet("text-color: rgb(0, 0, 0);")
        msg.setStyleSheet("background-color: rgb(255, 255, 255);")
        msg.setStyleSheet("QLabel{ color: white}")
        msg.setStyleSheet("background-color:  rgb(255, 255, 255);color: rgb(0, 0, 0);")
        return msg.question(interface, title, message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    def getMetaData():
        """Get the meta data."""

        return {
            'version': '1.0.36'
        }

    def schemaTypeHasNull(schema):
        """Check if the schema type (array) has null."""

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
        """Translate the relative schema path to the title."""

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
        """Get the feature attribute by key."""

        layer = Utils.getLayerById()
        fields = layer.fields()
        idx = fields.indexFromName(key)
        return feature.attributes()[idx]

    def deepUpdate(d, u):
        """Deep update dictionary."""

        for k, v in u.items():
            if isinstance(v, collections.abc.Mapping):
                d[k] = Utils.deepUpdate(d.get(k, {}), v)
            else:
                d[k] = v
        return d
    
    def loadDefaultJson(_fileName = 'default.json'):
        """Load the default JSON schema."""

        dirname = os.path.dirname(__file__)
        filename = os.path.realpath(os.path.join(dirname, '..', 'schema', _fileName))
        fd = open(filename, 'r')
        jsonObj = json.load(fd)
        fd.close()
        return jsonObj
    
    def transformCoordinates(layer):
        """Get the coordinate transform for the layer."""

        crs = QgsProject.instance().crs().authid()

        crsFeature = layer.crs().authid()
        
        srcCrsNr = int(crsFeature.split(":")[1])
        sourceCrs = QgsCoordinateReferenceSystem.fromEpsgId(srcCrsNr) #srcCrsNr
        
        destCrsNr = int(crs.split(":")[1])
        destCrs = QgsCoordinateReferenceSystem.fromEpsgId(destCrsNr) #fromProj(crs)

        return QgsCoordinateTransform(sourceCrs, destCrs, QgsProject.instance())

    def focusFeature(interface, feature, select = False, zoom = 2000):
        """Center/Zoom the feature"""

        geom = feature.geometry()
        coordinates = geom.asPoint() 

        
        map_pos = QgsPointXY(coordinates.x(), coordinates.y())

        xform = Utils.transformCoordinates(Utils.getLayerById())
        #map_pos = xform.transform(map_pos)
        interface.mapCanvas().setCenter(map_pos)
        
        current_scale =  interface.mapCanvas().scale()
        if zoom is not None:
            interface.mapCanvas().zoomScale(min(zoom, current_scale))

        if select:
            Utils.deselectFeature()
            Utils.selectFeature(feature)

    def selectFeatureById(id):
        """Select the feature by ID."""
        layer = Utils.getLayerById()
        if layer is not None:
            layer.selectByIds([id])

    def selectFeatures(features = []):
        """Select the feature by ID."""
        layer = Utils.getLayerById()
        if layer is not None:
            layer.selectByIds([feature.id() for feature in features])

    def selectFeature(feature):
        """Select the feature by ID."""
        layer = Utils.getLayerById()
        if layer is not None:
            layer.selectByIds([feature.id()])
    
    def refreshLayer():
        """Refresh the layer."""
        layer = Utils.getLayerById()
        if layer is not None:
            layer.triggerRepaint()

    def deselectFeature(feature = None):
        """Deselect the feature."""

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

        for layer in layers:
            if layer.id().startswith(layerId1) :
                return layer
        
        return None
    
    def getLayerByName(lfbName = None, lfbVersion = None):
        """Get the layer by name."""

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
        """Get the selected features."""

        for layer in QgsProject.instance().mapLayers().values():

            layerId1 = re.sub('[^a-zA-Z0-9 ]', '_', FIM_LAYER_ID)
            
            if layer.id().startswith(layerId1) :
                return layer.selectedFeatures()

        return []

    def getSelectedFeatures(interface, lfbName, removeSelection = False):
        """Get the selected features."""

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

        return selected_layers
    
    def getPluginByName(plugin_name):
        """Get the plugin by name."""
        return qgis.utils.plugins[plugin_name]

    def checkPluginExists(plugin_name):
        """Check if the plugin exists."""
        return plugin_name in qgis.utils.plugins
    
    def pluginAvailable(pluginName):
        """Check if the plugin is available."""
        if pluginName in available_plugins:
            return True
        return False
    def idNotUnique(layer, id):
        """Check if the ids are unique."""
       
        for f in layer.getFeatures():
            if str(f['los_id']) == str(id):
                return f
        return None
    
    def update_unterlosnummer(feature, unterlosnr):
        """Set the unterlosnummer."""

        vl = Utils.getLayerById()
        
        for tFeature in vl.getFeatures():

            if tFeature['los_id'] != feature['los_id']:
                continue

            vl.startEditing()
            tFeature.setAttribute('unterlosnr', unterlosnr)
            vl.updateFeature(tFeature)

            break
    
    def update_unterlosnummern(features, unterlosnr):
        """Set the unterlosnummer."""

        vl = Utils.getLayerById()
        
        for tFeature in vl.getFeatures():
            # if tFeature['los_id'] is not in features array
            if tFeature['los_id'] not in [feature['los_id'] for feature in features]:
                continue

            vl.startEditing()
            tFeature.setAttribute('unterlosnr', unterlosnr)
            vl.updateFeature(tFeature)

    
    def set_workflow(type):
        """Set the workflow AFTER upload."""

        vl = Utils.getLayerById()
        for tFeature in vl.getFeatures():
            currentWorkflow = Utils.getFeatureAttribute(tFeature, 'workflow')

            status = 0
            
            if type == 'upload':
                if currentWorkflow == 5: # Aufnahmetrupp
                    currentWorkflow = 6
                elif currentWorkflow == 9: # Kontrolltrupp
                    currentWorkflow = 17
                elif currentWorkflow == 22: # Inventurleiter
                    currentWorkflow = 23
                else:
                    continue
            elif type == 'download':
                if currentWorkflow == 3: # Aufnahmetrupp
                    currentWorkflow = 4
                elif currentWorkflow == 18: # Kontrolltrupp
                    currentWorkflow = 8
                elif currentWorkflow == 20: # Inventurleiter
                    currentWorkflow = 21
                else:
                    continue
            else:
                continue

            vl.startEditing()
            
            tFeature.setAttribute('workflow', currentWorkflow)
            # tFeature.setAttribute('status', status)

            vl.updateFeature(tFeature)
            vl.commitChanges()
            vl.endEditCommand()

    def validateAll(schema, json):
        """Validate all features."""

        v = Draft7Validator(schema)

        schemaErrors = sorted(v.iter_errors(json), key=lambda e: e.path)
        lfbErrors = Utils.lfbLayers(json)

        for error in lfbErrors:
            schemaErrors.append(error)

        return schemaErrors
    
    def lfbLayers(self, json):

        # https://github.com/b-lack/qgis-fim-plugin/issues/25

        # 0 = Plenter
        # 1 = Hauptbestand
        # 2 = Unterstand
        # 3 = Oberstand

        label_errors = []

        rules_type = {
            1: [ # es
                [3, 1, 36, 9],
                [31, 36, 9]
            ],
            2: [ # zs
                [3, 1, 2, 4, 36, 9],
                [2, 4, 31, 36, 9]
            ],
            3: [ # ms
                [3, 1, 25, 2, 4, 31, 36, 9]
            ],
            4: [ # zsv
                [3, 1, 2, 4, 36, 9]
            ],
            5: [ # zsu
                [3, 1, 2, 4, 36, 9]
            ],
            6: [ # pl
                [0]
            ],
            7: [ # 3
                [3, 1, 25, 2, 4, 36, 9],
                [3, 2, 4, 31, 36, 9]
            ]
        }
        rules_length = {
            1: {
                "min": 1,
                "max": 1
            },
            2: {
                "min": 2,
                "max": 2
            },
            3: {
                "min": 3,
                "max": 10
            },
            4: {
                "min": 2,
                "max": 2
            },
            5: {
                "min": 2,
                "max": 2
            },
            6: {
                "min": 1,
                "max": 10
            },
            7: {
                "min": 1,
                "max": 10
            }
        }


        elements = [d['schicht_id'] for d in json['t_bestockung']['t_bestockung']]
        elements_unique = list(set(elements))
        #elements_unique.sort()

        if 'bestandnschichtigid' not in json['bestandsbeschreibung']:
            return []
        
        schicht_id = json['bestandsbeschreibung']['bestandnschichtigid']

        if rules_length.get(schicht_id) != None:

            

            if (len(elements_unique) < rules_length[schicht_id]['min'] or len(elements_unique) > rules_length[schicht_id]['max']):
                label_errors.append(exceptions.ValidationError(
                    message='Anzahl an Bestockungsschichten entspricht nicht der n-Schichtigkeit der Bestandesbeschreibung.',
                    validator='minItems',
                    validator_value=rules_length[schicht_id]['min'],
                    instance=elements_unique,
                    schema_path=['allOf', 3, 'then', 'properties', 't_bestockung', 'properties', 't_bestockung', 'minItems']
                ))
        
        if rules_type.get(schicht_id) != None:
            for i in rules_type[schicht_id]:
                
                if(all(x in i for x in elements)):
                    break
                else:
                    label_errors.append(exceptions.ValidationError(
                        message='Falsche Schichtenkombination',
                        validator='minItems',
                        validator_value=rules_length[schicht_id]['min'],
                        instance=elements_unique,
                        schema_path=['allOf', 3, 'then', 'properties', 't_bestockung', 'properties', 't_bestockung', 'minItems']
                    ))
        
        return label_errors