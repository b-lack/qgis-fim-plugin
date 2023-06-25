# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gerrit/Sites/lfb/lfb-regeneration_wildlife_impact_monitoring/lfb_regeneration_wildlife_impact/gui/form/views/tab_default.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(921, 902)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("margin: 10px;\n"
"padding: 10px;\n"
"border-radius: 22px;\n"
"border: 2px solid grey;\n"
"background-color: grey;\n"
"width: 20px;\n"
"height: 20px;")
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.lfbTabScroll = QtWidgets.QScrollArea(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.lfbTabScroll.sizePolicy().hasHeightForWidth())
        self.lfbTabScroll.setSizePolicy(sizePolicy)
        self.lfbTabScroll.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lfbTabScroll.setTabletTracking(True)
        self.lfbTabScroll.setStyleSheet("border:none;")
        self.lfbTabScroll.setLineWidth(0)
        self.lfbTabScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lfbTabScroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lfbTabScroll.setWidgetResizable(True)
        self.lfbTabScroll.setObjectName("lfbTabScroll")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 385, 902))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("QWidget{\n"
"    border: 2px solid grey;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"    background-color: rgba(0,0,0,0.1);\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lfbObjectDescription = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbObjectDescription.sizePolicy().hasHeightForWidth())
        self.lfbObjectDescription.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lfbObjectDescription.setFont(font)
        self.lfbObjectDescription.setStyleSheet("border:none;\n"
"background-color: transparent;")
        self.lfbObjectDescription.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lfbObjectDescription.setWordWrap(True)
        self.lfbObjectDescription.setObjectName("lfbObjectDescription")
        self.horizontalLayout.addWidget(self.lfbObjectDescription)
        self.verticalLayout.addWidget(self.widget)
        self.lfbTabLayout = QtWidgets.QFormLayout()
        self.lfbTabLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.lfbTabLayout.setContentsMargins(20, 20, 20, -1)
        self.lfbTabLayout.setSpacing(0)
        self.lfbTabLayout.setObjectName("lfbTabLayout")
        self.verticalLayout.addLayout(self.lfbTabLayout)
        self.lfbTabScroll.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.lfbTabScroll)
        self.toolButton = QtWidgets.QToolButton(Form)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("margin: 10px;\n"
"padding: 10px;\n"
"border-radius: 22px;\n"
"border: 2px solid grey;\n"
"background-color: grey;\n"
"width: 20px;\n"
"height: 20px;")
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.lfbInfoBox = QtWidgets.QTextBrowser(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbInfoBox.sizePolicy().hasHeightForWidth())
        self.lfbInfoBox.setSizePolicy(sizePolicy)
        self.lfbInfoBox.setMinimumSize(QtCore.QSize(200, 0))
        self.lfbInfoBox.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lfbInfoBox.setObjectName("lfbInfoBox")
        self.horizontalLayout_2.addWidget(self.lfbInfoBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton_2.setText(_translate("Form", "<"))
        self.lfbObjectDescription.setText(_translate("Form", "TextLabel"))
        self.toolButton.setText(_translate("Form", ">"))
        self.lfbInfoBox.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying __init__.py</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying lfb_regeneration_wildlife_impact.py</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying resources.py</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying metadata.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of i18n to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of state to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of gui to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of schema to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of assets to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying help/build/html to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact/helpCopying __init__.py</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying lfb_regeneration_wildlife_impact.py</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying resources.py</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying metadata.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of i18n to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of state to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of gui to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of schema to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of assets to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying help/build/html to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact/helpCopying __init__.py</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying lfb_regeneration_wildlife_impact.py</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying resources.py</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying metadata.txt</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of i18n to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of state to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of gui to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of schema to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying contents of assets to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copying help/build/html to /home/gerrit/.local/share/QGIS/QGIS3/profiles/default/python/plugins/lfb_regeneration_wildlife_impact/help</p></body></html>"))
