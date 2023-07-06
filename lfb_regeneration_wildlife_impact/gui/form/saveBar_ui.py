# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gerrit/Sites/lfb/lfb-regeneration_wildlife_impact_monitoring/lfb_regeneration_wildlife_impact/gui/form/saveBar.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lfbSaveBar(object):
    def setupUi(self, lfbSaveBar):
        lfbSaveBar.setObjectName("lfbSaveBar")
        lfbSaveBar.resize(917, 492)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(lfbSaveBar.sizePolicy().hasHeightForWidth())
        lfbSaveBar.setSizePolicy(sizePolicy)
        lfbSaveBar.setStyleSheet("Qwidget#lfbSaveBar{\n"
"    background-color: #222;\n"
"    color: #fff;\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(lfbSaveBar)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lfbProgressBar = QtWidgets.QProgressBar(lfbSaveBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbProgressBar.sizePolicy().hasHeightForWidth())
        self.lfbProgressBar.setSizePolicy(sizePolicy)
        self.lfbProgressBar.setMinimumSize(QtCore.QSize(0, 2))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.lfbProgressBar.setFont(font)
        self.lfbProgressBar.setAutoFillBackground(False)
        self.lfbProgressBar.setStyleSheet("QProgressBar::chunk{\n"
"    background-color: red;\n"
"    \n"
"}\n"
"QProgressBar{\n"
"    color:transparent;\n"
"    border:none;\n"
"    margin:0;\n"
"    height:2px;\n"
"    background-color: #222;\n"
"    color: #fff;\n"
"}")
        self.lfbProgressBar.setProperty("value", 24)
        self.lfbProgressBar.setObjectName("lfbProgressBar")
        self.gridLayout.addWidget(self.lfbProgressBar, 1, 0, 1, 1)
        self.lfbActionRow = QtWidgets.QWidget(lfbSaveBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbActionRow.sizePolicy().hasHeightForWidth())
        self.lfbActionRow.setSizePolicy(sizePolicy)
        self.lfbActionRow.setMinimumSize(QtCore.QSize(0, 0))
        self.lfbActionRow.setMaximumSize(QtCore.QSize(16777215, 100))
        self.lfbActionRow.setAutoFillBackground(False)
        self.lfbActionRow.setStyleSheet("background-color: #222;\n"
"color: #fff;\n"
"padding:10px;\n"
"margin:0px;")
        self.lfbActionRow.setObjectName("lfbActionRow")
        self.lfbsabeLayout = QtWidgets.QHBoxLayout(self.lfbActionRow)
        self.lfbsabeLayout.setContentsMargins(0, 5, 0, 5)
        self.lfbsabeLayout.setSpacing(0)
        self.lfbsabeLayout.setObjectName("lfbsabeLayout")
        self.lfbHomeBtn = QtWidgets.QToolButton(self.lfbActionRow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lfbHomeBtn.setFont(font)
        self.lfbHomeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lfbHomeBtn.setStyleSheet("QToolButton{\n"
"    border-radius: 20px;\n"
"    border: 2px solid #333;\n"
"    color: #555;\n"
"    margin: 5px;\n"
"}\n"
"QToolButton:enabled{\n"
"    background-color: green;\n"
"    color: #fff;\n"
"}")
        self.lfbHomeBtn.setObjectName("lfbHomeBtn")
        self.lfbsabeLayout.addWidget(self.lfbHomeBtn)
        self.lfbDevBtn = QtWidgets.QPushButton(self.lfbActionRow)
        self.lfbDevBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lfbDevBtn.setStyleSheet("color: #fff;\n"
"background-color: #333;")
        self.lfbDevBtn.setObjectName("lfbDevBtn")
        self.lfbsabeLayout.addWidget(self.lfbDevBtn)
        self.lfbSchemaBtn = QtWidgets.QPushButton(self.lfbActionRow)
        self.lfbSchemaBtn.setObjectName("lfbSchemaBtn")
        self.lfbsabeLayout.addWidget(self.lfbSchemaBtn)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(15, -1, -1, -1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lfbId = QtWidgets.QLabel(self.lfbActionRow)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lfbId.setFont(font)
        self.lfbId.setStyleSheet("padding:0;")
        self.lfbId.setObjectName("lfbId")
        self.horizontalLayout.addWidget(self.lfbId)
        self.lfbFokusFeature = QtWidgets.QToolButton(self.lfbActionRow)
        self.lfbFokusFeature.setStyleSheet("background: #222222;\n"
"padding: 5px;")
        self.lfbFokusFeature.setObjectName("lfbFokusFeature")
        self.horizontalLayout.addWidget(self.lfbFokusFeature)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.lfbPluginVersion = QtWidgets.QLabel(self.lfbActionRow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbPluginVersion.sizePolicy().hasHeightForWidth())
        self.lfbPluginVersion.setSizePolicy(sizePolicy)
        self.lfbPluginVersion.setStyleSheet("padding:0;")
        self.lfbPluginVersion.setObjectName("lfbPluginVersion")
        self.verticalLayout_2.addWidget(self.lfbPluginVersion)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.lfbsabeLayout.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lfbsabeLayout.addItem(spacerItem2)
        self.lfbErrorsLayout = QtWidgets.QHBoxLayout()
        self.lfbErrorsLayout.setObjectName("lfbErrorsLayout")
        self.lfbsabeLayout.addLayout(self.lfbErrorsLayout)
        self.lfbErrorDialogBtn = QtWidgets.QPushButton(self.lfbActionRow)
        self.lfbErrorDialogBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lfbErrorDialogBtn.setStyleSheet("color: red;\n"
"margin:5px 0 10px;\n"
"padding:0;\n"
"border:none;\n"
"background: transparent;")
        self.lfbErrorDialogBtn.setObjectName("lfbErrorDialogBtn")
        self.lfbsabeLayout.addWidget(self.lfbErrorDialogBtn)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lfbSaveBtn = QtWidgets.QPushButton(self.lfbActionRow)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lfbSaveBtn.setFont(font)
        self.lfbSaveBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lfbSaveBtn.setStyleSheet("QPushButton{\n"
"    border-radius: 20px;\n"
"    border: 2px solid #333;\n"
"    color: #555;\n"
"    margin: 2px;\n"
"}\n"
"QPushButton:enabled{\n"
"    border-radius: 20px;\n"
"    border: 2px solid #fff;\n"
"    background-color: green;\n"
"    color: #fff;\n"
"}")
        self.lfbSaveBtn.setObjectName("lfbSaveBtn")
        self.verticalLayout.addWidget(self.lfbSaveBtn)
        self.lfbsabeLayout.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.lfbActionRow, 2, 0, 1, 1)

        self.retranslateUi(lfbSaveBar)
        QtCore.QMetaObject.connectSlotsByName(lfbSaveBar)

    def retranslateUi(self, lfbSaveBar):
        _translate = QtCore.QCoreApplication.translate
        lfbSaveBar.setWindowTitle(_translate("lfbSaveBar", "Form"))
        self.lfbHomeBtn.setText(_translate("lfbSaveBar", "<"))
        self.lfbDevBtn.setText(_translate("lfbSaveBar", "DEV"))
        self.lfbSchemaBtn.setText(_translate("lfbSaveBar", "SCHEMA"))
        self.lfbId.setText(_translate("lfbSaveBar", "TextLabel"))
        self.lfbFokusFeature.setText(_translate("lfbSaveBar", "Karte auf Punkt zentrieren"))
        self.lfbPluginVersion.setText(_translate("lfbSaveBar", "Version"))
        self.lfbErrorDialogBtn.setText(_translate("lfbSaveBar", "Error Text"))
        self.lfbSaveBtn.setText(_translate("lfbSaveBar", "FERTIG"))
