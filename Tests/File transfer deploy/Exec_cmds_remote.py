import paramiko

def run_ssh_command(hostname, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(command)
        return stdout.read().decode('utf-8')
    except Exception as e:
        return f"Error: {e}"
    finally:
        ssh.close()
        


#usage
#run_ssh_command(hostname, username, password, command_to_run)
