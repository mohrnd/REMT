from PyQt5 import QtWidgets
import pyqtgraph as pg

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Temperature Monitoring System")
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)
        self.plot_graph.setBackground("w")
        self.plot_graph.setTitle("Temperature vs Time", color="#333333", size="20pt")
        styles = {"color": "#333333", "font-size": "14px", "font-family": "Arial"}
        self.plot_graph.setLabel("left", "Temperature (°C)", **styles)
        self.plot_graph.setLabel("bottom", "Time (min)", **styles)
        self.plot_graph.addLegend(offset=(50, 50))
        self.plot_graph.showGrid(x=True, y=True, alpha=0.5)
        self.plot_graph.setXRange(1, 10)
        self.plot_graph.setYRange(20, 40)
        time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]
        temperature_2 = [32, 35, 40, 22, 38, 32, 27, 38, 32, 38]
        pen = pg.mkPen(color=(255, 0, 0), width=2)
        self.plot_line(
            "Temperature Sensor 1", time, temperature_1, pen, brush=None
        )
        pen = pg.mkPen(color=(0, 0, 255), width=2)
        self.plot_line(
            "Temperature Sensor 2", time, temperature_2, pen, brush=None
        )

    def plot_line(self, name, time, temperature, pen, brush):
        self.plot_graph.plot(
            time,
            temperature,
            name=name,
            pen=pen,
            symbol=None,  # Removing symbols
            connect="all",  # Connect points with lines
        )

app = QtWidgets.QApplication([])
app.setStyle('Fusion')  # Use Fusion style for a modern look
main = MainWindow()
main.show()
app.exec()
