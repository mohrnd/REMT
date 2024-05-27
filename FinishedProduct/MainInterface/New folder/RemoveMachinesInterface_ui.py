# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemoveMachinesInterface.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QTableWidgetItem, QWidget)

from qfluentwidgets import (PrimaryPushButton, PushButton, TableWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(813, 768)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 771, 731))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MainTable = TableWidget(self.gridLayoutWidget)
        if (self.MainTable.columnCount() < 3):
            self.MainTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.MainTable.setObjectName(u"MainTable")

        self.gridLayout.addWidget(self.MainTable, 0, 0, 1, 1)

        self.RemoveMachinesButton = PrimaryPushButton(self.gridLayoutWidget)
        self.RemoveMachinesButton.setObjectName(u"RemoveMachinesButton")

        self.gridLayout.addWidget(self.RemoveMachinesButton, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.MainTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Machine Name", None));
        ___qtablewidgetitem1 = self.MainTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"IP address", None));
        ___qtablewidgetitem2 = self.MainTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Action", None));
        self.RemoveMachinesButton.setText(QCoreApplication.translate("Form", u"Remove selected machines", None))
    # retranslateUi

