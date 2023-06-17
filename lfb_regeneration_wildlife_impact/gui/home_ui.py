# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gerrit/Sites/lfb/lfb-regeneration_wildlife_impact_monitoring/lfb_regeneration_wildlife_impact/gui/home.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(815, 522)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.lfbHeadline = QtWidgets.QWidget(Form)
        self.lfbHeadline.setObjectName("lfbHeadline")
        self._2 = QtWidgets.QVBoxLayout(self.lfbHeadline)
        self._2.setContentsMargins(-1, 50, -1, 10)
        self._2.setObjectName("_2")
        self.label = QtWidgets.QLabel(self.lfbHeadline)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self._2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.lfbHeadline)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self._2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 20, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lfbNewEntry = QtWidgets.QPushButton(self.lfbHeadline)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lfbNewEntry.setFont(font)
        self.lfbNewEntry.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lfbNewEntry.setStyleSheet("QPushButton{\n"
"    border-radius: 20px;\n"
"    border: 2px solid #333;\n"
"    color: #555;\n"
"    margin: 10px 0px 0px;\n"
"    padding: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: yellow;\n"
"}\n"
"QPushButton:enabled{\n"
"    border-radius: 20px;\n"
"    border: 2px solid #fff;\n"
"    background-color: green;\n"
"    color: #fff;\n"
"}")
        self.lfbNewEntry.setObjectName("lfbNewEntry")
        self.horizontalLayout.addWidget(self.lfbNewEntry)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self._2.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.lfbHeadline, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Verbiss und Wildtier Monitoring"))
        self.label_2.setText(_translate("Form", "Überwachung des Verjüngungszustandes durch die Aufnahme von Naturaldaten."))
        self.lfbNewEntry.setText(_translate("Form", "NEUER EINTRAG"))