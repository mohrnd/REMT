import paramiko
from transfert import Transfer
import csv

def ssh_client_creation(host, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)
    return ssh_client



def test_cron2(ssh_client, commands, password):
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



if __name__ == "__main__":
    
    remote_path = '/home/test'
    
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
                hostname=ip_add
            else:
                pass


    
    # Connexion SSH
    ssh_client = ssh_client_creation(host, port, username, password)
    
    commands9= [f'touch /home/{username}/Bureau/test.sh']
    # Exécution des commandes sans sudo 
    results9 = test_cron2(ssh_client, commands9, password)
    print(results9)
    
    
    
    commands11= [f'chmod +x /home/{username}/Bureau/test.sh']
    # Exécution des commandes sans sudo 
    results11 = test_cron2(ssh_client, commands11, password)
    print(results11)
    
    
    commands2 = [f"echo '#!/bin/bash' > /home/{username}/Bureau/test.sh"]

    # Exécution des commandes sans sudo 
    results2 = test_cron2(ssh_client, commands2, password)
    print(results2)
    

    
    commands4 = [f"echo 'journalctl -p crit > /home/{username}/Bureau/system_critical.txt' >> /home/{username}/Bureau/test.sh"]

    # Exécution des commandes sans sudo 
    results4 = test_cron2(ssh_client, commands4, password)
    print(results4)
    

    
    commands6 = [f'./Bureau/test.sh']
    # Exécution des commandes sans sudo 
    results6 = test_cron2(ssh_client, commands6, password)
    print(results6)

    # Création d'une instance de la classe Transfer
    transfer = Transfer()


    commands33 = ['hostname -f']
    # Exécution des commandes sans sudo 
    results33 = test_cron2(ssh_client, commands33, password)
    # Récupérer le nom de la machine 
    machine_name = results33[0]
    
    from datetime import datetime
    
    # Récupérer la date du jour
    date_aujourdhui = datetime.now().strftime("%Y-%m-%d") 
    

    # Chemin local où vous souhaitez télécharger le fichier
    localpath =  rf'Tests/LOGS/var/logs/{machine_name}/{machine_name}__{date_aujourdhui}/journal/system_critical.txt'

    # Chemin distant du fichier que vous souhaitez télécharger
    remotepath = f"/home/{username}/Bureau/system_critical.txt"

    # Appel de la méthode GET pour télécharger le fichier
    result = transfer.GET(hostname, username, password, localpath, remotepath)

    # Affichage du résultat
    print(result)

    commands7 = [f'rm  Bureau/test.sh']
    # Exécution des commandes sans sudo 
    results7 = test_cron2(ssh_client, commands7, password)
    print(results7)
    
    commands8= [f'rm Bureau/system_critical.txt']
    # Exécution des commandes sans sudo 
    results8 = test_cron2(ssh_client, commands8, password)
    print(results8)
    
    





