import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
from customtkinter import *
import sys

app = CTk()
app.resizable(width=False, height=False)  # Empêcher le redimensionnement de la fenêtre
set_appearance_mode("dark")  # Mode d'apparence sombre
set_default_color_theme("dark-blue")  # Thème de couleur par défaut
app.title("Mon Editeur De Code")  # Titre de la fenêtre
app.geometry("1100x600")  # Dimensions de la fenêtre

file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def open_file(event=None):  # Accepter un argument event pour pouvoir l'appeler par un raccourci clavier
    global file_path
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    if path:
        with open(path, 'r') as file:
            code = file.read()
            code_input.delete('1.0', END)
            code_input.insert('1.0', code)
            set_file_path(path)

def save(event=None):  # Accepter un argument event pour pouvoir l'appeler par un raccourci clavier
    global file_path
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
        
    if path:
        with open(path, 'w') as file:
            code = code_input.get('1.0', END)
            file.write(code)
            set_file_path(path)

def new_file(event=None):  # Accepter un argument event pour pouvoir l'appeler par un raccourci clavier
    global file_path
    file_path = ''  
    code_input.delete('1.0', END)  



def run():
    if file_path == '':
        messagebox.showerror('Erreur', "Vous n'avez pas encore sauvegardé votre fichier.")
        return
    
    command = [sys.executable, file_path]  # Utilise sys.executable pour obtenir le chemin de l'interpréteur Python
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if output:
        code_output.insert('1.0', output.decode())  # Afficher la sortie standard
    if error:
        code_output.insert('1.0', error.decode())  # Afficher les erreurs


# Code input
code_input = Text(app, font="consolas 18")
code_input.place(x=280, y=30, width=800, height=850)

# Output code
code_output = Text(app, font="consolas 15", bg="#323846", fg="lightgreen")
code_output.place(x=960, y=30, width=620, height=850)

# Boutons
new_button =  CTkButton(app, text="Nouveau fichier", command=new_file, width=90, height=30)
open_button =  CTkButton(app, text="Ouvrir", command=open_file, width=90, height=30)
save_button =  CTkButton(app, text="Enregistrer", command=save, width=90, height=30)
run_button =  CTkButton(app, text="Exécuter", command=run, width=90, height=30)

# Positionnement des boutons
new_button.place(x=40, y=225)
open_button.place(x=40, y=270)
save_button.place(x=40, y=320)
run_button.place(x=40, y=370)

# Liens des raccourcis clavier
app.bind('<Control-n>', new_file)  # Ctrl+N pour nouveau fichier
app.bind('<Control-o>', open_file)  # Ctrl+O pour ouvrir
app.bind('<Control-s>', save)       # Ctrl+S pour enregistrer

app.mainloop()
