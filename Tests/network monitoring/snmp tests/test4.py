from pysnmp.hlapi import *

# TODO :if there are several lines in the outputs it only prints the first line MUST FIX !!!!!!!!

def snmp_get(oid, host='192.168.69.47', community='public', port=161):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        nextCmd(SnmpEngine(),
            CommunityData(community),
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
        return results

            

oids = [
    ('NIC names', '.1.3.6.1.2.1.2.2.1.2'), 
    ('Bytes IN', '.1.3.6.1.2.1.2.2.1.10'), 
    ('Bytes OUT', '.1.3.6.1.2.1.2.2.1.16'), 
    ('Number of CPU cores', '1.3.6.1.2.1.25.3.3.1.2')
]

for name, oid in oids:
    try:
        result = snmp_get(oid)
        if result:
            print(f"{name}:", result)
    except StopIteration:
        print("No result for this OID")
    print()
