from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
from pysnmp.proto.api import v2c
import datetime
import logging
import csv

logging.basicConfig(filename='TrapsReceived.log', level=logging.INFO, format='%(asctime)s - %(message)s')

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

# Initialize SNMP engine
snmpEngine = engine.SnmpEngine()

# Add SNMP users from CSV
csv_file_path = r'C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\network monitoring\snmp tests\snmp_users.csv'
add_snmp_users_from_csv(csv_file_path, snmpEngine)

# Transport setup
# UDP over IPv4
config.addTransport(
    snmpEngine,
    udp.domainName,
    udp.UdpTransport().openServerMode(('0.0.0.0', 162))
)

# Define a function to interpret OID values
def interpret_oid(oid):
    oid_mappings = {
        '1.3.6.1.2.1.1.3.0': 'SysUptime',
        '1.3.6.1.6.3.1.1.4.1.0': 'SNMPTrapOID',
        '1.3.6.1.6.3.1.1.4.3.0': 'SNMPTrapEnterprise'
    }
    return oid_mappings.get(oid, oid)

# Callback function for receiving notifications
def cbFun(snmpEngine, stateReference, contextEngineId, contextName,
          varBinds, cbCtx):
    transport_info = snmpEngine.msgAndPduDsp.getTransportInfo(stateReference)
    if transport_info:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip_address = transport_info[1][0]
        print(current_time,'Trap from "%s"' % (ip_address))
        logging.info('Trap from "%s"', ip_address)

    else:
        print('error')
        logging.error('error')

    for name, val in varBinds:
        oid_str = name.prettyPrint()
        value_str = val.prettyPrint()
        interpreted_oid = interpret_oid(oid_str)
        print('%s = %s' % (interpreted_oid, value_str))
        logging.info('%s = %s', interpreted_oid, value_str)
        with open(r'C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\Tests\network monitoring\snmp tests\OID_interpretations.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if value_str == row['OID']:
                    print(' Interpreted OID: ', row['text'])
                    logging.info(' Interpreted OID: %s', row['text'])
                else:
                    pass

# Register SNMP Application at the SNMP engine
ntfrcv.NotificationReceiver(snmpEngine, cbFun)

# Run I/O dispatcher which would receive queries and send confirmations
try:
    snmpEngine.transportDispatcher.jobStarted(1)  # this job would never finish
    snmpEngine.transportDispatcher.runDispatcher()
except Exception as e:
    print("Error:", e)
finally:
    snmpEngine.transportDispatcher.closeDispatcher()
