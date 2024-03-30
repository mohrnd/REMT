from scp import SCPClient
import paramiko
import os
import shutil
import subprocess
from fabric import Connection
import csv

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

if __name__ == "__main__":
    

    
    csv_file = "Tests/LOGS/users.csv"

    # Liste pour stocker les données lues depuis le fichier CSV
    data_from_csv = []

    # Lire les données depuis le fichier CSV
    with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                data_from_csv.append(row)

    # Vérifier si des données ont été lues depuis le fichier CSV
    if len(data_from_csv) > 1:  # Vérifier si des données autres que l'en-tête ont été lues
            host, port, username, password, hostname = data_from_csv[1]  # Récupérer les valeurs depuis la deuxième ligne (première ligne étant l'en-tête)

    ssh_client = ssh_client_creation(host, port, username, password)

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

    # Spécifier le chemin local en utilisant le nom de la machine
    local_path_verify = rf'../../REMT/Tests/LOGS/var/logs/{machine_name}'
    

    # Supprimer le dossier existant s'il existe déjà
    if os.path.exists(local_path_verify):
        shutil.rmtree(local_path_verify)
        print("Le dossier existant a été supprimé.")

    # Spécifier le chemin local en utilisant le nom de la machine
    local_path = rf'../REMT/Tests/LOGS/var/logs/{machine_name}'
    
    # Créer le répertoire s'il n'existe pas déjà
    os.makedirs(local_path, exist_ok=True)


    # Télécharger le dossier
    remote_path = '/home/journal'
    download_folder(host, remote_path, local_path, username, password)


    result4 = conn.sudo('rm -r /home/journal', password=password, warn=True)

    
    script_path1 = '../REMT/Tests/LOGS/activites_de_configuration.py'
    subprocess.run(["python", script_path1])

    script_path2 = '../REMT/Tests/LOGS/activites_du_parefeu.py'
    subprocess.run(["python", script_path2])

    script_path3 = '../REMT/Tests/LOGS/activites_memoire.py'
    subprocess.run(["python", script_path3])


    
    script_path5 = '../REMT/Tests/LOGS/activités_ssh.py'
    subprocess.run(["python", script_path5])

    script_path6 = '../REMT/Tests/LOGS/activites_usb.py'
    subprocess.run(["python", script_path6])
    
    script_path7 = '../REMT/Tests/LOGS/Advanced _Configuration_and_Power_Interface_events.py'
    subprocess.run(["python", script_path7])

    script_path8 = '../REMT/Tests/LOGS/cmd_history.py'
    subprocess.run(["python", script_path8])

    script_path9 = '../REMT/Tests/LOGS/cnx_actives.py'
    subprocess.run(["python", script_path9])

    script_path10 = '../REMT/Tests/LOGS/device_detection.py'
    subprocess.run(["python", script_path10])
    
    script_path11 = '../REMT/Tests/LOGS/kernel_logs.py'
    subprocess.run(["python", script_path11])

    script_path12 = '../REMT/Tests/LOGS/processus.py'
    subprocess.run(["python", script_path12])
    
    script_path13 = '../REMT/Tests/LOGS/status_des_services.py'
    subprocess.run(["python", script_path13])

    script_path14 = '../REMT/Tests/LOGS/sys_alert.py'
    subprocess.run(["python", script_path14])

    script_path15 = '../REMT/Tests/LOGS/sys_critical.py'
    subprocess.run(["python", script_path15])

    script_path16 = '../REMT/Tests/LOGS/sys_debug.py'
    subprocess.run(["python", script_path16])

    script_path17 = '../REMT/Tests/LOGS/sys_emerg.py'
    subprocess.run(["python", script_path17])

    script_path18 = '../REMT/Tests/LOGS/sys_error.py'
    subprocess.run(["python", script_path18])

    script_path19 = '../REMT/Tests/LOGS/sys_info.py'
    subprocess.run(["python", script_path19])

    script_path20 = '../REMT/Tests/LOGS/sys_notice.py'
    subprocess.run(["python", script_path20])
    
    script_path21 = '../REMT/Tests/LOGS/sys_warning.py'
    subprocess.run(["python", script_path21])

    script_path22 = '../REMT/Tests/LOGS/system_boots.py'
    subprocess.run(["python", script_path22])
    
    script_path23 = '../REMT/Tests/LOGS/transactions_effectuées.py'
    subprocess.run(["python", script_path23])
    
    script_path24 = '../REMT/Tests/LOGS/utilisation_disque.py'
    subprocess.run(["python", script_path24])
    
    
    #### pour 4 et 25 execute les si t'as une cnx internet
    
    #script_path4 = '../REMT/Tests/LOGS/activités_reseau.py'
    #subprocess.run(["python", script_path4])
    
    #script_path25 = '../REMT/Tests/LOGS/vérifier_les_mises_à_jour_disponibles.py'
    #subprocess.run(["python", script_path25])
