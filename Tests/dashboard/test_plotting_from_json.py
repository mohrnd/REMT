import sys
import os
import json
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QTimer
import pyqtgraph as pg
from Ui_machine_details import Ui_Form

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.create_plots()
        self.load_timer = QTimer(self)
        self.load_timer.timeout.connect(self.plot_all_values)
        self.load_timer.start(5000)  # Update plot every 5 seconds

    def create_plots(self):
        layout = QVBoxLayout(self.frame)
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground("w")
        self.plot_widget.setTitle("Temperature vs Time", color="#333333", size="20pt")
        styles = {"color": "#333333", "font-size": "14px", "font-family": "Arial"}
        self.plot_widget.setLabel("left", "Temperature (°C)", **styles)
        self.plot_widget.setLabel("right", ".", **styles)
        self.plot_widget.setLabel("bottom", "Time (min)", **styles)
        self.plot_widget.addLegend(offset=(50, 50))
        self.plot_widget.showGrid(x=True, y=True, alpha=0.5)
    
        # Add a new axis on the right side ranging from 0 to 1
        axis = pg.AxisItem(orientation='right')
        axis.setLabel(text='.', **styles)
        axis.setRange(0, 1)
        self.plot_widget.plotItem.layout.addItem(axis, 2, 3)

        axis = pg.AxisItem(orientation='right')
        axis.setLabel(text='.', **styles)
        axis.setRange(0, 100)
        self.plot_widget.plotItem.layout.addItem(axis, 2, 4)
        
        layout.addWidget(self.plot_widget)
        self.plot_all_values()
    
    
    def plot_all_values(self):
        time = []
        temperature_1 = []

        # Read data from JSON file
        try:
            with open(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\dashboard\data.json', 'r') as file:
                data = json.load(file)
                for entry in data:
                    time.append(entry['Time'])
                    temperature_1.append(entry['Temperature'])

            if time and temperature_1:  # Check if lists are not empty
                # Update plot
                time2 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
                pen = pg.mkPen(color=(255, 0, 0), width=2)
                pen2 = pg.mkPen(color=(0, 255, 0), width=2)
                self.plot_widget.clear()
                self.plot_widget.plot(time, temperature_1, name="Temperature Sensor 1", pen=pen, symbol=None, connect="all")
                self.plot_widget.plot(time, time2, name="Temperature Sensor 2", pen=pen2, symbol=None, connect="all")
            month_labels = ['10/10/21','10/10/22 \n time1','10/10/23 \n time1','10/10/24 \n time1','10/10/25 \n time1','10/10/26 \n time1','10/10/27 \n time1','10/10/28 \n time1','10/10/29 \n time1','10/10/30 \n time1']

            ax = self.plot_widget.getAxis('bottom')
            ax.setTicks([[(i, label) for i, label in enumerate(month_labels)]])
            
            
        except Exception as e:
            print("Error:", e)

def main():
    color = QColor('#351392')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
