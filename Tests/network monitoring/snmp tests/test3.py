from pysnmp.hlapi import *

community_string = 'public'
device_ip = '192.168.69.47'
snmp_engine = SnmpEngine()
community_data = CommunityData(community_string, mpModel=1)
context = ContextData()

oids = [
    ('NIC names', '.1.3.6.1.2.1.2.2.1.2'), 
    ('NIC Status', '1.3.6.1.2.1.2.2.1.8'), 
    ('Mac address', '1.3.6.1.2.1.2.2.1.6'), 
    ('Bytes IN', '.1.3.6.1.2.1.2.2.1.10'), 
    ('Bytes OUT', '.1.3.6.1.2.1.2.2.1.16'), 
    ('1 minute Load', '.1.3.6.1.4.1.2021.10.1.3.1'), 
    ('5 minute Load', '.1.3.6.1.4.1.2021.10.1.3.2'),
    ('15 minute Load', '.1.3.6.1.4.1.2021.10.1.3.3'),
    ('percentage of user CPU time', '.1.3.6.1.4.1.2021.11.9.0'),
    ('raw user cpu time', '.1.3.6.1.4.1.2021.11.50.0'),
    ('Number of CPU cores', '1.3.6.1.2.1.25.3.3.1.2'), 
    ('percentages of system CPU time', '.1.3.6.1.4.1.2021.11.10.0'),
    ('raw system cpu time', '.1.3.6.1.4.1.2021.11.52.0'),
    ('percentages of idle CPU time', '.1.3.6.1.4.1.2021.11.11.0'),
    ('raw idle cpu time', '.1.3.6.1.4.1.2021.11.53.0'),
    ('raw nice cpu time', '.1.3.6.1.4.1.2021.11.51.0'),
    ('Total Swap Size', '.1.3.6.1.4.1.2021.4.3.0'),
    ('Available Swap Space', '.1.3.6.1.4.1.2021.4.4.0'),
    ('Total RAM in machine', '.1.3.6.1.4.1.2021.4.5.0'),
    ('Total RAM used', '.1.3.6.1.4.1.2021.4.6.0'),
    ('Total RAM Free', '.1.3.6.1.4.1.2021.4.11.0'),
    ('Total RAM Shared', '.1.3.6.1.4.1.2021.4.13.0'),
    ('Total RAM Buffered', '.1.3.6.1.4.1.2021.4.14.0'),
    ('Total Cached Memory', '.1.3.6.1.4.1.2021.4.15.0'),
    ('Path of the device for the partition', '.1.3.6.1.4.1.2021.9.1.3.1'),
    ('Total size of the disk/partion (kBytes)', '.1.3.6.1.4.1.2021.9.1.6.1'),
    ('Disk usage Pourcentage', '1.3.6.1.4.1.2021.9.1.9.1'),
    ('Available space on the disk', '.1.3.6.1.4.1.2021.9.1.7.1'),
    ('Used space on the disk', '.1.3.6.1.4.1.2021.9.1.8.1'),
    ('Percentage of space used on disk', '.1.3.6.1.4.1.2021.9.1.9.1'),
    ('Percentage of inodes used on disk', '.1.3.6.1.4.1.2021.9.1.10.1'),
    ('System Uptime', '.1.3.6.1.2.1.1.3.0')
    
    
]

def retrieve_data(oid):
    error_indication, error_status, error_index, var_binds = next(
        getCmd(snmp_engine, community_data, UdpTransportTarget((device_ip, 161)), context, ObjectType(ObjectIdentity(oid)))
    )
    if error_indication:
        return None
    else:
        return var_binds[0][1].prettyPrint()

for name, oid in oids:
    data = retrieve_data(oid)
    if data is not None:
        print(f"{name}: {data}")
    else:
        print(f"Failed to retrieve data for {name}.")

