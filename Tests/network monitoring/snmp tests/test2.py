from pysnmp.hlapi import *
#works remotly but not secure
def snmp_get(oid, host='192.168.69.47', community='public', port=161):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((host, port)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
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
        for varBind in varBinds:
            return varBind[1].prettyPrint()


result = snmp_get('1.3.6.1.2.1.2.2.1.8')
if result:
    print("Result:", result)
