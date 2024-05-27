from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Temperature Monitoring System")
        
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)
        
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]
        temperature_2 = [32, 35, 40, 22, 38, 32, 27, 38, 32, 38]
        temperature_3 = [28, 29, 30, 31, 33, 35, 36, 37, 35, 33]
        temperature_4 = [36, 38, 37, 39, 40, 38, 37, 36, 34, 35]

        self.create_plot(layout, "Temperature Sensor 1", time, temperature_1, row=0, col=0)
        self.create_plot(layout, "Temperature Sensor 2", time, temperature_2, row=0, col=1)
        self.create_plot(layout, "Temperature Sensor 3", time, temperature_3, row=1, col=0)
        self.create_plot(layout, "Temperature Sensor 4", time, temperature_4, row=1, col=1)
        
    def create_plot(self, layout, sensor_name, time, temperature, row, col):
        plot_widget = pg.PlotWidget()
        plot_widget.setBackground("w")
        plot_widget.setTitle("Temperature vs Time", color="#333333", size="20pt")
        styles = {"color": "#666666", "font-size": "12pt", "font-family": "Segoe UI", "font-weight": "bold"}

        plot_widget.setLabel("left", "Temperature (°C)", **styles)
        plot_widget.setLabel("bottom", "Time (min)", **styles)
        plot_widget.addLegend(offset=(50, 50))
        plot_widget.showGrid(x=True, y=True, alpha=0.5)
        plot_widget.setXRange(min(time), max(time))
        plot_widget.setYRange(min(temperature), max(temperature))

        pen = pg.mkPen(color=(255, 0, 0), width=2)
        plot_widget.plot(time, temperature, name=sensor_name, pen=pen, symbol=None, connect="all")
        
        layout.addWidget(plot_widget, row, col)

app = QtWidgets.QApplication([])
app.setStyle('Fusion')  # Use Fusion style for a modern look
main = MainWindow()
main.show()
app.exec_()
