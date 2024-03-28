import sys
import os
import csv
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
        self.load_timer.timeout.connect(self.update_plot)
        self.load_timer.start(5000)  # Update plot every 5 seconds

    def create_plots(self):
        layout = QVBoxLayout(self.frame)
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground("w")
        self.plot_widget.setTitle("Temperature vs Time", color="#333333", size="20pt")
        styles = {"color": "#333333", "font-size": "14px", "font-family": "Arial"}
        self.plot_widget.setLabel("left", "Temperature (°C)", **styles)
        self.plot_widget.setLabel("bottom", "Time (min)", **styles)
        self.plot_widget.addLegend(offset=(50, 50))
        self.plot_widget.showGrid(x=True, y=True, alpha=0.5)
        layout.addWidget(self.plot_widget)
        self.update_plot()

    def update_plot_all_values(self):
        time = []
        temperature_1 = []

        # Read data from CSV file
        with open(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\dashboard\data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                time.append(float(row[0]))
                temperature_1.append(float(row[1]))

        # Update plot
        pen = pg.mkPen(color=(255, 0, 0), width=2)
        self.plot_widget.clear()
        self.plot_widget.plot(time, temperature_1, name="Temperature Sensor 1", pen=pen, symbol=None, connect="all")
    
    # plot the latest 10 values
    def update_plot(self):
        time = []
        temperature_1 = []
    
        # Read data from CSV file
        with open(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\dashboard\data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                time.append(float(row[0]))
                temperature_1.append(float(row[1]))
    
        # Extract the last 10 values
        time = time[-10:]
        temperature_1 = temperature_1[-10:]
    
        # Update plot
        pen = pg.mkPen(color=(255, 0, 0), width=2)
        self.plot_widget.clear()
        self.plot_widget.plot(time, temperature_1, name="Temperature Sensor 1", pen=pen, symbol=None, connect="all")

def main():
    color = QColor('#351392')
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
