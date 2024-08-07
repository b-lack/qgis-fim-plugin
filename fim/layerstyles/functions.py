from qgis.core import *
from qgis.gui import *
from qgis.utils import qgsfunction

import math
import colorsys

import json

@qgsfunction(args='auto', group='Custom')
def color_by_workflow(workflow):
    values = (
            ('Von FU heruntergeladen - offline bei FU', 4, 4, '#decc44'),
            ('Sps', 1, 5, '#e62323'),
            ('bearbeitet oder hochgeladen', 5, 6, '#729b6f'),
            ('kontrolle', 7, 8, '#f3a6b2'),
            ('wiederholungsaufnahme', 11, 12, '#b80808'),
            ('sonstige', 13, 100, '#1228d1')
    )

    return '#1228d1'

@qgsfunction(args='auto', group='Custom')
def lfb_transect(geometry, form):

    jsonObject = json.loads(form)

    return geometry, 22/10000, radians(23  * 360 / 400)

@qgsfunction(args='auto', group='Custom')
def meters_to_map_units(meters):
    return QgsRenderContext().convertMetersToMapUnits(meters)

@qgsfunction(args='auto', group='Custom')
def azimuttransektploteins_to_degree(form):
    jsonObject = json.loads(form)

    gon = jsonObject['baumplot1']['azimuttransektploteins']
    return gon * 360 / 400

@qgsfunction(args='auto', group='Custom')
def azimuttransektploteins(form):
    jsonObject = json.loads(form)

    return str(jsonObject['baumplot1']['azimuttransektploteins']) + ' gon'

# Baumart Label
@qgsfunction(args='auto', group='Custom')
def lfb_label_baumart(form, nr):

    jsonObject = json.loads(form)
    default = 'not set'

    if 'baumplot1' in jsonObject and 'baumplot1' in jsonObject['baumplot1']:
        default = 'BA: ' + str(jsonObject['baumplot1']['baumplot1'][nr-1]['icode_ba'])
        default += ', ' + str(jsonObject['baumplot1']['baumplot1'][nr-1]['azimut']) + ' gon'
        default += ', ' + str(jsonObject['baumplot1']['baumplot1'][nr-1]['distanz']) + ' cm'


    return default

@qgsfunction(args='auto', group='Custom')
def lfb_baumplot(form):

    jsonObject = json.loads(form)

    trees = []

    if 'baumplot1' in jsonObject and 'baumplot1' in jsonObject['baumplot1']:
        for tree in jsonObject['baumplot1']['baumplot1']:

            trees.append({
                'azimuth': math.radians(tree['azimut'] * 360 / 400),
                'distance': QgsRenderContext().convertMetersToMapUnits(tree['distanz'] / 100) , # Zentimeter
                'diameter': QgsRenderContext().convertMetersToMapUnits(tree['bhd']) / 1000, # Millimeter
            })

    return trees

# TREE SIZE
@qgsfunction(args='auto', group='Custom')
def lfb_tree_size(form, nr):

    jsonObject = json.loads(form)
    defaultsize = 1

    if 'baumplot1' in jsonObject and 'baumplot1' in jsonObject['baumplot1']:
        defaultsize = QgsRenderContext().convertMetersToMapUnits(jsonObject['baumplot1']['baumplot1'][nr-1]['bhd'] / 2) # mm

    defaultsize = defaultsize * 100

    return jsonObject['baumplot1']['baumplot1'][nr-1]['bhd'] / 2 / 1000 # defaultsize

# TREE COLOR
def generate_tree_color(model_id):
    r = int(model_id/(256**3))
    g = int(model_id%(256**3)/(256**2))
    b = int(model_id%(256**2)/256)

    return str(r) + ',' + str(g) + ',' + str(b)

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

@qgsfunction(args='auto', group='Custom')
def lfb_tree_generated_color(form, nr):

    jsonObject = json.loads(form)
    default = '0,0,0'

    if 'baumplot1' in jsonObject and 'baumplot1' in jsonObject['baumplot1']:
        icode_ba = jsonObject['baumplot1']['baumplot1'][nr-1]['icode_ba']

        rgb = hsv2rgb(icode_ba / 999, 1, 1) # hue, satuation, light

        return str(rgb[0]) + ',' + str(rgb[1]) + ',' + str(rgb[2])


    return default
