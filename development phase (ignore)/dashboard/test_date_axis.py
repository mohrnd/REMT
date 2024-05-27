import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
import pyqtgraph as pg
from collections import defaultdict
from datetime import datetime

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Machine Details")
        layout = QVBoxLayout(self)
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)
        self.load_timer = QTimer(self)
        self.load_timer.timeout.connect(self.plot_all_values)
        self.load_timer.start(5000)  # Update plot every 5 seconds

    def plot_all_values(self):
        try:
            with open(r"C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\data_viewer\SERVER1.json", "r") as file:
                data = json.load(file)

            timestamps = [datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S") for entry in data]
            cpu_usage = [float(entry["CPUusage"]) for entry in data]

            self.plot_widget.clear()
            self.plot_widget.plot(x=timestamps, y=cpu_usage, pen='r', name="CPU Usage")
            self.plot_widget.setLabel("bottom", "Timestamp")
            self.plot_widget.setLabel("left", "CPU Usage (%)")
            self.plot_widget.setTitle("CPU Usage vs Time")

        except Exception as e:
            print("Error:", e)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
