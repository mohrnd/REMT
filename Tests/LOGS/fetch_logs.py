from scp import SCPClient
import paramiko
import os
import shutil
import subprocess
from fabric import Connection
import csv
from datetime import datetime

def ssh_client_creation(host, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)
    return ssh_client

def test_cron(ssh_client, commands, password):
    results2 = []  # Liste pour stocker les résultats des commandes
    
    for command in commands:
        # Exécute la commande spécifiée sur le serveur distant sans sudo
        stdin, stdout, stderr = ssh_client.exec_command(command, get_pty=True)
        
        # Récupère le résultat de la commande
        result2 = stdout.read().decode().strip()
        
        # Vérifie s'il y a eu des erreurs
        error = stderr.read().decode().strip()
        if error:
            results2.append(error)
        else:
            # Stocke le résultat dans la liste des résultats
            results2.append(result2)
    
    return results2



def download_folder(remote_host, remote_path, local_path, username, password):
    # Créer une connexion SSH
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Se connecter à la machine distante
        ssh_client.connect(remote_host, username=username, password=password)

        # Initialiser SCPClient
        with SCPClient(ssh_client.get_transport()) as scp:
            # Télécharger le dossier distant
            scp.get(remote_path, local_path, recursive=True)

    except Exception as e:
        print(f"Erreur lors du téléchargement du dossier: {e}")

    finally:
        # Fermer la connexion SSH
        ssh_client.close()

def fetch():

    
    csv_file = "Tests/LOGS/users.csv"
    
    machine_name = "localhost"
    ip_add = "192.168.1.21"

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if machine_name == row['Machine_Name'] and ip_add == row['ip_add']:
                port = 22  # Port par défaut pour SSH
                username = row['linux_username']
                password = row['password']
                host=ip_add
                ssh_client = ssh_client_creation(host, port, username, password)
            else:
                pass

    # Établir une connexion avec les informations fournies
    conn = Connection(host, user=username, port=port, connect_kwargs={"password": password})


    # Utiliser la méthode sudo() pour exécuter la commande avec les privilèges sudo,
    # en spécifiant le mot de passe
    result1 = conn.sudo('rsync -av /var/log/ /home/journal', password=password, warn=True)
        
    result2 = conn.sudo('chmod -R a+rwx /home/journal', password=password, warn=True)

    commands = ['rm /home/journal/README']
    # Exécution des commandes avec sudo 
    results = test_cron(ssh_client, commands, password)
    print(results) 


    # Récupérer le nom de la machine

    commands3 = ['hostname -f']
    # Exécution des commandes sans sudo 
    results3 = test_cron(ssh_client, commands3, password)
    # Récupérer le nom de la machine 
    machine_name = results3[0]
    
    # Récupérer la date du jour
    date_aujourdhui = datetime.now().strftime("%Y-%m-%d")  

    # Spécifier le chemin local en utilisant le nom de la machine
    local_path_verify = rf'../../REMT/Tests/LOGS/var/logs/{machine_name}/{machine_name}__{date_aujourdhui}'
    

    # Supprimer le dossier existant s'il existe déjà
    if os.path.exists(local_path_verify):
        shutil.rmtree(local_path_verify)
        print("Le dossier existant a été supprimé.")

    # Spécifier le chemin local en utilisant le nom de la machine
    local_path = rf'../REMT/Tests/LOGS/var/logs/{machine_name}/{machine_name}__{date_aujourdhui}'
    
    # Créer le répertoire s'il n'existe pas déjà
    os.makedirs(local_path, exist_ok=True)


    # Télécharger le dossier
    remote_path = '/home/journal'
    download_folder(ip_add, remote_path, local_path, username, password)


    result4 = conn.sudo('rm -r /home/journal', password=password, warn=True)

    
    script_path1 = './Tests/LOGS/activites_de_configuration.py'
    subprocess.run(["python", script_path1])
    
    script_path2 = './Tests/LOGS/activites_du_parefeu.py'
    subprocess.run(["python", script_path2])

    script_path3 = './Tests/LOGS/activites_memoire.py'
    subprocess.run(["python", script_path3])


    
    script_path5 = './Tests/LOGS/activités_ssh.py'
    subprocess.run(["python", script_path5])

    script_path6 = './Tests/LOGS/activites_usb.py'
    subprocess.run(["python", script_path6])
    
    script_path7 = './Tests/LOGS/Advanced _Configuration_and_Power_Interface_events.py'
    subprocess.run(["python", script_path7])

    script_path8 = './Tests/LOGS/cmd_history.py'
    subprocess.run(["python", script_path8])

    script_path9 = './Tests/LOGS/cnx_actives.py'
    subprocess.run(["python", script_path9])

    script_path10 = './Tests/LOGS/device_detection.py'
    subprocess.run(["python", script_path10])
    
    script_path11 = './Tests/LOGS/kernel_logs.py'
    subprocess.run(["python", script_path11])

    script_path12 = './Tests/LOGS/processus.py'
    subprocess.run(["python", script_path12])
    
    script_path13 = './Tests/LOGS/status_des_services.py'
    subprocess.run(["python", script_path13])

    script_path14 = './Tests/LOGS/sys_alert.py'
    subprocess.run(["python", script_path14])

    script_path15 = './Tests/LOGS/sys_critical.py'
    subprocess.run(["python", script_path15])

    script_path16 = './Tests/LOGS/sys_debug.py'
    subprocess.run(["python", script_path16])

    script_path17 = './Tests/LOGS/sys_emerg.py'
    subprocess.run(["python", script_path17])

    script_path18 = './Tests/LOGS/sys_error.py'
    subprocess.run(["python", script_path18])

    script_path19 = './Tests/LOGS/sys_info.py'
    subprocess.run(["python", script_path19])

    script_path20 = './Tests/LOGS/sys_notice.py'
    subprocess.run(["python", script_path20])
    
    script_path21 = './Tests/LOGS/sys_warning.py'
    subprocess.run(["python", script_path21])

    script_path22 = './Tests/LOGS/system_boots.py'
    subprocess.run(["python", script_path22])
    
    script_path23 = './Tests/LOGS/transactions_effectuées.py'
    subprocess.run(["python", script_path23])
    
    script_path24 = './Tests/LOGS/utilisation_disque.py'
    subprocess.run(["python", script_path24])
    

def main():
    fetch()


