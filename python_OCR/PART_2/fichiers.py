# MANIPULATION DE FICHIERS ET RÉPERTOIRES AVEC LE MODULE OS
import os

	# MANIPULER LES CHEMINS
import os.path

		# MÉTHODES UTILES
# abspath(path)             →   Retourne un chemin absolu
# basename(p)               →   Retourne le dernier élément d'un chemin
# commonprefix(list)        →   Retourne le chemin commun le plus long d'une liste de chemins
# dirname(p)                →   Retourne le dossier parent de l'élément
# exists(path)              →   Test si un chemin existe
# getaTime(filename)        →   Retourne la date du dernier accès au fichier [os.stat()]
# getctime(filename)        →   Retourne la date du dernier changement de metadonnées du fichier
# getmTime(filename)        →   Retourne la date de la dernière modification du fichier
# getsize(filename)         →   Retourne la taille d'un fichier (en octets)
# isabs(s)                  →   Test si un chemin est absolu
# isdir(s)                  →   Test si le chemin est un dossier
# isfile(path)              →   Test si le chemin est un fichier régulier
# islink(path)              →   Test si le chemin est un lien symbolique
# ismount(path)             →   Test si le chemin est un point de montage
# join(path, s)             →   Ajoute un élément au chemin passé en paramètre
# normcase(s)               →   Normalise la casse d'un chemin
# normpath(path)            →   Normalise le chemin, élimine les doubles barres obliques, etc.
# realpath(filename)        →   Retourne le chemin canonique du nom de fichier spécifié (élimine les liens symboliques)
# samefile(f1, f2)          →   Test si deux chemins font référence au même fichier réel
# sameopenfile(f1, f2)      →   Test si deux objets de fichiers ouverts font référence au même fichier
# split(p)                  →   Fractionne un chemin d'accès. Retourne un tuple
import os
path = "/home/olivier/scripts/cgi-bin/action.py"
os.path.dirname(path)  # '/home/olivier/scripts/cgi-bin'
os.path.basename(path)  # 'action.py'
os.path.join(path, "func")  # '/home/olivier/scripts/cgi-bin/action.py/func'
os.path.split(path)  # ('/home/olivier/scripts/cgi-bin', 'action.py')
os.path.abspath(".")  # '/home/olivier'

	# LISTER LES FICHIERS D'UN DOSSIER : listdir()
os.listdir("/home/olivier")  # ['.bash_history', 'Images', 'script.py']
# retourne une liste incluant dossiers et fichiers cachés

	# LISTER LES ÉLÉMENTS RÉCURSIVEMENT : FONCTION walk
# walk(top, topdown = True, onerror = None, followlinks = False)
import os
folder_path = "/mnt/box/files"
for path, dirs, files in os.walk(folder_path):
    for filename in files:
        print(filename)

	# RECHERCHE D'ÉLÉMENTS PAR MOTIF
# possible de récupérer les fichiers et dossiers correspondant à un motif
# *          →   n'importe quel séquence de caractères
# ?          →   n'importe quel caractère
# []         →   n'importe quel caractère listé entre les crochets
import glob # Penser à importer module glob
# glob.glob(motif)       →   Liste les dossiers et les fichiers correspondants au motif
# glob.iglob(motif)      →   Idem que glob mais retourne un itérateur
glob.glob("/home/olivier/scripts/*.txt") # ['/home/olivier/scripts/data.txt']

	# MANIPULER LES ÉLÉMENTS
# os.makedirs(path)        →   Créer récursivement tous les dossiers d'un path si ceux-ci n'existent pas
# os.mkdir(path)           →   Créer le dernier dossier d'un path. Si un des dossiers n'existe pas une erreur est retournée
# os.remove(path)          →   Supprime le fichier / dossier indiqué
# os.rename(old, new)      →   Renomme le fichier / dossier indiqué

# OBTENIR CHEMIN DU RÉPERTOIRE COURANT : getcwd()
import os
os.getcwd()  # '/Users/jbb'
# CWD : Current Working Directory

