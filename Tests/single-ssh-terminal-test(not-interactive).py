import paramiko

# WARNING: this is not an interactive shell, i cannot use cd or anything else just direct commands like ls or ip a
# the following can only be used for diagnostics
hostname = "192.168.69.41"
port = 22
user = "server1"
passwd = "Pa$$w0rd"

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=user, password=passwd)
    
    while True:
        try:
            cmd = input("$> ")
            if cmd == "exit":
                break
        
            stdin, stdout, stderr = client.exec_command(f'/bin/bash -c "{cmd}"')
            print(stdout.read().decode())
        except KeyboardInterrupt:
            break

    client.close()

except Exception as err:
    print(str(err))
