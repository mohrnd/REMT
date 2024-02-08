import paramiko

hostname = "192.168.69.42"
username = "root"
password = "Pa$$w0rd"
port = 22

paramiko.util.log_to_file("paramiko.log")

ssh = paramiko.SSHClient()

# Automatically add unknown hosts to the `known_hosts` file
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname, username=username, password=password)
    sftp = ssh.open_sftp()
    local_path = "/home/manager1/Desktop/test2.py"
    remote_path = "/home/server1/Desktop/test2.py" 


    sftp.put(local_path, remote_path)

    print(f"File '{local_path}' successfully sent to '{remote_path}'")

    sftp.close()
    ssh.close()

except paramiko.AuthenticationException as auth_exception:
    print("Authentication failed:", auth_exception)
except paramiko.SSHException as ssh_exception:
    print("SSH connection failed:", ssh_exception)
except Exception as e:
    print("An error occurred:", e)
