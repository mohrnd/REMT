import os
import shutil

from_dir=input('Enter the path of the folder or file to protect: ')
# Obtenir le nom du dossier à partir de son chemin
folder_name = os.path.basename(from_dir)
# Demander à l'utilisateur le nouveau nom du dossier à créer
new_folder_name = input('Enter the new name of the folder or file to protect: ')
# Construire le nouveau chemin avec le nouveau nom de dossier
from_dir2 = os.path.join(os.path.dirname(from_dir), new_folder_name)

fname=input('Enter the name of the folder to create, this folder will contain what you want to protect: ')
pasw=input('Enter the password: ')


#C:/Users/dell-5320/Desktop
#C:/Users/dell-5320/Music
#C:/Users/dell-5320/Pictures/Screenshots

todir = input('Enter where you want to place the folder containing: ')
todir=os.path.join(todir,fname)
os.mkdir(todir)

# Masquer le dossier de destinantion et le rendre en read only
#le dossier sera caché (+h) et défini en lecture seule (+r).
#(+s) veut dire  "super caché"  garder masqué même lorsque vous activez l'option pour afficher les fichiers masqués dans votre système d'exploitation

try:
    os.system(f'attrib +h +s +r "{todir}"')
    print("Le dossier  a été masqué avec succès.")
except Exception as e:
    print(f"Une erreur s'est produite lors de la masquage du dossier : {e}")



for i in pasw:
    for j in range(0,11):
        path=os.path.join(todir,str(j))
        try:
            os.mkdir(path)
        except:
            print('error1')
        for k in range(1,11):
            path2=os.path.join(path,str(k))
            try:
                os.mkdir(path2)
            except:
                print('error2')
            
    todir=todir+'/'+i

try:
    # Renommer le dossier
    os.rename(from_dir, from_dir2)
    print(f"Le dossier {folder_name} a été renommé en {new_folder_name} avec succès.")
except FileNotFoundError:
    print("Le dossier spécifié n'existe pas.")
except FileExistsError:
    print(f"Un dossier avec le nom {new_folder_name} existe déjà.")
except Exception as e:
    print(f"Une erreur s'est produite : {e}")

# Masquer le dossier renommé et le rendre en read only
#le dossier sera caché (+h) et défini en lecture seule (+r).
#(+s) veut dire  "super caché"  garder masqué même lorsque vous activez l'option pour afficher les fichiers masqués dans votre système d'exploitation

try:
    os.system(f'attrib +h +s +r  "{from_dir2}"')
    print(f"Le dossier {new_folder_name} a été masqué avec succès.")
except Exception as e:
    print(f"Une erreur s'est produite lors de la masquage du dossier : {e}")
    


try:
    shutil.move(from_dir2,todir)
except:
    print()
    