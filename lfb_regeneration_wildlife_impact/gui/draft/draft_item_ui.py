# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gerrit/Sites/lfb/lfb-regeneration_wildlife_impact_monitoring/lfb_regeneration_wildlife_impact/gui/draft/draft_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(757, 114)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lfbDraftModifiedByBtn = QtWidgets.QLabel(Form)
        self.lfbDraftModifiedByBtn.setObjectName("lfbDraftModifiedByBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lfbDraftModifiedByBtn)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lfbDraftModifiedBtn = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lfbDraftModifiedBtn.sizePolicy().hasHeightForWidth())
        self.lfbDraftModifiedBtn.setSizePolicy(sizePolicy)
        self.lfbDraftModifiedBtn.setObjectName("lfbDraftModifiedBtn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lfbDraftModifiedBtn)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lfbDraftAufnahmetruppLabel = QtWidgets.QLabel(Form)
        self.lfbDraftAufnahmetruppLabel.setObjectName("lfbDraftAufnahmetruppLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lfbDraftAufnahmetruppLabel)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lfbDraftWorkflowLabel = QtWidgets.QLabel(Form)
        self.lfbDraftWorkflowLabel.setObjectName("lfbDraftWorkflowLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lfbDraftWorkflowLabel)
        self.horizontalLayout_5.addLayout(self.formLayout)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lfbDraftIconBtn = QtWidgets.QPushButton(Form)
        self.lfbDraftIconBtn.setObjectName("lfbDraftIconBtn")
        self.horizontalLayout_4.addWidget(self.lfbDraftIconBtn)
        self.lfbDraftIconRemoveBtn = QtWidgets.QPushButton(Form)
        self.lfbDraftIconRemoveBtn.setObjectName("lfbDraftIconRemoveBtn")
        self.horizontalLayout_4.addWidget(self.lfbDraftIconRemoveBtn)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Modified:"))
        self.lfbDraftModifiedByBtn.setText(_translate("Form", "-"))
        self.label_4.setText(_translate("Form", "Created:"))
        self.lfbDraftModifiedBtn.setText(_translate("Form", "-"))
        self.label_2.setText(_translate("Form", "Aufnahmetrupp:"))
        self.lfbDraftAufnahmetruppLabel.setText(_translate("Form", "-"))
        self.label_3.setText(_translate("Form", "Workflow:"))
        self.lfbDraftWorkflowLabel.setText(_translate("Form", "-"))
        self.lfbDraftIconBtn.setText(_translate("Form", "Datenaufnahme fortführen"))
        self.lfbDraftIconRemoveBtn.setText(_translate("Form", "Löschen"))
