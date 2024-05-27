from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import ntfrcv
from pysnmp.proto.api import v2c
import datetime
import logging
import csv
from .cipher_decipher_logic.CipherDecipher import *
from .notifications import win_notif

logging.basicConfig(filename='TrapsReceived.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def add_snmp_users_from_csv(CSV_File_Path, snmpEngine, MasterPassword):
    print('add_snmp_users_from_csv: ', MasterPassword)
    with open(CSV_File_Path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row['SNMPv3_username']
            auth_protocol = row['auth_Protocole']
            priv_protocol = row['Priv_Protocole']
            if auth_protocol == 'SHA':
                auth_protocol = getattr(config, 'usmHMACSHAAuthProtocol')
            elif auth_protocol == 'MD5':
                auth_protocol = getattr(config, 'usmHMACMD5AuthProtocol')
            if priv_protocol == 'DES':
                priv_protocol = getattr(config, 'usmDESPrivProtocol')
            elif priv_protocol == 'AES':
                priv_protocol = getattr(config, 'usmAesCfb128Protocol')
                
            auth_password = row['auth_password']
            priv_password = row['priv_password']
            auth_password_deciphered = get_password_no_form(MasterPassword,auth_password)
            priv_password_deciphered = get_password_no_form(MasterPassword,priv_password)
            print(auth_password_deciphered,priv_password_deciphered )
            security_engine_id = v2c.OctetString(hexValue=row['security_engine_id'])
            # SNMPv3 setup
            config.addV3User(
                snmpEngine,
                username,
                auth_protocol,
                auth_password_deciphered,
                priv_protocol,
                priv_password_deciphered,
                securityEngineId=security_engine_id
            )

def interpret_oid(oid):
    oid_mappings = {
        '1.3.6.1.2.1.1.3.0': 'SysUptime',
        '1.3.6.1.6.3.1.1.4.1.0': 'SNMPTrapOID',
        '1.3.6.1.6.3.1.1.4.3.0': 'SNMPTrapEnterprise'
    }
    return oid_mappings.get(oid, oid)

def cbFun(snmpEngine, stateReference, contextEngineId, contextName, varBinds, cbCtx):
    transport_info = snmpEngine.msgAndPduDsp.getTransportInfo(stateReference)
    log_message_parts = []  # List to collect parts of the log message

    if transport_info:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip_address = transport_info[1][0]
        log_message_parts.append(f'Trap from "{ip_address}"')
        notification_title = 'SNMP Trap Received'
        notification_message = f'Trap from {ip_address} received at {current_time}'
        notification_icon = None
        win_notif(notification_title, notification_message, notification_icon)
    else:
        log_message_parts.append('error')

    for name, val in varBinds:
        oid_str = name.prettyPrint()
        value_str = val.prettyPrint()
        interpreted_oid = interpret_oid(oid_str)
        log_message_parts.append(f'{interpreted_oid} = {value_str}')
        
        with open('..\REMT\FinishedProduct\MainInterface\Trapsviewer\TrapReceiver\OID_interpretations.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if value_str == row['OID']:
                    log_message_parts.append(f'Interpreted OID: {row["text"]}')
                    break

    log_message = ', '.join(log_message_parts)  # Join parts with ', '
    print(log_message)
    logging.info(log_message)

def main(masterpassword):
    print('main: ', masterpassword)
    snmpEngine = engine.SnmpEngine()

    # Add SNMP users from CSV
    csv_file_path = 'machines.csv'

    add_snmp_users_from_csv(csv_file_path, snmpEngine, masterpassword)
    # Transport setup
    # UDP over IPv4
    config.addTransport(
        snmpEngine,
        udp.domainName,
        udp.UdpTransport().openServerMode(('0.0.0.0', 162))
    )

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

# if __name__ == "__main__":
#     masterpassword = 'MASTERPASSWORD'
#     main(masterpassword)
