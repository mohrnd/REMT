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

        setup_script_content = f'''#!/bin/bash
#turn into an executable with: chmod +x setup.sh
#run as root

echo "Installing net-snmp RPMs..."
yum install -y net-snmp net-snmp-libs net-snmp-utils net-snmp-agent-libs

rm -rf  /etc/snmp/snmpd.conf
touch /etc/snmp/snmpd.conf

systemctl stop snmpd

echo "Setting up..."
echo "com2sec notConfigUser  default       {community_string}" >> /etc/snmp/snmpd.conf
echo "group   notConfigGroup v1           notConfigUser" >> /etc/snmp/snmpd.conf
echo "group   notConfigGroup v2c           notConfigUser" >> /etc/snmp/snmpd.conf
echo "view    systemview    included   .1.3.6.1.2.1.1" >> /etc/snmp/snmpd.conf
echo "view    systemview    included   .1.3.6.1.2.1.25.1.1" >> /etc/snmp/snmpd.conf
echo "access  notConfigGroup \"\"      any       noauth    exact  systemview none none" >> /etc/snmp/snmpd.conf
echo "syslocation " >> /etc/snmp/snmpd.conf #can be removed
echo "syscontact " >> /etc/snmp/snmpd.conf
echo "dontLogTCPWrappersConnects yes" >> /etc/snmp/snmpd.conf
echo "createUser {username} SHA {sha_password} AES {aes_password}" >> /etc/snmp/snmpd.conf
echo "rouser {username} authpriv system" >> /etc/snmp/snmpd.conf
echo "informsink {ip} {community_string}" >> /etc/snmp/snmpd.conf
echo "authtrapenable 2" >> /etc/snmp/snmpd.conf
echo "agentSecName {username}" >> /etc/snmp/snmpd.conf
echo "defaultMonitors yes" >> /etc/snmp/snmpd.conf

echo "Enabling and starting snmpd service..."
systemctl enable snmpd
systemctl start snmpd
systemctl restart snmpd

echo "Setting up the firewall..."
firewall-cmd --add-service=snmp --permanent
firewall-cmd --zone=public --add-port=161/udp --permanent
firewall-cmd --zone=public --add-port=162/udp --permanent
firewall-cmd --reload

echo "SNMP configuration completed."
'''
        with open('setup.sh', 'w') as file:
            file.write(setup_script_content.format(community_string=community_string, username=username, sha_password=sha_password, aes_password=aes_password))

        sys.exit("Setup script generated successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SetupScriptGenerator()
    window.show()
    sys.exit(app.exec_())
