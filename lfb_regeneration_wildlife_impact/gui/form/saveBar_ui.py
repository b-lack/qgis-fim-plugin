# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gerrit/Sites/lfb/lfb-regeneration_wildlife_impact_monitoring/lfb_regeneration_wildlife_impact/gui/form/saveBar.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(917, 492)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("background-color: #222;\n"
"color: #fff;")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.lfbProgressBar = QtWidgets.QProgressBar(Form)
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
        self.lfbActionRow = QtWidgets.QWidget(Form)
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
        self.verticalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
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
"padding: 0;")
        self.lfbFokusFeature.setObjectName("lfbFokusFeature")
        self.horizontalLayout.addWidget(self.lfbFokusFeature)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.lfbProcessInfo = QtWidgets.QLabel(self.lfbActionRow)
        self.lfbProcessInfo.setStyleSheet("padding:0;")
        self.lfbProcessInfo.setText("")
        self.lfbProcessInfo.setObjectName("lfbProcessInfo")
        self.verticalLayout_2.addWidget(self.lfbProcessInfo)
        self.lfbsabeLayout.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lfbsabeLayout.addItem(spacerItem)
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lfbHomeBtn.setText(_translate("Form", "<"))
        self.lfbDevBtn.setText(_translate("Form", "DEV"))
        self.lfbSchemaBtn.setText(_translate("Form", "SCHEMA"))
        self.lfbId.setText(_translate("Form", "TextLabel"))
        self.lfbFokusFeature.setText(_translate("Form", "fokus"))
        self.lfbErrorDialogBtn.setText(_translate("Form", "Error Text"))
        self.lfbSaveBtn.setText(_translate("Form", "FERTIG"))
