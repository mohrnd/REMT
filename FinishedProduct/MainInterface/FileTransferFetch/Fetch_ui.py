# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Fetch.ui'
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

from qfluentwidgets import (LineEdit, PrimaryPushButton, PushButton, StrongBodyLabel,
    TableWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(579, 768)
        self.MainTable = TableWidget(Frame)
        if (self.MainTable.columnCount() < 3):
            self.MainTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.MainTable.setObjectName(u"MainTable")
        self.MainTable.setGeometry(QRect(9, 190, 561, 431))
        self.Deploy = PrimaryPushButton(Frame)
        self.Deploy.setObjectName(u"Deploy")
        self.Deploy.setGeometry(QRect(410, 650, 161, 32))
        self.Localpath = LineEdit(Frame)
        self.Localpath.setObjectName(u"Localpath")
        self.Localpath.setGeometry(QRect(9, 50, 431, 33))
        self.Broswse = PushButton(Frame)
        self.Broswse.setObjectName(u"Broswse")
        self.Broswse.setGeometry(QRect(449, 50, 121, 32))
        self.Title1 = StrongBodyLabel(Frame)
        self.Title1.setObjectName(u"Title1")
        self.Title1.setGeometry(QRect(9, 20, 131, 19))
        self.LineEdit = LineEdit(Frame)
        self.LineEdit.setObjectName(u"LineEdit")
        self.LineEdit.setGeometry(QRect(9, 100, 431, 33))
        self.PushButton = PushButton(Frame)
        self.PushButton.setObjectName(u"PushButton")
        self.PushButton.setGeometry(QRect(450, 100, 121, 32))
        self.StrongBodyLabel = StrongBodyLabel(Frame)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setGeometry(QRect(10, 170, 111, 19))

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Form", None))
        ___qtablewidgetitem = self.MainTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Frame", u"Machine Name", None));
        ___qtablewidgetitem1 = self.MainTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Frame", u"IP Address", None));
        ___qtablewidgetitem2 = self.MainTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Frame", u"Select", None));
        self.Deploy.setText(QCoreApplication.translate("Frame", u"Fetch", None))
        self.Localpath.setPlaceholderText(QCoreApplication.translate("Frame", u"Local path", None))
        self.Broswse.setText(QCoreApplication.translate("Frame", u"Browse", None))
        self.Title1.setText(QCoreApplication.translate("Frame", u"Fetch a file/folder:", None))
        self.LineEdit.setPlaceholderText(QCoreApplication.translate("Frame", u"Remote path", None))
        self.PushButton.setText(QCoreApplication.translate("Frame", u"Verify existance", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Frame", u"Machines online:", None))
    # retranslateUi

