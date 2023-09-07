# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LfbRegenerationWildlifeImpact
                                 A QGIS plugin
 FIM
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-05-08
        copyright            : (C) 2023 by Grünecho
        email                : support@grunecho.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LfbRegenerationWildlifeImpact class from file LfbRegenerationWildlifeImpact.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """

    installJsonschema()

    from .fim import Fim
    return Fim(iface)


def installJsonschema():

    try:
        import jsonschema
    except ModuleNotFoundError:
        import subprocess

        subprocess.check_call(["python", "-m", "pip", "install", "jsonschema"])