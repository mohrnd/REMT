from fabric import Connection
import os

# last resort
hostname = '192.168.69.47'
user = 'root'
port = 22 
password = 'Pa$$w0rd' 


conn = Connection(hostname, user=user, port=port, connect_kwargs={"password": password})
nothing = open(os.devnull, 'w')
output = conn.run(f'snmpwalk -v3 -l authPriv -u roadmin -a SHA -A admin123 -x AES -X admin123 192.168.69.47 1.3.6.1.2.1.2.2.1.2', warn=True, out_stream=nothing)
nothing.close()

print(output.stdout)