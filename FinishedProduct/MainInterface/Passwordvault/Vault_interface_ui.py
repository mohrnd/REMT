# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vault_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QTableWidgetItem,
    QWidget)

from qfluentwidgets import (LineEdit, PasswordLineEdit, PrimaryPushButton, PushButton,
    TableWidget, TextEdit)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(813, 768)
        self.MasterPassword_input = PasswordLineEdit(Form)
        self.MasterPassword_input.setObjectName(u"MasterPassword_input")
        self.MasterPassword_input.setGeometry(QRect(10, 20, 791, 33))
        self.MainTable = TableWidget(Form)
        if (self.MainTable.columnCount() < 3):
            self.MainTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.MainTable.setObjectName(u"MainTable")
        self.MainTable.setGeometry(QRect(10, 70, 791, 391))
        self.FetchPasswords_Button = PrimaryPushButton(Form)
        self.FetchPasswords_Button.setObjectName(u"FetchPasswords_Button")
        self.FetchPasswords_Button.setGeometry(QRect(10, 490, 791, 32))
        self.output_TextEdit = TextEdit(Form)
        self.output_TextEdit.setObjectName(u"output_TextEdit")
        self.output_TextEdit.setGeometry(QRect(10, 540, 791, 181))
        self.Flush_TextEdit = PushButton(Form)
        self.Flush_TextEdit.setObjectName(u"Flush_TextEdit")
        self.Flush_TextEdit.setGeometry(QRect(700, 730, 102, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.MainTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Machine name", None));
        ___qtablewidgetitem1 = self.MainTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"IP address", None));
        ___qtablewidgetitem2 = self.MainTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Action", None));
        self.FetchPasswords_Button.setText(QCoreApplication.translate("Form", u"Fetch passwords", None))
        self.Flush_TextEdit.setText(QCoreApplication.translate("Form", u"Flush", None))
    # retranslateUi

