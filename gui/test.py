from qgis.core import *
from qgis.gui import *

app = QgsApplication([], True)
app.initQgis()

print(app.showSettings())

osmUrl = 'type=xyz&url=http://a.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0&crs=EPSG3857'
rlayer = QgsRasterLayer(osmUrl, 'OpenStreetMap', 'wms')

canvas = QgsMapCanvas()
canvas.setExtent(rlayer.extent())
canvas.setLayers([rlayer])
canvas.show()

app.exec_()  

app.exitQgis()