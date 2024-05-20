import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCompleter
from qfluentwidgets import setThemeColor
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor
import re
from .Ui_Traps_Viewer_interface import Ui_Form

class MainWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.log_file_path = r"..\REMT\TrapsReceived.log"  # Update with the actual log file path
        self.stands = ["SystemStartup", "SystemShutdown"]
        self.ip_addresses = set()
        self.load_log_file()

        self.Filter_Button.clicked.connect(self.filter_traps)

        completer_data = list(self.ip_addresses) + self.stands
        self.completer = QCompleter(completer_data, self.Filter)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setMaxVisibleItems(10)
        self.Filter.setCompleter(self.completer)

        # Create a QTimer for updating every 60 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_content)
        self.timer.start(60000)  # 60000 milliseconds = 60 seconds

    def load_log_file(self):
        try:
            with open(self.log_file_path, 'r') as file:
                content = file.read()
                self.All_Traps_received.setPlainText(content)
                self.extract_ip_addresses(content)
                # self.extract_latest_trap(content)
        except Exception as e:
            self.All_Traps_received.setPlainText(f"Error reading log file: {e}")

    def extract_ip_addresses(self, content):
        lines = content.split('\n')
        ip_pattern = re.compile(r'Trap from "(\d+\.\d+\.\d+\.\d+)"')
        for line in lines:
            match = ip_pattern.search(line)
            if match:
                self.ip_addresses.add(match.group(1))

    def filter_traps(self):
        filter_text = self.Filter.text()
        if not filter_text:
            return

        try:
            with open(self.log_file_path, 'r') as file:
                lines = file.readlines()

            filtered_lines = []
            for line in lines:
                if filter_text in line:
                    filtered_lines.append(line)

            self.All_Traps_received.setPlainText(''.join(filtered_lines))
        except Exception as e:
            self.All_Traps_received.setPlainText(f"Error filtering log file: {e}")


    def update_content(self):
        # Call load_log_file to update the content
        self.load_log_file()


def main():
    app = QApplication(sys.argv)
    color = QColor('#351392')
    setThemeColor(color.name(), Qt.GlobalColor, '')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
