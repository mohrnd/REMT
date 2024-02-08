import paramiko

def copy_files(source_host, source_username, source_password, source_path, destination_host, destination_username, destination_password, destination_path):
    
    source_host = '192.168.1.32'
    source_username='user1'
    source_password='Didine.2003'
    source_path='/home/user1/Bureau/test.py'
    destination_host='192.168.1.33'
    destination_username='user2'
    destination_password='Didine.2003'
    destination_path='/home/user2/Bureau/test.py'
    
    # Se connecter au serveur source
    source_client = paramiko.SSHClient()
    source_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    source_client.connect(source_host, username=source_username, password=source_password)

    # Se connecter au serveur de destination
    destination_client = paramiko.SSHClient()
    destination_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    destination_client.connect(destination_host, username=destination_username, password=destination_password)

    # Ouvrir les canaux SFTP sur les deux serveurs
    source_sftp = source_client.open_sftp()
    destination_sftp = destination_client.open_sftp()

    # Copier le fichier du serveur source au serveur de destination
    source_file = source_sftp.open(source_path, 'r')
    destination_sftp.putfo(source_file, destination_path)
    source_file.close()

    # Fermer les connexions
    source_sftp.close()
    destination_sftp.close()
    source_client.close()
    destination_client.close()

# Utilisation de la fonction pour copier un fichier
copy_files('source_host', 'source_username', 'source_password', '/chemin/vers/fichier/source.txt', 'destination_host', 'destination_username', 'destination_password', '/chemin/vers/fichier/destination.txt')
