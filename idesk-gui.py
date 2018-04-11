# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'idesk_v2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import sys


class UiForm(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(704, 638)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.title)
        self.subtitle = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setItalic(True)
        self.subtitle.setFont(font)
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle.setObjectName("subtitle")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.subtitle)
        self.headerbreak = QtWidgets.QFrame(Form)
        self.headerbreak.setFrameShape(QtWidgets.QFrame.HLine)
        self.headerbreak.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.headerbreak.setObjectName("headerbreak")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.headerbreak)
        self.captiontitle = QtWidgets.QLabel(Form)
        self.captiontitle.setObjectName("captiontitle")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.captiontitle)
        self.captionEdit = QtWidgets.QLineEdit(Form)
        self.captionEdit.setObjectName("captionEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.captionEdit)
        self.tooltip = QtWidgets.QLabel(Form)
        self.tooltip.setObjectName("tooltip")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.tooltip)
        self.toolTipEdit = QtWidgets.QLineEdit(Form)
        self.toolTipEdit.setObjectName("toolTipEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.toolTipEdit)
        self.command = QtWidgets.QLabel(Form)
        self.command.setObjectName("command")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.command)
        self.commandEdit = QtWidgets.QLineEdit(Form)
        self.commandEdit.setObjectName("commandEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.commandEdit)
        self.icon = QtWidgets.QLabel(Form)
        self.icon.setObjectName("icon")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.icon)
        self.iconEdit = QtWidgets.QLineEdit(Form)
        self.iconEdit.setObjectName("iconEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.iconEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.info = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.info.setFont(font)
        self.info.setObjectName("info")
        self.horizontalLayout.addWidget(self.info)
        self.submit = QtWidgets.QPushButton(Form)
        self.submit.setObjectName("submit")
        self.horizontalLayout.addWidget(self.submit)
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "Idesk"))
        self.subtitle.setText(_translate("Form", "gui configuration tool"))
        self.captiontitle.setText(_translate("Form", "Caption:"))
        self.tooltip.setText(_translate("Form", "Tooltip:"))
        self.command.setText(_translate("Form", "Command:"))
        self.icon.setText(_translate("Form", "Icon:"))
        self.info.setText(_translate("Form", "(Gets saved into .idesktop as caption value.lnc)"))
        self.submit.setText(_translate("Form", "Submit"))
        self.cancel.setText(_translate("Form", "Cancel"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UiForm()
    ex.show()
    sys.exit(app.exec_())
