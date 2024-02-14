from customtkinter import *
import paramiko
import sys
import logging
import time
import getpass

# Configuration du module logging
logging.basicConfig(filename='ssh_session.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Récupérer le nom de l'utilisateur actuel
current_user = getpass.getuser()

# Variable globale pour stocker le répertoire actuel
current_directory = None

# Liste pour stocker l'historique des commandes
command_history = []

# Variable pour suivre l'état de la connexion
connected_status_displayed = False

def execute_command(command):
    global current_directory, connected_status_displayed  # Référence à la variable globale

    start_time = time.time()  # Heure de début de l'exécution de la commande

    if command.strip() == 'clear':
        output_text.delete("1.0", "end")  # Effacer le contenu du widget de texte
        return  # Sortir de la fonction après avoir effacé le contenu
    elif command.strip() == 'history':
        # Afficher le prompt et la commande "history"
        output_text.insert("end", f"[{current_user}@localhost {current_directory if current_directory else '~'}]$ history\n")
        # Afficher l'historique des commandes
        output_text.insert("end", "\n".join(command_history) + "\n\n")
        return
    elif command.strip() == 'exit':
        # Terminer l'application
        app.quit()
        return
    elif command.startswith('cd '):
        # Si la commande commence par "cd ", alors c'est une commande de changement de répertoire
        # Nous devons extraire le chemin du répertoire de la commande
        path = command.split(' ', 1)[1]  # Récupérer le chemin du répertoire à changer
        current_directory = path  # Mettre à jour le répertoire actuel
        ssh_command = f'cd "{path}" && pwd'  # Combinaison de la commande cd et pwd pour obtenir le nouveau répertoire courant
    else:
        # Pour les autres commandes, nous exécutons directement la commande
        if current_directory:
            ssh_command = f'cd "{current_directory}" && {command}'
        else:
            ssh_command = command

    # Informations de connexion SSH
    host = '192.168.1.33'
    port = 22
    username = 'user2'
    password = 'Didine.2003'

    try:
        # Connexion SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        
        # Affichage du statut de connexion si ce n'est pas déjà affiché
        if not connected_status_displayed:
            output_text_frame1.insert("end", f"Connected to {username}@localhost by {current_user}!\n")
            connected_status_displayed = True

        # Ajouter la commande à l'historique
        command_history.append(command)

        # Affichage du prompt personnalisé
        output_text.insert("end", f"[{username}@localhost {current_directory if current_directory else '~'}]$ {command}\n")

        # Exécution de la commande sur le shell distant
        stdin, stdout, stderr = ssh.exec_command(ssh_command)

        # Récupération de la sortie de la commande
        output = stdout.read().decode('utf-8')

        # Récupération de la sortie d'erreur
        errors = stderr.read().decode('utf-8')

        # Affichage du résultat dans le widget de texte
        output_text.insert("end", output)
        output_text.insert("end", errors)

        # Ajout d'une ligne vide après le résultat
        output_text.insert("end", "\n")

    except Exception as e:
        # Gestion des exceptions
        output_text.insert("end", f"Error executing command: {e}\n")
        logging.error(f"Error executing command: {e}")

    finally:
        # Fermeture de la connexion SSH
        if ssh:
            ssh.close()

        # Heure de fin de l'exécution de la commande
        end_time = time.time()
        execution_time = end_time - start_time  # Calcul du temps d'exécution

        # Enregistrement dans le fichier journal avec les informations sur l'utilisateur et la machine
        logging.info(f"Command executed by {current_user} on {host}: '{command}', Execution time: {execution_time:.2f} seconds, Result: {output.strip()}")

# Initialisation de l'application tkinter
app = CTk()
app.resizable(width=False, height=False)  # Empêcher le redimensionnement de la fenêtre
set_appearance_mode("dark")  # Mode d'apparence sombre
set_default_color_theme("dark-blue")  # Thème de couleur par défaut
app.title("SSH_SESSION")  # Titre de la fenêtre
app.geometry("750x550")  # Dimensions de la fenêtre

# Création d'un cadre pour le texte de sortie.
frame_principal = CTkFrame(app,fg_color="#140716")
frame_principal.pack(padx=0, pady=0, fill="both", expand=True)

# Création d'un cadre pour les boutons
frame1 = CTkFrame(frame_principal, border_width=2, corner_radius=5, height=100,fg_color="#D88CE3")
frame1.pack(padx=10, pady=5, fill="x", expand=True)

# Création d'un widget de texte pour afficher le statut de connexion dans le frame1
output_text_frame1 = CTkTextbox(frame1, border_width=2, corner_radius=5, height=100, fg_color="#D88CE3", text_color="#140716")
output_text_frame1.pack(fill="both", expand=True)

# Création d'un cadre pour le texte de sortie
frame2 = CTkFrame(frame_principal)
frame2.pack(padx=10, pady=5, fill="x", expand=True)

# Widget de texte pour afficher la sortie de la commande
output_text = CTkTextbox(frame2, border_width=2, corner_radius=5, height=250,fg_color="#D88CE3",text_color="#140716")
output_text.pack(fill="both", expand=True)

# Affichage du statut de connexion dès l'ouverture de l'application
output_text_frame1.insert("end", "Connecting...\n")

# Connexion SSH et affichage du statut de connexion
execute_command("")

# Création d'un cadre pour les boutons
frame3 = CTkFrame(frame_principal, border_width=2, corner_radius=5, height=150,fg_color="#D88CE3")
frame3.pack(padx=10, pady=5, fill="x", expand=True)

# Création d'un bouton pour soumettre les passwords
submit_button = CTkButton(frame3, text="Enter The Password",text_color="#f5e8f7",fg_color="#7e1b8c")
submit_button.grid(row=1, column=0, padx=(20,0), pady=20)

# Création d'un bouton pour soumettre les commandes
submit_button = CTkButton(frame3, text="Submit The Command", text_color="#f5e8f7",command=lambda: execute_command(command_entry.get()),fg_color="#7e1b8c")
submit_button.grid(row=1, column=1, padx=(250,0), pady=20)

# Création d'un champ de saisie pour les commandes utilisateur
command_entry = CTkEntry(frame3,placeholder_text="Enter The Command",placeholder_text_color="#f5e8f7",fg_color="#7e1b8c")
command_entry.grid(row=1, column=2, padx=(20,0), pady=20)



# Ajout d'un gestionnaire d'événements pour la touche "Entrée" dans le champ de saisie de la commande
def on_enter_key(event):
    execute_command(command_entry.get())

# Liaison de l'événement "<Return>" (la touche "Entrée") au gestionnaire d'événements
command_entry.bind("<Return>", on_enter_key)

# Lancement de la boucle principale de l'application tkinter
app.mainloop()
