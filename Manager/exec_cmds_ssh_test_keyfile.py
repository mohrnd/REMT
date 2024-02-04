import paramiko

def run_ssh_command(hostname, username, private_key_path, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        private_key = paramiko.RSAKey(filename=private_key_path)
        ssh.connect(hostname, username=username, pkey=private_key)
        stdin, stdout, stderr = ssh.exec_command(command)
        print("Command output:")
        print(stdout.read().decode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        ssh.close()

hostname = "192.168.68.43"
username = "server1"
private_key_path = r"C:\Users\BALLS2 (rip BALLS)\Desktop\REST-PFE\REST-Remote-Execution-and-Security-Toolkit-Linux\Manager\id_rsa.pub"  
command_to_run = "ls -l"  

run_ssh_command(hostname, username, private_key_path, command_to_run)
