from qgis.PyQt.QtWidgets import (QWidget)

from PyQt5 import QtWidgets


class GnssPluginWidget(QtWidgets.QWidget):
  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
  
        self.textbox = QtWidgets.QLineEdit()
        self.echo_label = QtWidgets.QLabel('')
        self.echo_label2 = QtWidgets.QLabel('')
        self.echo_label3 = QtWidgets.QLabel('')
  
        self.textbox.textChanged.connect(self.textbox_text_changed)
  
        # PySide2.QtWidgets.QGridLayout.addWidget(arg__1, row, column, rowSpan, columnSpan[, alignment=Qt.Alignment()])
        self.layout.addWidget(self.textbox, 0, 0)
        self.layout.addWidget(self.echo_label, 1, 0)
        self.layout.addWidget(self.echo_label2, 2, 0)
        self.layout.addWidget(self.echo_label3, 3, 0)
  
    def textbox_text_changed(self):
        self.echo_label.setText(self.textbox.text())
        self.echo_label2.setText(self.textbox.text())
        self.echo_label3.setText(self.textbox.text())