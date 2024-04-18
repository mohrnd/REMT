import paramiko
from transfert import Transfer
import csv


#La commande yum check-update est utilisée pour vérifier les mises à jour disponibles, mais elle ne les installe pas automatiquement. Une fois que vous avez exécuté yum check-update et que vous avez identifié les mises à jour que vous souhaitez installer, vous pouvez ensuite utiliser la commande yum update pour effectuer réellement la mise à jour des packages.

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
    

    
    commands4 = [f"echo 'systemctl status sshd > /home/{username}/Bureau/services_status.txt' >> /home/{username}/Bureau/test.sh"]

    # Exécution des commandes sans sudo 
    results4 = test_cron2(ssh_client, commands4, password)
    print(results4)
    
    commands5 = [f"echo 'systemctl status rsyslog >> /home/{username}/Bureau/services_status.txt' >> /home/{username}/Bureau/test.sh"]

    # Exécution des commandes sans sudo 
    results5 = test_cron2(ssh_client, commands5, password)
    print(results5)
    
    
    
    commands16 = [f"echo 'systemctl status firewalld >> /home/{username}/Bureau/services_status.txt' >> /home/{username}/Bureau/test.sh"]

    # Exécution des commandes sans sudo 
    results16 = test_cron2(ssh_client, commands16, password)
    print(results16)
    
    
    
    commands17 = [f"echo 'systemctl status NetworkManager >> /home/{username}/Bureau/services_status.txt' >> /home/{username}/Bureau/test.sh"]

    # Exécution des commandes sans sudo 
    results17 = test_cron2(ssh_client, commands17, password)
    print(results17)
    
    
    commands18 = [f"echo 'systemctl status auditd >> /home/{username}/Bureau/services_status.txt' >> /home/{username}/Bureau/test.sh"]

    # Exécution des commandes sans sudo 
    results18 = test_cron2(ssh_client, commands18, password)
    print(results18)
    

    
    commands6 = [f'./Bureau/test.sh']
    # Exécution des commandes sans sudo 
    results6 = test_cron2(ssh_client, commands6, password)
    print(results6)

    # Création d'une instance de la classe Transfer
    transfer = Transfer()

    commands33 = ['hostname -f']
    results33 = test_cron2(ssh_client, commands33, password)
    # Récupérer le nom de la machine 
    machine_name = results33[0]
    
    from datetime import datetime
    
    # Récupérer la date du jour
    date_aujourdhui = datetime.now().strftime("%Y-%m-%d") 
    

    # Chemin local où vous souhaitez télécharger le fichier
    localpath =  rf'Tests/LOGS/var/logs/{machine_name}/{machine_name}__{date_aujourdhui}/journal/services_status.txt'

    # Chemin distant du fichier que vous souhaitez télécharger
    remotepath = f"/home/{username}/Bureau/services_status.txt"

    # Appel de la méthode GET pour télécharger le fichier
    result = transfer.GET(hostname, username, password, localpath, remotepath)

    # Affichage du résultat
    print(result)

    commands7 = [f'rm  Bureau/test.sh']
    # Exécution des commandes sans sudo 
    results7 = test_cron2(ssh_client, commands7, password)
    print(results7)
    
    commands8= [f'rm Bureau/services_status.txt']
    # Exécution des commandes sans sudo 
    results8 = test_cron2(ssh_client, commands8, password)
    print(results8)
    





