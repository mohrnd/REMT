import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton


# template
class IPSelectionWindow(QWidget):
    def __init__(self, ip_list):
        super().__init__()
        self.ip_list = ip_list
        self.initUI()

    def initUI(self):
        self.setWindowTitle('IP Selection Window')
        self.layout = QVBoxLayout()
        self.checkboxes = []
        for ip in self.ip_list:
            checkbox = QCheckBox(ip)
            self.checkboxes.append(checkbox)
            self.layout.addWidget(checkbox)

        self.select_button = QPushButton('Select IPs')
        self.select_button.clicked.connect(self.print_selected_ips)
        self.layout.addWidget(self.select_button)

        self.setLayout(self.layout)

    def print_selected_ips(self):
        selected_ips = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]
        print("Selected IPs:", selected_ips)

def main():
    # Sample list of IP addresses
    ip_list = ['192.168.1.1', '10.0.0.1', '172.16.0.1', '8.8.8.8']

    app = QApplication(sys.argv)
    window = IPSelectionWindow(ip_list)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
