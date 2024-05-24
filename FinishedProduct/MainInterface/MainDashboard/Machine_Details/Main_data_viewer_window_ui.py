# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_data_viewer_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QSizePolicy,
    QSpacerItem, QTabWidget, QToolBox, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, CalendarPicker, CaptionLabel, CardWidget,
    ElevatedCardWidget, HorizontalSeparator, LineEdit, PrimaryPushButton,
    ProgressBar, ProgressRing, PushButton, SimpleCardWidget,
    StrongBodyLabel, SubtitleLabel, TimePicker)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1079, 820)
        self.MainCard = CardWidget(Form)
        self.MainCard.setObjectName(u"MainCard")
        self.MainCard.setGeometry(QRect(10, 10, 1061, 351))
        self.SubtitleLabel = SubtitleLabel(self.MainCard)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")
        self.SubtitleLabel.setGeometry(QRect(10, 0, 161, 28))
        self.horizontalLayoutWidget = QWidget(self.MainCard)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 1041, 101))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ElevatedCardWidget_7 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_7.setObjectName(u"ElevatedCardWidget_7")
        self.MachineName = BodyLabel(self.ElevatedCardWidget_7)
        self.MachineName.setObjectName(u"MachineName")
        self.MachineName.setGeometry(QRect(10, 10, 151, 20))

        self.verticalLayout_2.addWidget(self.ElevatedCardWidget_7)

        self.ElevatedCardWidget_6 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_6.setObjectName(u"ElevatedCardWidget_6")
        self.MachineIP = BodyLabel(self.ElevatedCardWidget_6)
        self.MachineIP.setObjectName(u"MachineIP")
        self.MachineIP.setGeometry(QRect(10, 10, 151, 19))

        self.verticalLayout_2.addWidget(self.ElevatedCardWidget_6)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.ElevatedCardWidget_5 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_5.setObjectName(u"ElevatedCardWidget_5")
        self.BodyLabel_3 = BodyLabel(self.ElevatedCardWidget_5)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        self.BodyLabel_3.setGeometry(QRect(10, 10, 63, 19))
        self.verticalLayoutWidget = QWidget(self.ElevatedCardWidget_5)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 20, 161, 51))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Uptime = SubtitleLabel(self.verticalLayoutWidget)
        self.Uptime.setObjectName(u"Uptime")

        self.verticalLayout.addWidget(self.Uptime, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.ElevatedCardWidget_5)

        self.ElevatedCardWidget_11 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_11.setObjectName(u"ElevatedCardWidget_11")
        self.BodyLabel_7 = BodyLabel(self.ElevatedCardWidget_11)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")
        self.BodyLabel_7.setGeometry(QRect(10, 10, 101, 19))
        self.verticalLayoutWidget_7 = QWidget(self.ElevatedCardWidget_11)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(0, 20, 161, 51))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.TotalDisk = SubtitleLabel(self.verticalLayoutWidget_7)
        self.TotalDisk.setObjectName(u"TotalDisk")

        self.verticalLayout_9.addWidget(self.TotalDisk, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.ElevatedCardWidget_11)

        self.ElevatedCardWidget_10 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_10.setObjectName(u"ElevatedCardWidget_10")
        self.BodyLabel_6 = BodyLabel(self.ElevatedCardWidget_10)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")
        self.BodyLabel_6.setGeometry(QRect(10, 10, 91, 19))
        self.verticalLayoutWidget_6 = QWidget(self.ElevatedCardWidget_10)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(0, 20, 161, 51))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.CpuCores = SubtitleLabel(self.verticalLayoutWidget_6)
        self.CpuCores.setObjectName(u"CpuCores")

        self.verticalLayout_8.addWidget(self.CpuCores, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.ElevatedCardWidget_10)

        self.ElevatedCardWidget_9 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_9.setObjectName(u"ElevatedCardWidget_9")
        self.BodyLabel_5 = BodyLabel(self.ElevatedCardWidget_9)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")
        self.BodyLabel_5.setGeometry(QRect(10, 10, 91, 19))
        self.verticalLayoutWidget_5 = QWidget(self.ElevatedCardWidget_9)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 20, 161, 51))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.TotalRam = SubtitleLabel(self.verticalLayoutWidget_5)
        self.TotalRam.setObjectName(u"TotalRam")

        self.verticalLayout_7.addWidget(self.TotalRam, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.ElevatedCardWidget_9)

        self.ElevatedCardWidget_8 = ElevatedCardWidget(self.horizontalLayoutWidget)
        self.ElevatedCardWidget_8.setObjectName(u"ElevatedCardWidget_8")
        self.BodyLabel_4 = BodyLabel(self.ElevatedCardWidget_8)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")
        self.BodyLabel_4.setGeometry(QRect(10, 10, 101, 19))
        self.verticalLayoutWidget_4 = QWidget(self.ElevatedCardWidget_8)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 20, 161, 51))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Nics = SubtitleLabel(self.verticalLayoutWidget_4)
        self.Nics.setObjectName(u"Nics")

        self.verticalLayout_6.addWidget(self.Nics, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.ElevatedCardWidget_8)

        self.horizontalLayoutWidget_2 = QWidget(self.MainCard)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 130, 1041, 201))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ElevatedCardWidget = ElevatedCardWidget(self.horizontalLayoutWidget_2)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        self.gridLayoutWidget_2 = QWidget(self.ElevatedCardWidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, -5, 341, 161))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.CPUusagering = ProgressRing(self.gridLayoutWidget_2)
        self.CPUusagering.setObjectName(u"CPUusagering")
        self.CPUusagering.setTextVisible(True)

        self.gridLayout_2.addWidget(self.CPUusagering, 1, 0, 1, 1)

        self.Diskusagering = ProgressRing(self.gridLayoutWidget_2)
        self.Diskusagering.setObjectName(u"Diskusagering")
        self.Diskusagering.setTextVisible(True)

        self.gridLayout_2.addWidget(self.Diskusagering, 1, 2, 1, 1)

        self.RAMusagering = ProgressRing(self.gridLayoutWidget_2)
        self.RAMusagering.setObjectName(u"RAMusagering")
        self.RAMusagering.setTextVisible(True)

        self.gridLayout_2.addWidget(self.RAMusagering, 1, 1, 1, 1)

        self.StrongBodyLabel = StrongBodyLabel(self.gridLayoutWidget_2)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")

        self.gridLayout_2.addWidget(self.StrongBodyLabel, 0, 0, 1, 1, Qt.AlignHCenter)

        self.StrongBodyLabel_2 = StrongBodyLabel(self.gridLayoutWidget_2)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")

        self.gridLayout_2.addWidget(self.StrongBodyLabel_2, 0, 1, 1, 1, Qt.AlignHCenter)

        self.StrongBodyLabel_3 = StrongBodyLabel(self.gridLayoutWidget_2)
        self.StrongBodyLabel_3.setObjectName(u"StrongBodyLabel_3")

        self.gridLayout_2.addWidget(self.StrongBodyLabel_3, 0, 2, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.ElevatedCardWidget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ElevatedCardWidget_13 = ElevatedCardWidget(self.horizontalLayoutWidget_2)
        self.ElevatedCardWidget_13.setObjectName(u"ElevatedCardWidget_13")
        self.gridLayoutWidget = QWidget(self.ElevatedCardWidget_13)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 341, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.min1LoadRing = ProgressRing(self.gridLayoutWidget)
        self.min1LoadRing.setObjectName(u"min1LoadRing")
        self.min1LoadRing.setTextVisible(True)

        self.gridLayout.addWidget(self.min1LoadRing, 1, 0, 1, 1)

        self.StrongBodyLabel_4 = StrongBodyLabel(self.gridLayoutWidget)
        self.StrongBodyLabel_4.setObjectName(u"StrongBodyLabel_4")

        self.gridLayout.addWidget(self.StrongBodyLabel_4, 0, 0, 1, 1, Qt.AlignHCenter)

        self.min15LoadRing = ProgressRing(self.gridLayoutWidget)
        self.min15LoadRing.setObjectName(u"min15LoadRing")
        self.min15LoadRing.setTextVisible(True)

        self.gridLayout.addWidget(self.min15LoadRing, 1, 2, 1, 1)

        self.StrongBodyLabel_6 = StrongBodyLabel(self.gridLayoutWidget)
        self.StrongBodyLabel_6.setObjectName(u"StrongBodyLabel_6")

        self.gridLayout.addWidget(self.StrongBodyLabel_6, 0, 2, 1, 1, Qt.AlignHCenter)

        self.min5LoadRing = ProgressRing(self.gridLayoutWidget)
        self.min5LoadRing.setObjectName(u"min5LoadRing")
        self.min5LoadRing.setTextVisible(True)

        self.gridLayout.addWidget(self.min5LoadRing, 1, 1, 1, 1)

        self.StrongBodyLabel_5 = StrongBodyLabel(self.gridLayoutWidget)
        self.StrongBodyLabel_5.setObjectName(u"StrongBodyLabel_5")

        self.gridLayout.addWidget(self.StrongBodyLabel_5, 0, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.ElevatedCardWidget_13)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.ElevatedCardWidget_2 = ElevatedCardWidget(self.horizontalLayoutWidget_2)
        self.ElevatedCardWidget_2.setObjectName(u"ElevatedCardWidget_2")
        self.gridLayoutWidget_7 = QWidget(self.ElevatedCardWidget_2)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(10, 10, 321, 31))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.TotalCachedMemory = BodyLabel(self.gridLayoutWidget_7)
        self.TotalCachedMemory.setObjectName(u"TotalCachedMemory")

        self.gridLayout_7.addWidget(self.TotalCachedMemory, 0, 1, 1, 1)

        self.StrongBodyLabel_11 = StrongBodyLabel(self.gridLayoutWidget_7)
        self.StrongBodyLabel_11.setObjectName(u"StrongBodyLabel_11")

        self.gridLayout_7.addWidget(self.StrongBodyLabel_11, 0, 0, 1, 1)

        self.gridLayoutWidget_5 = QWidget(self.ElevatedCardWidget_2)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 40, 321, 31))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.StrongBodyLabel_9 = StrongBodyLabel(self.gridLayoutWidget_5)
        self.StrongBodyLabel_9.setObjectName(u"StrongBodyLabel_9")

        self.gridLayout_5.addWidget(self.StrongBodyLabel_9, 0, 0, 1, 1, Qt.AlignHCenter)

        self.TotalSwap = BodyLabel(self.gridLayoutWidget_5)
        self.TotalSwap.setObjectName(u"TotalSwap")

        self.gridLayout_5.addWidget(self.TotalSwap, 0, 1, 1, 1)

        self.gridLayoutWidget_6 = QWidget(self.ElevatedCardWidget_2)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 70, 321, 31))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.AvailableSwap = BodyLabel(self.gridLayoutWidget_6)
        self.AvailableSwap.setObjectName(u"AvailableSwap")

        self.gridLayout_6.addWidget(self.AvailableSwap, 0, 1, 1, 1)

        self.StrongBodyLabel_10 = StrongBodyLabel(self.gridLayoutWidget_6)
        self.StrongBodyLabel_10.setObjectName(u"StrongBodyLabel_10")

        self.gridLayout_6.addWidget(self.StrongBodyLabel_10, 0, 0, 1, 1, Qt.AlignHCenter)

        self.HorizontalSeparator = HorizontalSeparator(self.ElevatedCardWidget_2)
        self.HorizontalSeparator.setObjectName(u"HorizontalSeparator")
        self.HorizontalSeparator.setGeometry(QRect(10, 110, 321, 3))
        self.gridLayoutWidget_3 = QWidget(self.ElevatedCardWidget_2)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 120, 321, 31))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.StrongBodyLabel_7 = StrongBodyLabel(self.gridLayoutWidget_3)
        self.StrongBodyLabel_7.setObjectName(u"StrongBodyLabel_7")

        self.gridLayout_3.addWidget(self.StrongBodyLabel_7, 0, 0, 1, 1, Qt.AlignHCenter)

        self.NetworkOut = BodyLabel(self.gridLayoutWidget_3)
        self.NetworkOut.setObjectName(u"NetworkOut")

        self.gridLayout_3.addWidget(self.NetworkOut, 0, 1, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.ElevatedCardWidget_2)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 150, 321, 31))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.NetworkIn = BodyLabel(self.gridLayoutWidget_4)
        self.NetworkIn.setObjectName(u"NetworkIn")

        self.gridLayout_4.addWidget(self.NetworkIn, 0, 1, 1, 1)

        self.StrongBodyLabel_8 = StrongBodyLabel(self.gridLayoutWidget_4)
        self.StrongBodyLabel_8.setObjectName(u"StrongBodyLabel_8")

        self.gridLayout_4.addWidget(self.StrongBodyLabel_8, 0, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.ElevatedCardWidget_2)

        self.TimestampLabel = CaptionLabel(self.MainCard)
        self.TimestampLabel.setObjectName(u"TimestampLabel")
        self.TimestampLabel.setGeometry(QRect(160, 10, 471, 16))
        self.CardWidget = CardWidget(Form)
        self.CardWidget.setObjectName(u"CardWidget")
        self.CardWidget.setGeometry(QRect(10, 370, 1061, 451))
        self.gridLayout_8 = QGridLayout(self.CardWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.PrimaryPushButton = PrimaryPushButton(self.CardWidget)
        self.PrimaryPushButton.setObjectName(u"PrimaryPushButton")

        self.horizontalLayout_4.addWidget(self.PrimaryPushButton)


        self.gridLayout_8.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.CardWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.LastHourTab = QWidget()
        self.LastHourTab.setObjectName(u"LastHourTab")
        self.TabLastHour = QTabWidget(self.LastHourTab)
        self.TabLastHour.setObjectName(u"TabLastHour")
        self.TabLastHour.setGeometry(QRect(0, 0, 1041, 371))
        self.CPULastHour = QWidget()
        self.CPULastHour.setObjectName(u"CPULastHour")
        self.TabLastHour.addTab(self.CPULastHour, "")
        self.LoadsLastHour = QWidget()
        self.LoadsLastHour.setObjectName(u"LoadsLastHour")
        self.TabLastHour.addTab(self.LoadsLastHour, "")
        self.NetworkLastHour = QWidget()
        self.NetworkLastHour.setObjectName(u"NetworkLastHour")
        self.TabLastHour.addTab(self.NetworkLastHour, "")
        self.tabWidget.addTab(self.LastHourTab, "")
        self.Last24HoursTab = QWidget()
        self.Last24HoursTab.setObjectName(u"Last24HoursTab")
        self.TabLast24Hours = QTabWidget(self.Last24HoursTab)
        self.TabLast24Hours.setObjectName(u"TabLast24Hours")
        self.TabLast24Hours.setGeometry(QRect(0, 0, 1041, 371))
        self.CPULast24Hours = QWidget()
        self.CPULast24Hours.setObjectName(u"CPULast24Hours")
        self.TabLast24Hours.addTab(self.CPULast24Hours, "")
        self.LoadsLast24Hours = QWidget()
        self.LoadsLast24Hours.setObjectName(u"LoadsLast24Hours")
        self.TabLast24Hours.addTab(self.LoadsLast24Hours, "")
        self.NetworkLast24Hours = QWidget()
        self.NetworkLast24Hours.setObjectName(u"NetworkLast24Hours")
        self.TabLast24Hours.addTab(self.NetworkLast24Hours, "")
        self.tabWidget.addTab(self.Last24HoursTab, "")
        self.CustomTab = QWidget()
        self.CustomTab.setObjectName(u"CustomTab")
        self.toolBox = QToolBox(self.CustomTab)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(0, 0, 1041, 361))
        self.Intervalselection = QWidget()
        self.Intervalselection.setObjectName(u"Intervalselection")
        self.Intervalselection.setGeometry(QRect(0, 0, 1041, 307))
        self.horizontalLayoutWidget_3 = QWidget(self.Intervalselection)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 0, 1041, 131))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.StartTime = TimePicker(self.horizontalLayoutWidget_3)
        self.StartTime.setObjectName(u"StartTime")

        self.gridLayout_9.addWidget(self.StartTime, 0, 2, 1, 1)

        self.EndDate = CalendarPicker(self.horizontalLayoutWidget_3)
        self.EndDate.setObjectName(u"EndDate")

        self.gridLayout_9.addWidget(self.EndDate, 1, 1, 1, 1)

        self.StartDate = CalendarPicker(self.horizontalLayoutWidget_3)
        self.StartDate.setObjectName(u"StartDate")

        self.gridLayout_9.addWidget(self.StartDate, 0, 1, 1, 1)

        self.EndTime = TimePicker(self.horizontalLayoutWidget_3)
        self.EndTime.setObjectName(u"EndTime")

        self.gridLayout_9.addWidget(self.EndTime, 1, 2, 1, 1)

        self.PlotButton = PrimaryPushButton(self.horizontalLayoutWidget_3)
        self.PlotButton.setObjectName(u"PlotButton")

        self.gridLayout_9.addWidget(self.PlotButton, 1, 3, 1, 1)

        self.Ticks = LineEdit(self.horizontalLayoutWidget_3)
        self.Ticks.setObjectName(u"Ticks")

        self.gridLayout_9.addWidget(self.Ticks, 0, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_9)

        self.toolBox.addItem(self.Intervalselection, u"Interval selection")
        self.Plots = QWidget()
        self.Plots.setObjectName(u"Plots")
        self.Plots.setGeometry(QRect(0, 0, 1041, 307))
        self.CustomSubTab = QTabWidget(self.Plots)
        self.CustomSubTab.setObjectName(u"CustomSubTab")
        self.CustomSubTab.setGeometry(QRect(0, 0, 1041, 311))
        self.CPUCustom = QWidget()
        self.CPUCustom.setObjectName(u"CPUCustom")
        self.CustomSubTab.addTab(self.CPUCustom, "")
        self.LoadsCustom = QWidget()
        self.LoadsCustom.setObjectName(u"LoadsCustom")
        self.CustomSubTab.addTab(self.LoadsCustom, "")
        self.NetworkCustom = QWidget()
        self.NetworkCustom.setObjectName(u"NetworkCustom")
        self.CustomSubTab.addTab(self.NetworkCustom, "")
        self.toolBox.addItem(self.Plots, u"Plots")
        self.tabWidget.addTab(self.CustomTab, "")

        self.gridLayout_8.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(2)
        self.TabLastHour.setCurrentIndex(2)
        self.TabLast24Hours.setCurrentIndex(2)
        self.toolBox.setCurrentIndex(1)
        self.CustomSubTab.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Form", u"Machine details: ", None))
        self.MachineName.setText(QCoreApplication.translate("Form", u"Name", None))
        self.MachineIP.setText(QCoreApplication.translate("Form", u"IP", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Form", u"Uptime:", None))
        self.Uptime.setText(QCoreApplication.translate("Form", u"None", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"Total Disk:", None))
        self.TotalDisk.setText(QCoreApplication.translate("Form", u"None", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Form", u"Cpu cores:", None))
        self.CpuCores.setText(QCoreApplication.translate("Form", u"None", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Form", u"Total Ram:", None))
        self.TotalRam.setText(QCoreApplication.translate("Form", u"None", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Form", u"NICs:", None))
        self.Nics.setText(QCoreApplication.translate("Form", u"None", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"CPU", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("Form", u"RAM", None))
        self.StrongBodyLabel_3.setText(QCoreApplication.translate("Form", u"Disk", None))
        self.StrongBodyLabel_4.setText(QCoreApplication.translate("Form", u"1 Min load", None))
        self.StrongBodyLabel_6.setText(QCoreApplication.translate("Form", u"15 Min load", None))
        self.StrongBodyLabel_5.setText(QCoreApplication.translate("Form", u"5 Min load", None))
        self.TotalCachedMemory.setText(QCoreApplication.translate("Form", u"Null", None))
        self.StrongBodyLabel_11.setText(QCoreApplication.translate("Form", u"Total cached Memory:", None))
        self.StrongBodyLabel_9.setText(QCoreApplication.translate("Form", u"Total swap:", None))
        self.TotalSwap.setText(QCoreApplication.translate("Form", u"Null", None))
        self.AvailableSwap.setText(QCoreApplication.translate("Form", u"Null", None))
        self.StrongBodyLabel_10.setText(QCoreApplication.translate("Form", u"Available swap:", None))
        self.StrongBodyLabel_7.setText(QCoreApplication.translate("Form", u"Network Out:", None))
        self.NetworkOut.setText(QCoreApplication.translate("Form", u"Null", None))
        self.NetworkIn.setText(QCoreApplication.translate("Form", u"Null", None))
        self.StrongBodyLabel_8.setText(QCoreApplication.translate("Form", u"Network In:", None))
        self.TimestampLabel.setText(QCoreApplication.translate("Form", u"   As of Null", None))
        self.PrimaryPushButton.setText(QCoreApplication.translate("Form", u"Refresh Graphs", None))
        self.TabLastHour.setTabText(self.TabLastHour.indexOf(self.CPULastHour), QCoreApplication.translate("Form", u"CPU, RAM, Disk usage", None))
        self.TabLastHour.setTabText(self.TabLastHour.indexOf(self.LoadsLastHour), QCoreApplication.translate("Form", u"1,5,15 mins Loads", None))
        self.TabLastHour.setTabText(self.TabLastHour.indexOf(self.NetworkLastHour), QCoreApplication.translate("Form", u"Network Usage", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.LastHourTab), QCoreApplication.translate("Form", u"Last Hour", None))
        self.TabLast24Hours.setTabText(self.TabLast24Hours.indexOf(self.CPULast24Hours), QCoreApplication.translate("Form", u"CPU, RAM, Disk usage", None))
        self.TabLast24Hours.setTabText(self.TabLast24Hours.indexOf(self.LoadsLast24Hours), QCoreApplication.translate("Form", u"1,5,15 mins Loads", None))
        self.TabLast24Hours.setTabText(self.TabLast24Hours.indexOf(self.NetworkLast24Hours), QCoreApplication.translate("Form", u"Network Usage", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Last24HoursTab), QCoreApplication.translate("Form", u"Last 24 Hours", None))
        self.EndDate.setText(QCoreApplication.translate("Form", u"End Date", None))
        self.StartDate.setText(QCoreApplication.translate("Form", u"Start Date", None))
        self.PlotButton.setText(QCoreApplication.translate("Form", u"Plot", None))
        self.Ticks.setPlaceholderText(QCoreApplication.translate("Form", u"Ticks", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Intervalselection), QCoreApplication.translate("Form", u"Interval selection", None))
        self.CustomSubTab.setTabText(self.CustomSubTab.indexOf(self.CPUCustom), QCoreApplication.translate("Form", u"CPU, RAM, Disk usage", None))
        self.CustomSubTab.setTabText(self.CustomSubTab.indexOf(self.LoadsCustom), QCoreApplication.translate("Form", u"1,5,15 mins Loads", None))
        self.CustomSubTab.setTabText(self.CustomSubTab.indexOf(self.NetworkCustom), QCoreApplication.translate("Form", u"Network Usage", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Plots), QCoreApplication.translate("Form", u"Plots", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CustomTab), QCoreApplication.translate("Form", u"Custom", None))
    # retranslateUi

