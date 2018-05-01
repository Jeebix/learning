# Penser à help(dict)

# INSTANCIATION
mon_dictionnaire = dict()
mon_dictionnaire = {}

type(mon_dictionnaire)  # <class 'dict'>

mon_dictionnaire = {}
mon_dictionnaire["pseudo"] = "Prolixe"
mon_dictionnaire["mot de passe"] = "*"
mon_dictionnaire  # {'mot de passe': '*', 'pseudo': 'Prolixe'}
mon_dictionnaire["pseudo"] = "6pri1"
mon_dictionnaire  # {'mot de passe': '*', 'pseudo': '6pri1'}

	# Dictionnaire dont les clés seront des tuples
	# contenant la lettre et le chiffre identifiant la case
echiquier = {}
echiquier['a', 1] = "tour blanche"  # En bas à gauche de l'échiquier
echiquier['b', 1] = "cavalier blanc"  # À droite de la tour
echiquier['c', 1] = "fou blanc"  # À droite du cavalier
echiquier['d', 1] = "reine blanche"  # À droite du fou
echiquier['a', 2] = "pion blanc"  # Devant la tour
echiquier['b', 2] = "pion blanc"  # Devant le cavalier, à droite du pion

	# dictionnaire = {"clé": valeur, ...}
placard = {"chemise": 3, "pantalon": 6, "tee-shirt": 7}

	# Set != dictionnaire
	# ne peut contenir 2 fois le même objet
mon_set = {'pseudo', 'mot de passe'}

# SUPPRIMER DES CLÉS D'UN DICTIONNAIRE

	# MOT-CLÉ del
placard = {"chemise": 3, "pantalon": 6, "tee shirt": 7}
del placard["chemise"]

	# MÉTHODE pop()
	# Supprime clé et valeur associée + renvoi cette valeur
placard = {"chemise": 3, "pantalon": 6, "tee shirt": 7}
placard.pop("chemise")  # 3

# DES FONCTIONS DANS DES DICTIONNAIRES

	# Fonctions manipulables comme des variables (peu utile)
print_2 = print  # L'objet print_2 pointera sur la fonction print
print_2("Affichons un message")  # Affichons un message

	# Dans des dictinnaires
def fete():
	print("C'est la fête.")
def oiseau():
	print("Fais comme l'oiseau")

fonctions = {}
fonctions["fete"] = fete  # on ne met pas les parenthèses
fonctions["oiseau"] = oiseau
fonctions["oiseau"]  # function oiseau at 0x00BA5198
fonctions["oiseau"]()  # on essaye de l'appeler
# Fais comme l'oiseau...

# LES MÉTHODES DE PARCOURS

	# PARCOURS DES CLÉS : MÉTHODE keys()
fruits = {"pommes": 21, "melons": 3, "poires": 31}
for cle in fruits.keys():
	print(cle)
	# melons poires pommes (les dictionnaires n'ont pas de structure ordonnée)
	# renvoi une séquence (pas une liste)

	# PARCOURS DES VALEURS : MÉTHODE values()
fruits = {"pommes": 21, "melons": 3, "poires": 31}
for valeur in fruits.values():
	print(valeur)
	# 3 31 21 (séquence)

if 21 in fruits.values():
	print("Un des fruits se trouve dans la quantité 21.")
	# Un des fruits se trouve dans la quantité 21.

	# PARCOURS DES CLÉS ET VALEURS SIMULTANÉMENT : méthode items()
# Renvoie une liste, contenant les couples clé: valeur, sous la forme d'un tuple
fruits = {"pommes": 21, "melons": 3, "poires": 31}
for cle, valeur in fruits.items():
	print("La clé {} contient la valeur {}.".format(cle, valeur))
# La clé melons contient la valeur 3.
# La clé poires contient la valeur 31.
# La clé pommes contient la valeur 21.

# LES DICTIONNAIRES ET PARAMÈTRES DE FONCTIONS

	# RÉCUPÉRER (CAPTURER) LES PARAMÈTRES NOMMÉS DANS UN DICTIONNAIRE : **paramètres
def fonction_inconnue(**parametres_nommes):
    """Fonction permettant de voir comment récupérer les paramètres nommés
    dans un dictionnaire"""
	
    print("J'ai reçu en paramètres nommés : {}.".format(parametres_nommes))

fonction_inconnue()  # Aucun paramètre
# J'ai reçu en paramètres nommés: {}
fonction_inconnue(p = 4, j = 8)
# J'ai reçu en paramètres nommés : {'p': 4, 'j': 8}
# fonction_inconnue(p) lèvera une exception

	# FONCTION QUI ACCEPTE N'IMPORTE QUEL TYPE DE PARAMÈTRES
	# def fonction_inconnue(*en_liste, **en_dictionnaire):
# Tous les paramètres non-nommés dans variable en_liste
# Tous les paramètres nommés dans en_dictionnaire

	# TRANSFORMER UN DICTIONNAIRE EN PARAMÈTRES NOMMÉS D'UNE FONCTION
parametres = {"sep": " >> ", "end": " -\n"}
print("Voici", "un", "exemple", "d'appel", **parametres)
# Voici >> un >> exemple >> d'appel -

# Equivaut à :
print("Voici", "un", "exemple", "d'appel", sep = " >> ", end = " -\n")
# Voici >> un >> exemple >> d'appel -
