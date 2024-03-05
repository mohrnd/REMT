import paramiko

hostname = "192.168.69.38"
username = "manager1"
password = "Pa$$w0rd"
port = 22

paramiko.util.log_to_file("paramiko.log")

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname, username=username, password=password)
    sftp = ssh.open_sftp()
    local_path = r"C:\Users\BALLS2 (rip BALLS)\Desktop\REMT\.vscode\settings.json"
    remote_path = "/home/manager1/Desktop/test2.py" 


    sftp.put(local_path, remote_path)
    print(f"File '{local_path}' successfully sent to '{remote_path}'")
    
    sftp.get(remote_path, local_path)

    print(f"File '{local_path}' successfully sent to '{remote_path}'")

    sftp.close()
    ssh.close()

except paramiko.AuthenticationException as auth_exception:
    print("Authentication failed:", auth_exception)
except paramiko.SSHException as ssh_exception:
    print("SSH connection failed:", ssh_exception)
except Exception as e:
    print("An error occurred:", e)
