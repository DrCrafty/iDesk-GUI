# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'idesk_v2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import sys
import subprocess
import os


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
        
        # up to here is the UI display
        # this part is the backend

        self.submit.clicked.connect(self.ok_button) # connected the submit button to the ok_button func
        self.cancel.clicked.connect(self.cancel_button) # connected the submit button to the cancel_button func

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
        self.cancel.setText(_translate("Form", "Quit"))

    def ok_button(self):
        """This button will take the input in the entries (lineEdits) and create a
        file that should be saved in .idesktop"""

        self.caption = self.captionEdit.text()  # this grabs the text in the lineEdits
        self.tooltip = self.toolTipEdit.text()
        self.command = self.commandEdit.text()
        self.icon = self.iconEdit.text()

        from pathlib import Path
        home = (str(Path.home()) + "/.idesktop")

        # check if the file .idesktop exists, if it does append the edit lines and write to the the .idesktop dir
        if (os.path.isdir(home)):
            # build up .lnk file and write it to .idesktop dir
            newFile = ()
            f = open(home + "/" + self.caption + '.lnk', 'w')
            f.write("table Icon\n  Caption: " + self.caption)
            f.write("\n  ToolTip.Caption: " + self.tooltip)
            f.write("\n  Icon: " + self.icon)
            f.write("\n  Command: " + self.command)
            f.write("\n  Width: 48 \n  Height: 48")
            f.write("\n  X: 100 \n  Y: 100")
            f.write("\nend")
            f.close
            #
            # this shouldn't just kill the app we need to retart the app
            # I can't remember how but we can research it
            #
            self.close()
            subprocess.call("python" + " idesk-gui.py", shell=True)

        else:
            #
            # it would be cool if this would appear in a notication box on the app
            #
            print("File does not exist, Please create a .idesktop directory in home")
            # for now it prints this message but it should change the text of a label
            sys.exit()

    def cancel_button(self):
        """exits the program"""
        sys.exit()

    # function no longer needed
    # def find_idesktop_dir(self):
        """this function will find the .idesktop directory. Only works on linux"""
        # command = ["locate", ".idesktop"]

        # output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
        # output = output.decode()

        # search_results = output.split('\n')

        # if search_results:
        #     return search_results[0]
        # else:
        #     return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UiForm()
    ex.show()
    sys.exit(app.exec_())