from pysnmp.hlapi import *


# FETCH UPTIME

# SNMPv3 parameters
snmp_engine = SnmpEngine()
security = UsmUserData('roadmin', 'admin123', 'admin123', authProtocol=usmHMACSHAAuthProtocol, privProtocol=usmAesCfb128Protocol)
ip_address = '192.168.69.47'
# Target parameters
target_address = UdpTransportTarget((ip_address, 161))

# SNMP walk operation
error_indication, error_status, error_index, var_binds = next(
    getCmd(snmp_engine, security, target_address, ContextData(), ObjectType(ObjectIdentity('1.3.6.1.2.1.1.3.0'))))

if error_indication:
    print(f"SNMP walk failed: {error_indication}")
else:
    if error_status:
        print(f"SNMP walk failed: {error_status.prettyPrint()}")
    else:
        for var_bind in var_binds:
            sys_uptime_hundredths = int(var_bind[1])
            sys_uptime_seconds = sys_uptime_hundredths // 100
            sys_uptime_minutes = sys_uptime_seconds // 60
            sys_uptime_hours = sys_uptime_minutes // 60
            sys_uptime_days = sys_uptime_hours // 24
            if sys_uptime_minutes <= 60:
                print(f"{ip_address}'s Uptime: {sys_uptime_minutes} minutes")
            elif sys_uptime_minutes >= 60:
                print(f"{ip_address}'s Uptime: {sys_uptime_hours} Hours")
            elif sys_uptime_hours >= 24:
                print(f"{ip_address}'s Uptime: {sys_uptime_days} Days")
