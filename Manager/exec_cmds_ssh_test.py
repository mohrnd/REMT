import paramiko

def run_ssh_command(hostname, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        print("Command output:")
        print(stdout.read().decode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the SSH connection
        ssh.close()
        
hostname = "192.168.69.40"
username = "manager1"
password = "Pa$$w0rd"
command_to_run = "sudo dnf update" 


run_ssh_command(hostname, username, password, command_to_run)
