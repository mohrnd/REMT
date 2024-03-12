import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from SingleSSH_Gui_test1_windows import SSHWidget  

class MultiSSHWindow(QWidget):
    def __init__(self, hosts):
        super().__init__()
        self.hosts = hosts
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.widgets = []
        for hostname, username, password in self.hosts:
            ssh_widget = SSHWidget(hostname, username, password)
            layout.addWidget(ssh_widget)
            self.widgets.append(ssh_widget)
        self.setLayout(layout)
        self.setWindowTitle('Multiple SSH Terminals')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hosts = [
        ('192.168.69.47', 'server1', 'Pa$$w0rd'),
        ('192.168.69.40', 'manager1', 'Pa$$w0rd'),
    ]
    window = MultiSSHWindow(hosts)
    window.setGeometry(100, 100, 800, 600)  
    window.show()
    sys.exit(app.exec_())

