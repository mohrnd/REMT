import paramiko
from .transfert import Transfer
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



def  fetch18 (machine_name, ip_add, password,port,username,host,hostname,local_path_in,csv_file,filename):
    
    remote_path = '/home/test'
    
    





    
    # Connexion SSH
    ssh_client = ssh_client_creation(host, port, username, password)
    
    commands9= [f'touch /home/{username}/Desktop/test.sh']
    # Exécution des commandes sans sudo 
    results9 = test_cron2(ssh_client, commands9, password)
    #print(results9)
    
    
    
    commands11= [f'chmod +x /home/{username}/Desktop/test.sh']
    # Exécution des commandes sans sudo 
    results11 = test_cron2(ssh_client, commands11, password)
    #print(results11)
    
    
    commands2 = [f"echo '#!/bin/bash' > /home/{username}/Desktop/test.sh"]

    # Exécution des commandes sans sudo 
    results2 = test_cron2(ssh_client, commands2, password)
    #print(results2)
    

    
    commands4 = [f"echo 'journalctl -p emerg > /home/{username}/Desktop/system_emerg.txt' >> /home/{username}/Desktop/test.sh"]

    # Exécution des commandes sans sudo 
    results4 = test_cron2(ssh_client, commands4, password)
    #print(results4)
    

    
    commands6 = [f'./Desktop/test.sh']
    # Exécution des commandes sans sudo 
    results6 = test_cron2(ssh_client, commands6, password)
    #print(results6)

    # Création d'une instance de la classe Transfer
    transfer = Transfer()



    from datetime import datetime
    
    # Récupérer la date du jour
    date_aujourdhui = datetime.now().strftime("%d-%m-%Y") 
    
    maintenant = datetime.now()

    # Formater la date et l'heure selon vos besoins
    heure = maintenant.strftime("%H-%M")
    

    # Définition de la variable add
    add = rf'{machine_name}/{filename}/journal/system_emerg.txt'

    # local_path_in est  Chemin local initial

    # Ajout de la valeur de la variable add au chemin local
    localpath = local_path_in + add
    
    # Chemin distant du fichier que vous souhaitez télécharger
    remotepath = f"/home/{username}/Desktop/system_emerg.txt"

    # Appel de la méthode GET pour télécharger le fichier
    result = transfer.GET(hostname, username, password, localpath, remotepath)

    # Affichage du résultat
    

    commands7 = [f'rm  Desktop/test.sh']
    # Exécution des commandes sans sudo 
    results7 = test_cron2(ssh_client, commands7, password)
    #print(results7)
    
    commands8= [f'rm Desktop/system_emerg.txt']
    # Exécution des commandes sans sudo 
    results8 = test_cron2(ssh_client, commands8, password)
    #print(results8)
    
    
    return result
    





