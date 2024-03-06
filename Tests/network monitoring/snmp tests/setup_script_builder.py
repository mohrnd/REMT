import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class SetupScriptGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SNMP Setup Script Generator")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.community_label = QLabel("SNMP Community String:")
        self.community_input = QLineEdit()
        layout.addWidget(self.community_label)
        layout.addWidget(self.community_input)

        self.username_label = QLabel("SNMP Username:")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.sha_label = QLabel("SHA Password:")
        self.sha_input = QLineEdit()
        layout.addWidget(self.sha_label)
        layout.addWidget(self.sha_input)

        self.aes_label = QLabel("AES Password:")
        self.aes_input = QLineEdit()
        
        self.ip_label = QLabel("local IP:")
        self.ip = QLineEdit()
        
        layout.addWidget(self.aes_label)
        layout.addWidget(self.aes_input)
        layout.addWidget(self.ip_label)
        layout.addWidget(self.ip)

        self.generate_button = QPushButton("Generate Setup Script")
        self.generate_button.clicked.connect(self.generate_setup_script)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def generate_setup_script(self):
        community_string = self.community_input.text()
        username = self.username_input.text()
        sha_password = self.sha_input.text()
        aes_password = self.aes_input.text()
        ip = self.ip.text()

        with open(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\network monitoring\snmp tests\snmp_agent_conf_template.txt', 'r') as file:
            setup_script_content = file.read()

        setup_script_content = setup_script_content.format(community_string=community_string, username=username, sha_password=sha_password, aes_password=aes_password, ip=ip)

        with open('setup_2.sh', 'w') as file:
            file.write(setup_script_content.format(community_string=community_string, username=username, sha_password=sha_password, aes_password=aes_password))

        sys.exit("Setup script generated successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SetupScriptGenerator()
    window.show()
    sys.exit(app.exec_())