@qgsfunction(args='auto', group='Custom')
def lfb_tree_color(form, nr):

    jsonObject = json.loads(form)
    default = '0,0,0'

    if 'baumplot1' in jsonObject and 'baumplot1' in jsonObject['baumplot1']:

        icode_ba = jsonObject['baumplot1']['baumplot1'][nr-1]['icode_ba']
        if icode_ba == 200: # Birke = 200 = 252,178,252
            return '252,178,252'
        elif icode_ba == 100: # Buche = 100 = 204,254,100
            return '204,254,100'
        elif icode_ba == 40: # Douglasie = 40 = 76,230,132
            return '76,230,132'
        elif icode_ba == 110 or icode_ba == 111 or icode_ba == 112: # Eiche = 110 & 111 = 252,250,156
            return '252,250,156'
        elif icode_ba == 921: # Lärche = ?? = 244,166,164
            return '244,166,164'
        elif icode_ba == 210: # Erle = ?? = 180,250,252
            return '180,250,252'
        elif icode_ba == 120: # Esche = ?? = 159,120,36
            return '159,120,36'
        elif icode_ba == 10: # Fichte = ?? = 188,190,188
            return '188,190,188'
        elif icode_ba == 20: # Kiefer = 20 = 244,166,164
            return '244,166,164'
        else:
            return '228,206,76'

    return default

# Landmarke Label
@qgsfunction(args='auto', group='Custom')
def lfb_label_landmarke(form, nr):

    jsonObject = json.loads(form)
    default = 'not set'

    if 'landmarken1' in jsonObject and 'landmarken1' in jsonObject['landmarken1']:
        default = jsonObject['landmarken1']['landmarken1'][nr-1]['landmarken']
        default += ', ' + str(jsonObject['landmarken1']['landmarken1'][nr-1]['azimut']) + ' gon'

    return default

@qgsfunction(args='auto', group='Custom')
def lfb_landmarken(form):

    jsonObject = json.loads(form)

    trees = []

    if 'landmarken1' in jsonObject and 'landmarken1' in jsonObject['landmarken1']:
        for tree in jsonObject['landmarken1']['landmarken1']:

            trees.append({
                'azimuth': math.radians(tree['azimut'] * 360 / 400),
                'distance': tree['distanz'] / 100 , # Zentimeter # QgsRenderContext().convertMetersToMapUnits(tree['distanz'] / 100)
                'title': tree['landmarken'], # Millimeter
            })

    return trees




# DEPRECATED
@qgsfunction(args='auto', group='Custom')
def lfb_tree_diameter(f):

    attrs = f.attributes()


    return [1 , 1]

@qgsfunction(args='auto', group='Custom')
def lfb_tree_color2(x, y, id, attributes):


    if 'form' not in attributes:
        return '#ff00ff'

    jsonObject = json.loads(attributes['form'])

    trees = []

    if 'baumplot1' in jsonObject and 'baumplot1' in jsonObject['baumplot1']:
        for tree in jsonObject['baumplot1']['baumplot1']:

            trees.append({
                'azimuth': math.radians(tree['azimut'] * 360 / 400),
                'distance': QgsRenderContext().convertMetersToMapUnits(tree['distanz']) / 100, # Zentimeter
                'diameter': QgsRenderContext().convertMetersToMapUnits(tree['bhd']) * 0.001, # Millimeter
            })





    return '#ff00ff'



@qgsfunction(args='auto', group='Custom')
def lfb_baumplot_length(form, feature, parent):

    jsonObject = json.loads(form)

    if 'baumplot1' in jsonObject:
        elementCount = len(jsonObject['baumplot1']['baumplot1'])
        return elementCount - 1

    return 0

@qgsfunction(args='auto', group='Custom')
def trees_by_azimuth_distance(form, idx, feature, parent, context):

    jsonObject = json.loads(form)
    element = jsonObject['baumplot1']['baumplot1'][int(idx)]



#https://gis.stackexchange.com/questions/402064/qgis-label-expression-to-print-keyvalue-from-a-list-of-dictionaries-coming-f
#https://gis.stackexchange.com/questions/268958/working-with-complex-json-attributes-in-qgis

    # https://qgis.org/pyqgis/3.0/core/Point/QgsPoint.html#qgis.core.QgsPoint.project


    geom = feature.geometry()
    pt = geom.asPoint()

#https://gis.stackexchange.com/questions/393905/how-to-convert-a-symbol-size-in-millimeter-into-that-in-meter-by-pyqgis
    distance = QgsRenderContext().convertMetersToMapUnits(element['distanz']) / 100 # Zentimeter
    azimuth = element['azimut'] # gon

    pt2 = pt.project(distance, azimuth)

    return QgsGeometry.fromPointXY(QgsPointXY(pt2.x(), pt2.y()))