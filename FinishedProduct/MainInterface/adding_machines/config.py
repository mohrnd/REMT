import paramiko


def ssh_client_creation(host, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)
    return ssh_client

def check_histtimeformat(ssh_client):
    command = "grep -qxF 'export HISTTIMEFORMAT=\"%F %T\"' ~/.bashrc && echo 'found' || echo 'not found'"
    stdin, stdout, stderr = ssh_client.exec_command(command)
    result = stdout.read().decode().strip()
    if result == "found":
        return True
    else:
        return False

def add_histtimeformat(ssh_client):
    # Commande pour ajouter la ligne dans le fichier .bashrc
    command = "echo 'export HISTTIMEFORMAT=\"%F %T\"' >> ~/.bashrc"
    
    # Exécute la commande sur le serveur distant
    ssh_client.exec_command(command)

def config(host, port, username, password):
    ssh_client = ssh_client_creation(host, port, username, password)
    if not check_histtimeformat(ssh_client):
        add_histtimeformat(ssh_client)
        return "Line added to .bashrc"
    else:
        return "Line already exists in .bashrc"


