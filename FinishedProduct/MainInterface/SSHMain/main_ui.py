# Form implementation generated from reading ui file 'c:\Users\dell-5320\Desktop\REMT\FinishedProduct\MainInterface\SSHMain\main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(579, 768)
        self.MainTable = TableWidget(parent=Form)
        self.MainTable.setGeometry(QtCore.QRect(10, 50, 561, 491))
        self.MainTable.setObjectName("MainTable")
        self.MainTable.setColumnCount(3)
        self.MainTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(2, item)
        self.OpenMultiSSH = PrimaryPushButton(parent=Form)
        self.OpenMultiSSH.setGeometry(QtCore.QRect(380, 570, 191, 32))
        self.OpenMultiSSH.setObjectName("OpenMultiSSH")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.MainTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Machine Name"))
        item = self.MainTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "IP Address"))
        item = self.MainTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Actions"))
        self.OpenMultiSSH.setText(_translate("Form", "Open Multi-SSH window"))
from qfluentwidgets import PrimaryPushButton, TableWidget