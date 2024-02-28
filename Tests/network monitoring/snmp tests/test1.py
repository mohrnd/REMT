from pysnmp.hlapi import *

# SNMPv3 parameters
snmp_engine = SnmpEngine()
security = UsmUserData('roadmin', 'admin123', 'admin123', authProtocol=usmHMACSHAAuthProtocol, privProtocol=usmAesCfb128Protocol)

# Target parameters
target_address = UdpTransportTarget(('192.168.69.40', 161))

# SNMP walk operation
error_indication, error_status, error_index, var_binds = next(
    getCmd(snmp_engine,security,target_address,ContextData(),ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0'))))

if error_indication:
    print(f"SNMP walk failed: {error_indication}")
else:
    if error_status:
        print(f"SNMP walk failed: {error_status.prettyPrint()}")
    else:
        for var_bind in var_binds:
            print(f"success ! {var_bind[0]} = {var_bind[1]}")
