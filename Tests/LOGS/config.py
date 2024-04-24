### ce code doit etre executé a linstallation ####


import paramiko
import csv 

def ssh_client_creation(host, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)
    return ssh_client

def check_histtimeformat(ssh_client):
    # Commande pour rechercher la ligne dans le fichier .bashrc
    command = "grep -qxF 'export HISTTIMEFORMAT=\"%F %T\"' ~/.bashrc && echo 'found' || echo 'not found'"
    
    # Exécute la commande sur le serveur distant
    stdin, stdout, stderr = ssh_client.exec_command(command)
    
    # Récupère le résultat de la commande
    result = stdout.read().decode().strip()
    
    # Vérifie si la ligne a été trouvée dans le fichier
    if result == "found":
        return True
    else:
        return False

def add_histtimeformat(ssh_client):
    # Commande pour ajouter la ligne dans le fichier .bashrc
    command = "echo 'export HISTTIMEFORMAT=\"%F %T\"' >> ~/.bashrc"
    
    # Exécute la commande sur le serveur distant
    ssh_client.exec_command(command)

def config(machine_name, ip_add,csv_file):
    


    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if machine_name == row['Machine_Name'] and ip_add == row['ip_add']:
                port = row['port']
                username = row['linux_username']
                password = row['password']
                host=ip_add
            else:
                pass

    # Connexion SSH
    ssh_client = ssh_client_creation(host, port, username, password)
    
    # Vérifie si la ligne existe déjà dans .bashrc
    if not check_histtimeformat(ssh_client):
        # Ajoute la ligne si elle n'existe pas déjà
        add_histtimeformat(ssh_client)
        print("Line added to .bashrc")
    else:
        print("Line already exists in .bashrc")

    # Ferme la connexion SSH
    ssh_client.close()

    
