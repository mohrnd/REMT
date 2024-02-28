from pysnmp.hlapi import *
##the following doesnt work
# SNMPv3 credentials
user = 'roadmin'
auth_key = 'admin123'  # Authentication password
priv_key = 'admin123'  # Privacy password
auth_proto = usmHMACSHAAuthProtocol
priv_proto = usmAesCfb128Protocol

# Rocky Linux device IP address
device_ip = '192.168.69.40'

# SNMPv3 engine creation
snmp_engine = SnmpEngine()

# Create SNMPv3 security parameters
security = UsmUserData(user, auth_key, priv_key, authProtocol=auth_proto, privProtocol=priv_proto)

# Create SNMPv3 context
context = ContextData()


oid_sys_descr = ObjectIdentity(ObjectIdentity('1.3.6.1.2.1.1.1.0'))
oid_sys_name = ObjectIdentity(ObjectIdentity('1.3.6.1.2.1.1.3.0'))
oid_sys_uptime = ObjectIdentity(ObjectIdentity('1.3.6.1.2.1.1.5.0'))

# Build SNMP GET request for each OID
get_sys_descr = getCmd(snmp_engine, security, UdpTransportTarget((device_ip, 161)), context, ObjectType(oid_sys_descr))
get_sys_name = getCmd(snmp_engine, security, UdpTransportTarget((device_ip, 161)), context, ObjectType(oid_sys_name))
get_sys_uptime = getCmd(snmp_engine, security, UdpTransportTarget((device_ip, 161)), context, ObjectType(oid_sys_uptime))

# Execute SNMP GET request and process the response
error_indication, error_status, error_index, var_binds = next(get_sys_descr)
sys_descr = var_binds[0][1].prettyPrint() if not error_indication else None

error_indication, error_status, error_index, var_binds = next(get_sys_name)
sys_name = var_binds[0][1].prettyPrint() if not error_indication else None

error_indication, error_status, error_index, var_binds = next(get_sys_uptime)
sys_uptime = var_binds[0][1].prettyPrint() if not error_indication else None

# Print system information
if sys_descr:
    print("1:", sys_descr)
else:
    print("Failed to retrieve system description.")
if sys_name:
    print("2:", sys_name)
else:
    print("Failed to retrieve system name.")
if sys_uptime:
    print("3:", sys_uptime)
else:
    print("Failed to retrieve system uptime.")
