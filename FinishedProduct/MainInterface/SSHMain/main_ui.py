# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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

from qfluentwidgets import (PrimaryPushButton, PushButton, TableWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(579, 768)
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
        self.MainTable.setGeometry(QRect(10, 50, 561, 491))
        self.OpenMultiSSH = PrimaryPushButton(Form)
        self.OpenMultiSSH.setObjectName(u"OpenMultiSSH")
        self.OpenMultiSSH.setGeometry(QRect(380, 570, 191, 32))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.MainTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Machine Name", None));
        ___qtablewidgetitem1 = self.MainTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"IP Address", None));
        ___qtablewidgetitem2 = self.MainTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Actions", None));
        self.OpenMultiSSH.setText(QCoreApplication.translate("Form", u"Open Multi-SSH window", None))
    # retranslateUi

