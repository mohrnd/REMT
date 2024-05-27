import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QTextEdit, QMessageBox
from PyQt5.QtCore import Qt
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
from pysnmp.proto.api import v2c
import csv
import datetime

class SNMPReceiverApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SNMP Notification Receiver")

        # Create GUI components
        self.start_button = QPushButton("Start Receiver")
        self.logs_label = QLabel("Logs:")
        self.logs_text = QTextEdit()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.logs_label)
        layout.addWidget(self.logs_text)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Connect button click event
        self.start_button.clicked.connect(self.start_receiver)

        # Initialize SNMP engine
        self.snmpEngine = engine.SnmpEngine()

    def start_receiver(self):
        # Add SNMP users from CSV
        csv_file_path = r'C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\network monitoring\snmp tests\snmp_users.csv'
        add_snmp_users_from_csv(csv_file_path, self.snmpEngine)

        # Transport setup
        # UDP over IPv4
        config.addTransport(
            self.snmpEngine,
            udp.domainName,
            udp.UdpTransport().openServerMode(('0.0.0.0', 162))
        )

        # Register SNMP Application at the SNMP engine
        ntfrcv.NotificationReceiver(self.snmpEngine, self.cbFun)

        # Run I/O dispatcher which would receive queries and send confirmations
        try:
            self.snmpEngine.transportDispatcher.jobStarted(1)  # this job would never finish
            self.snmpEngine.transportDispatcher.runDispatcher()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            self.snmpEngine.transportDispatcher.closeDispatcher()

    def cbFun(self, snmpEngine, stateReference, contextEngineId, contextName,
              varBinds, cbCtx):
        transport_info = snmpEngine.msgAndPduDsp.getTransportInfo(stateReference)
        if transport_info:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ip_address = transport_info[1][0]
            log_message = f"{current_time} - Trap from {ip_address}\n"
            self.logs_text.append(log_message)
        else:
            log_message = "Trap from Unknown IP Address likely an SNMPv3 trap, wait for the SNMPV3 TRAP UPDATE or edit the source code yourself\n"
            self.logs_text.append(log_message)

        for name, val in varBinds:
            oid_str = name.prettyPrint()
            value_str = val.prettyPrint()
            interpreted_oid = interpret_oid(oid_str)
            log_message = f"{interpreted_oid} = {value_str}\n"
            self.logs_text.append(log_message)

def add_snmp_users_from_csv(CSV_File_Path, snmpEngine):
    with open(CSV_File_Path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row['username']
            auth_protocol = getattr(config, row['auth_protocol'])
            auth_password = row['auth_password']
            priv_protocol = getattr(config, row['priv_protocol'])
            priv_password = row['priv_password']
            security_engine_id = v2c.OctetString(hexValue=row['security_engine_id'])
            # SNMPv3 setup
            config.addV3User(
                snmpEngine,
                username,
                auth_protocol,
                auth_password,
                priv_protocol,
                priv_password,
                securityEngineId=security_engine_id
            )

            # SNMPv1/2c setup
            community_string = row['community_string']
            config.addV1System(snmpEngine, 'default', community_string)

def interpret_oid(oid):
    oid_mappings = {
        '1.3.6.1.2.1.1.3.0': 'SysUptime',
        '1.3.6.1.6.3.1.1.4.1.0': 'SNMPTrapOID',
        '1.3.6.1.6.3.1.1.4.3.0': 'SNMPTrapEnterprise'
    }
    return oid_mappings.get(oid, oid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SNMPReceiverApp()
    window.show()
    sys.exit(app.exec_())
