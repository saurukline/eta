# -*- coding: utf-8 -*-
"""
/***************************************************************************
 eta
                                 A QGIS plugin
 Gerenciamento de ETA
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-02-09
        copyright            : (C) 2022 by Iuri Carvalho / VIX
        email                : iuri@vixsystem.com.br
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
    """Load eta class from file eta.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .eta import eta
    return eta(iface)
