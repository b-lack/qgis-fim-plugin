# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gerrit/Sites/lfb/lfb-regeneration_wildlife_impact_monitoring/lfb_regeneration_wildlife_impact/gui/form/views/object_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(719, 540)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.lfbObjectGroup = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lfbObjectGroup.setFont(font)
        self.lfbObjectGroup.setStyleSheet("QGroupBox#lfbObjectGroup{\n"
"    background: rgba(0,0,0,0.1);\n"
"border-radius: 10px;\n"
"}")
        self.lfbObjectGroup.setObjectName("lfbObjectGroup")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.lfbObjectGroup)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lfbFormObject = QtWidgets.QGridLayout()
        self.lfbFormObject.setObjectName("lfbFormObject")
        self.gridLayout_3.addLayout(self.lfbFormObject, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.lfbObjectGroup, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lfbObjectGroup.setTitle(_translate("Form", "GroupBox"))
