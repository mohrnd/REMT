import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from Ui_machine_details import Ui_Form  
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, setThemeColor, Theme, FluentWindow,
                            NavigationAvatarWidget, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, CheckBox, PushButton)

import os
import csv

import datetime

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QVBoxLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import pyqtgraph as pg

from Ui_machine_details import Ui_Form  

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_plots()

    def create_plots(self):
        layout = QVBoxLayout(self.frame)

        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]

        self.create_plot(layout, "Temperature Sensor 1", time, temperature_1)


    def create_plot(self, layout, sensor_name, time, temperature):
        plot_widget = pg.PlotWidget()
        plot_widget.setBackground("w")
        plot_widget.setTitle("Temperature vs Time", color="#333333", size="20pt")
        styles = {"color": "#333333", "font-size": "14px", "font-family": "Arial"}
        plot_widget.setLabel("left", "Temperature (°C)", **styles)
        plot_widget.setLabel("bottom", "Time (min)", **styles)
        plot_widget.addLegend(offset=(50, 50))
        plot_widget.showGrid(x=True, y=True, alpha=0.5)
        plot_widget.setXRange(min(time), max(time))
        plot_widget.setYRange(min(temperature), max(temperature))

        pen = pg.mkPen(color=(255, 0, 0), width=2)
        plot_widget.plot(time, temperature, name=sensor_name, pen=pen, symbol=None, connect="all")
        
        layout.addWidget(plot_widget)


def main():
    color = QColor('#351392')
    app = QApplication(sys.argv)
    setThemeColor(color ,Qt.GlobalColor , '') 
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