# OBTENIR CHEMIN DU RÉPERTOIRE COURANT DANS UN SCRIPT PYTHON : abspath()
from os import path as os_path
PATH = os_path.abspath(os_path.split(__file__)[0])

# CHANGER LE RÉPERTOIRE DE TRAVAIL COURANT
import os
os.chdir("/Users/jbb/desktop/sandbox/python_OCR")  # CHDIR : Change Directory

# CHEMINS RELATIFS ET ABSOLUS

	# CHEMIN ABSOLU
# "/Users/jbb/desktop/sandbox/python_OCR"
# On décrit la suite des répertoires menant au fichier

	# CHEMIN RELATIF
# On tient compte du dossier dans lequel on se trouve actuellement
# Répertoire parent : ../

# LECTURE ET ÉCRITURE DE FICHIERS

	# OUVERTURE DE FICHIERS : open('path', 'open_mode')
mon_fichier = open("fichier.txt", "r")
mon_fichier  # <_io.TextIOWrapper name = 'fichier.txt' encoding = 'cp1252' >
type(mon_fichier)  # <class '_io.TextIOWrapper' >

		# 'r' Mode lecture (read)

		# 'w' Ouverture en écriture (write)
			# contenu du fichier écrasé
			# fichier créé s'il n'existe pas

		# 'a' Ouverture en mode ajout (append)
			# écriture à la fin du fichier
			# n'écrase pas l'ancien contenu
			# fichier créé s'il n'existe pas

	# FERMER LE FICHIER : close()
mon_fichier.close()
mon_fichier.closed()  # True

	# LIRE L'INTÉGRALITÉ DU FICHIER : read()
mon_fichier = open("fichier.txt", "r")
contenu = mon_fichier.read()
# read() renvoi tout le contenu d'un fichier capturé dans une chaîne de caractères
print(contenu)  # C'est le contenu du fichier. Spectaculaire non ?
mon_fichier.close()

	# ÉCRITURE DANS UN FICHIER

		# ÉCRIRE UNE CHAÎNE : write(str_to_write)
mon_fichier = open("fichier.txt", "w")  # Argh j'ai tout écrasé !
mon_fichier.write("Premier test d'écriture dans un fichier via Python")
50  # Renvoi nombre de caractères écrits
mon_fichier.close()

		# ÉCRIRE D'AUTRES TYPES DE DONNÉES
# Si nombre ou autres que chaîne de caractères à écrire,
# les convertir en chaîne avant de les écrire et les convertir en entier après les avoir lus

		# LE MOT-CLÉ with
# with open(mon_fichier, mode_ouverture) as variable:
    # Opérations sur le fichier
	# Syntaxe pour éviter d'oublier de refermer un fichier
with open('fichier.txt', 'r') as mon_fichier:
    texte = mon_fichier.read()
# with crée un 'context manager' (gestionnaire de contexte) qui vérifie que le fichier
# est ouvert et fermé, même si des erreurs se produisent pendant le bloc.
# Python ferme donc le fichier tout seul.

# ENREGISTRER DES OBJETS DANS DES FICHIERS : MODULE pickle
import pickle

	# ENREGISTRER UN OBJET DANS UN FICHIER : CLASSE Pickler & MÉTHODE dump()
score = {
    "joueur 1": 5,
    "joueur 2": 35,
    "joueur 3": 20,
    "joueur 4": 2,
}
with open('donnees.txt', 'wb') as fichier:
	# Écriture en mode binaire 'wb' (Write Binary)
  	# On crée l'objet Pickler en lui passant en paramètre le fichier pour enregistrement
	mon_pickler = pickle.Pickler(fichier)
	# Enregistrement objet score dans fichier donnees.txt avec dump()
	mon_pickler.dump(score)
	# Dans l'idéal 1 objet par fichier

	# RÉCUPÉRER NOS OBJETS ENREGISTRÉS : CLASSE Unpickler & MÉTHODE load()
with open('donnees', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    score_recupere = mon_depickler.load()
	# load() renvoi 1er objet lu
	# Si plusieurs objets, appeler plusieurs fois load()







