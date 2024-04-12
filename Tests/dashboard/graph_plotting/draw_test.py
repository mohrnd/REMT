import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFrame
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime, timedelta

# Path to your JSON file
json_file = r"C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\dashboard\SERVER1.json"

# Function to parse timestamp to datetime object
def parse_timestamp(timestamp):
    return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

# Load JSON data
with open(json_file, 'r') as f:
    data = json.load(f)

# Extract LOAD1min and timestamp data
load1min_data = []
timestamps = []
for entry in data:
    load1min_data.append(entry["LOAD1min"])
    timestamps.append(parse_timestamp(entry["timestamp"]))

# Create a custom QMainWindow class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LOAD1min Plot")

        # Create a central widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # Create a QVBoxLayout to hold the plot and button
        layout = QVBoxLayout(self.centralWidget)

        # Create a QFrame to hold the plot
        self.frame = QFrame()
        layout.addWidget(self.frame)

        # Create a layout for the frame if it does not exist
        if self.frame.layout() is None:
            self.frame.setLayout(QVBoxLayout())

        # Create a Figure and a FigureCanvas to embed the plot
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.frame.layout().addWidget(self.canvas)

        # Create a plot
        self.plot_load1min()

        # Add a refresh button
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.plot_load1min)
        layout.addWidget(self.refresh_button)

    def plot_load1min(self):
        # Clear previous plot
        self.fig.clear()

        # Plotting
        ax = self.fig.add_subplot(111)
        ax.plot(timestamps, load1min_data, marker='o', linestyle='-')
        ax.set_title('Average LOAD1min per Hour')
        ax.set_xlabel('Time')
        ax.set_ylabel('Average LOAD1min')
        ax.grid(True)
        ax.tick_params(axis='x', rotation=90)

        # Draw the plot
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
