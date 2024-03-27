from pysnmp.hlapi import *

def snmp_get_v3(oid, username, authkey, privkey, host, port=161, auth_protocol=usmHMACSHAAuthProtocol, priv_protocol=usmAesCfb128Protocol):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        nextCmd(SnmpEngine(),
            UsmUserData(username, authkey, privkey, auth_protocol, priv_protocol),
            UdpTransportTarget((host, port)),
            ContextData(),
            ObjectType(ObjectIdentity(oid)),
            lexicographicMode=False)
    )

    if errorIndication:
        print(errorIndication)
        return None
    elif errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'
            )
        )
        return None
    else:
        results = []
        for varBind in varBinds:
            results.append(varBind[1].prettyPrint())
        return varBinds

            

oids = [
    ('NIC names', '.1.3.6.1.2.1.2.2.1.2'), 
    ('Bytes IN', '.1.3.6.1.2.1.2.2.1.10'), 
    ('Bytes OUT', '.1.3.6.1.2.1.2.2.1.16'), 
    ('Number of CPU cores', '1.3.6.1.2.1.25.3.3.1.2')
]

username = 'roadmin'
authkey = 'admin123'
privkey = 'admin123'
hostname = '192.168.69.47'
for name, oid in oids:
    try:
        result = snmp_get_v3(oid, username, authkey, privkey, hostname)
        if result:
            print(f"{name}:", result)
    except StopIteration:
        print("No result for this OID")
    print()
