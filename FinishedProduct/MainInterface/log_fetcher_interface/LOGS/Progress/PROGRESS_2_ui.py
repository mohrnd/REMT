# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PROGRESS_2.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

from qfluentwidgets import (LineEdit, PasswordLineEdit, PrimaryPushButton, PushButton,
    StateToolTip, TextEdit)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(470, 524)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.configprogress_startFetching = PrimaryPushButton(self.centralwidget)
        self.configprogress_startFetching.setObjectName(u"configprogress_startFetching")
        self.configprogress_startFetching.setGeometry(QRect(300, 430, 161, 51))
        self.StateToolTip = StateToolTip(self.centralwidget)
        self.StateToolTip.setObjectName(u"StateToolTip")
        self.StateToolTip.setEnabled(True)
        self.StateToolTip.setGeometry(QRect(10, 430, 256, 51))
        self.configprogress_TextEdit = TextEdit(self.centralwidget)
        self.configprogress_TextEdit.setObjectName(u"configprogress_TextEdit")
        self.configprogress_TextEdit.setGeometry(QRect(10, 0, 451, 381))
        self.Masterpasswordinput = PasswordLineEdit(self.centralwidget)
        self.Masterpasswordinput.setObjectName(u"Masterpasswordinput")
        self.Masterpasswordinput.setGeometry(QRect(10, 390, 451, 33))
        self.configprogress_exit = PrimaryPushButton(self.centralwidget)
        self.configprogress_exit.setObjectName(u"configprogress_exit")
        self.configprogress_exit.setGeometry(QRect(300, 430, 161, 51))
        self.configprogress_exit.setCheckable(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 470, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.configprogress_startFetching.setText(QCoreApplication.translate("MainWindow", u"Start Fetching", None))
        self.Masterpasswordinput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please insert your master password", None))
        self.configprogress_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

