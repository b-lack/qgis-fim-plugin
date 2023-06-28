# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gerrit/Sites/lfb/lfb-regeneration_wildlife_impact_monitoring/lfb_regeneration_wildlife_impact/gui/setup/folder_selection.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 302)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(-1, 50, -1, 50)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 4)
        self.lfbTempAlert = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbTempAlert.sizePolicy().hasHeightForWidth())
        self.lfbTempAlert.setSizePolicy(sizePolicy)
        self.lfbTempAlert.setStyleSheet("color: orange;")
        self.lfbTempAlert.setAlignment(QtCore.Qt.AlignCenter)
        self.lfbTempAlert.setObjectName("lfbTempAlert")
        self.gridLayout.addWidget(self.lfbTempAlert, 1, 2, 1, 2)
        self.lfbFolderSelection = gui.QgsFileWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbFolderSelection.sizePolicy().hasHeightForWidth())
        self.lfbFolderSelection.setSizePolicy(sizePolicy)
        self.lfbFolderSelection.setFullUrl(False)
        self.lfbFolderSelection.setStorageMode(gui.QgsFileWidget.GetDirectory)
        self.lfbFolderSelection.setOptions(QtWidgets.QFileDialog.ReadOnly|QtWidgets.QFileDialog.ShowDirsOnly)
        self.lfbFolderSelection.setObjectName("lfbFolderSelection")
        self.gridLayout.addWidget(self.lfbFolderSelection, 2, 1, 1, 4)
        self.lfbFolderSelectionError = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbFolderSelectionError.sizePolicy().hasHeightForWidth())
        self.lfbFolderSelectionError.setSizePolicy(sizePolicy)
        self.lfbFolderSelectionError.setObjectName("lfbFolderSelectionError")
        self.gridLayout.addWidget(self.lfbFolderSelectionError, 3, 1, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Speicherort"))
        self.lfbTempAlert.setText(_translate("Form", "!! Deine Daten werden aktuell nur temporär gespeichert !!"))
        self.lfbFolderSelectionError.setText(_translate("Form", "Select a folder you want to save data in."))
from qgis import gui
