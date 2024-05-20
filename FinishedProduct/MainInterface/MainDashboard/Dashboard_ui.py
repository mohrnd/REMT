# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QSizePolicy,
    QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CardWidget, ElevatedCardWidget, SimpleCardWidget,
    SubtitleLabel, TableWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(806, 768)
        icon = QIcon()
        icon.addFile(u"../../../FinishedProduct/MainInterface/black.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.CardWidget = CardWidget(Form)
        self.CardWidget.setObjectName(u"CardWidget")
        self.CardWidget.setGeometry(QRect(10, 10, 791, 221))
        self.verticalLayoutWidget = QWidget(self.CardWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 181, 221))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ElevatedCardWidget = ElevatedCardWidget(self.verticalLayoutWidget)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        self.verticalLayoutWidget_2 = QWidget(self.ElevatedCardWidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 30, 181, 51))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.TotalMachines = SubtitleLabel(self.verticalLayoutWidget_2)
        self.TotalMachines.setObjectName(u"TotalMachines")

        self.verticalLayout_3.addWidget(self.TotalMachines, 0, Qt.AlignHCenter)

        self.BodyLabel_3 = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        self.BodyLabel_3.setGeometry(QRect(10, 10, 63, 19))

        self.verticalLayout.addWidget(self.ElevatedCardWidget)

        self.ElevatedCardWidget_2 = ElevatedCardWidget(self.verticalLayoutWidget)
        self.ElevatedCardWidget_2.setObjectName(u"ElevatedCardWidget_2")
        self.verticalLayoutWidget_3 = QWidget(self.ElevatedCardWidget_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 30, 181, 51))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.MachinesOnline = SubtitleLabel(self.verticalLayoutWidget_3)
        self.MachinesOnline.setObjectName(u"MachinesOnline")

        self.verticalLayout_4.addWidget(self.MachinesOnline, 0, Qt.AlignHCenter)

        self.BodyLabel_4 = BodyLabel(self.ElevatedCardWidget_2)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")
        self.BodyLabel_4.setGeometry(QRect(10, 10, 63, 19))

        self.verticalLayout.addWidget(self.ElevatedCardWidget_2)

        self.horizontalLayoutWidget = QWidget(self.CardWidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(190, 0, 601, 221))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ElevatedCardWidget_4 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_4.setObjectName(u"ElevatedCardWidget_4")
        self.BodyLabel_6 = BodyLabel(self.ElevatedCardWidget_4)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")
        self.BodyLabel_6.setGeometry(QRect(10, 10, 131, 19))
        self.verticalLayoutWidget_5 = QWidget(self.ElevatedCardWidget_4)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 30, 291, 171))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.LatestShutdown = SubtitleLabel(self.verticalLayoutWidget_5)
        self.LatestShutdown.setObjectName(u"LatestShutdown")

        self.verticalLayout_6.addWidget(self.LatestShutdown, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.ElevatedCardWidget_4)

        self.ElevatedCardWidget_5 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_5.setObjectName(u"ElevatedCardWidget_5")
        self.BodyLabel_7 = BodyLabel(self.ElevatedCardWidget_5)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")
        self.BodyLabel_7.setGeometry(QRect(10, 10, 131, 19))
        self.verticalLayoutWidget_6 = QWidget(self.ElevatedCardWidget_5)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(0, 30, 291, 171))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.LatestStartup = SubtitleLabel(self.verticalLayoutWidget_6)
        self.LatestStartup.setObjectName(u"LatestStartup")

        self.verticalLayout_7.addWidget(self.LatestStartup, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.ElevatedCardWidget_5)

        self.CardWidget_2 = CardWidget(Form)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.CardWidget_2.setGeometry(QRect(10, 240, 791, 521))
        self.MainTable = TableWidget(self.CardWidget_2)
        if (self.MainTable.columnCount() < 8):
            self.MainTable.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.MainTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.MainTable.setObjectName(u"MainTable")
        self.MainTable.setGeometry(QRect(10, 10, 771, 501))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TotalMachines.setText(QCoreApplication.translate("Form", u"None", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"Total:", None))
        self.MachinesOnline.setText(QCoreApplication.translate("Form", u"None", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"Online:", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Form", u"Latest Shutdown:", None))
        self.LatestShutdown.setText(QCoreApplication.translate("Form", u"None", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"Latest Startup:", None))
        self.LatestStartup.setText(QCoreApplication.translate("Form", u"None", None))
        ___qtablewidgetitem = self.MainTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Machine name", None));
        ___qtablewidgetitem1 = self.MainTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"IP Address", None));
        ___qtablewidgetitem2 = self.MainTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Status", None));
        ___qtablewidgetitem3 = self.MainTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Latest Uptime", None));
        ___qtablewidgetitem4 = self.MainTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"CPU Usage", None));
        ___qtablewidgetitem5 = self.MainTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"RAM Usage", None));
        ___qtablewidgetitem6 = self.MainTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Disk usage", None));
        ___qtablewidgetitem7 = self.MainTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Action", None));
    # retranslateUi

