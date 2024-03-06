"""
Multiple SNMP USM users
+++++++++++++++++++++++

Receive SNMP TRAP/INFORM messages with the following options:

* SNMPv1/SNMPv2c
  * with SNMP community "public"
  * over IPv4/UDP, listening at 127.0.0.1:162

* SNMPv3
* with USM users:

  * 'usr-md5-des', auth: MD5, priv DES, ContextEngineId: 8000000001020304
  * 'usr-md5-none', auth: MD5, priv NONE, ContextEngineId: 8000000001020304
  * 'usr-sha-aes128', auth: SHA, priv AES, ContextEngineId: 8000000001020304

* over IPv4/UDP, listening at 127.0.0.1:162
* print received data on stdout

Either of the following Net-SNMP commands will send notifications to this
receiver:

| $ snmptrap -v2c -c public 127.0.0.1:162 123 1.3.6.1.6.3.1.1.5.1 1.3.6.1.2.1.1.5.0 s test

| $ snmptrap -v3 -u usr-md5-des -l authPriv -A authkey1 -X privkey1 -e 8000000001020304 127.0.0.1 123 1.3.6.1.6.3.1.1.5.1
| $ snmptrap -v3 -u usr-md5-none -l authNoPriv -A authkey1 -e 8000000001020304 127.0.0.1 123 1.3.6.1.6.3.1.1.5.1
| $ snmpinform -v3 -u usr-sha-aes128 -l authPriv -a SHA -A authkey1 -x AES -X privkey1 127.0.0.1 123 1.3.6.1.6.3.1.1.5.1




EVERYTHING WORKS CORRECTLY !!
snmptrap -v3 -u roadmin -l authPriv -a SHA -A admin123 -x AES -X admin123 -e 0x80001f8880ad8ba63fe904de6500000000 192.168.69.45:162 123 1.3.6.1.6.3.1.1.5.1
snmpinform -v3 -u roadmin -l authPriv -a SHA -A admin123 -x AES -X admin123 192.168.69.45 6969 1.3.6.1.6.3.1.1.5.1

trapsess -v3 -u roadmin -l authPriv -a SHA -A admin123 -x AES -X admin123 192.168.69.45



"""#
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
from pysnmp.proto.api import v2c

# Create SNMP engine with autogenernated engineID and pre-bound
# to socket transport dispatcher
snmpEngine = engine.SnmpEngine()

# Transport setup

# UDP over IPv4
config.addTransport(
    snmpEngine,
    udp.domainName,
    udp.UdpTransport().openServerMode(('192.168.69.45', 162))
)

# SNMPv1/2c setup
config.addV1System(snmpEngine, 'default', 'teststring')

# SNMPv3/USM setup

# user: usr-md5-des, auth: MD5, priv DES
config.addV3User(
    snmpEngine, 'roadmin',
    config.usmHMACMD5AuthProtocol, 'admin123',
    config.usmDESPrivProtocol, 'admin123'
)

# user: usr-md5-des, auth: MD5, priv DES, securityEngineId: 80001f8880ad8ba63fe904de6500000000
# this USM entry is used for TRAP receiving purposes
config.addV3User(
    snmpEngine, 'roadmin',
    config.usmHMACMD5AuthProtocol, 'admin123',
    config.usmDESPrivProtocol, 'admin123',
    securityEngineId=v2c.OctetString(hexValue='80001f8880ad8ba63fe904de6500000000')
)

# user: usr-md5-none, auth: MD5, priv NONE
config.addV3User(
    snmpEngine, 'roadmin',
    config.usmHMACMD5AuthProtocol, 'admin123'
)

# user: usr-md5-none, auth: MD5, priv NONE, securityEngineId: 8000000001020304
# this USM entry is used for TRAP receiving purposes
config.addV3User(
    snmpEngine, 'roadmin',
    config.usmHMACMD5AuthProtocol, 'admin123',
    securityEngineId=v2c.OctetString(hexValue='80001f8880ad8ba63fe904de6500000000')
)

# user: usr-sha-aes128, auth: SHA, priv AES
config.addV3User(
    snmpEngine, 'roadmin',
    config.usmHMACSHAAuthProtocol, 'admin123',
    config.usmAesCfb128Protocol, 'admin123'
)
# user: usr-sha-aes128, auth: SHA, priv AES, securityEngineId: 8000000001020304
# this USM entry is used for TRAP receiving purposes
config.addV3User(
    snmpEngine, 'roadmin',
    config.usmHMACSHAAuthProtocol, 'admin123',
    config.usmAesCfb128Protocol, 'admin123',   
    securityEngineId=v2c.OctetString(hexValue='80001f8880ad8ba63fe904de6500000000')
)

# Callback function for receiving notifications
# noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
def cbFun(snmpEngine, stateReference, contextEngineId, contextName,
          varBinds, cbCtx):
    print('Notification from ContextEngineId "%s", ContextName "%s"' % (
        contextEngineId.prettyPrint(), contextName.prettyPrint()))
    for name, val in varBinds:
        print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))


# Register SNMP Application at the SNMP engine
ntfrcv.NotificationReceiver(snmpEngine, cbFun)

snmpEngine.transportDispatcher.jobStarted(1)  # this job would never finish

# Run I/O dispatcher which would receive queries and send confirmations
try:
    snmpEngine.transportDispatcher.runDispatcher()
except:
    snmpEngine.transportDispatcher.closeDispatcher()
    raise


'''
snmptrap -v 3 -l authPriv -u roadmin -a SHA -A admin123 -x AES -X admin123 -e 0x80001f8880ad8ba63fe904de6500000000 192.168.69.45:162 '' 1.3.6.1.4.1.8072.9999.9999 1.3.6.1.4.1.8072.9999.9999 s "gang shit"
!!!!!!!!!!!!! running external commands (exec, extend, pass) !!!!!!!!!!!!!
http://www.net-snmp.org/docs/man/snmpd.conf.html#lbAX
'''