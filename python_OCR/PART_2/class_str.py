# """ ... """ docstring
# #!/usr/bin/python3 chemin interpréteur python sous Linux (début de fichier)
# -*- coding: utf-8 -* encodage à préciser

# INSTANCIATION
chaine = str() # Crée une chaîne vide
# Equivaut à chaîne = ""
chaine = ""

while chaine.lower() != "q":
	print("Tapez 'Q' pour quitter...")
	chaine = input()

print("Merci !")

# QUELQUES MÉTHODES (ne modifient pas l'objet d'origine, mais renvoient un nouvel objet)
chaine.upper() # Mettre en majuscules

chaine.lower() # Mettre en minuscules

chaine.capitalize() # Mettre 1ère lettre en majuscule

chaine.strip() # Enlève les espaces au début et à la fin de la chaîne

chaine.center(20) # Centre une chaîne
				  # avec en paramètre la taille de la chaîne que l'on veut obtenir
				  # Ex.: chaine = test
				  # 	 chaine.upper().center(10)
				  #		 '   TEST   '

# 1ère SYNTAXE MÉTHODE FORMAT
prenom = "Paul"
nom = "Dupont"
age = 21
chaine = "Je m'apelle {0} {1} et j'ai {2} ans."

chaine.format(prenom, nom, age) # Formate une chaîne avec variables passées en paramètres
# "Je m'appelle Paul Dupont et j'ai 21 ans."

# Equivaut à :
nouvelle_chaine = "Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom, age)
# Dans la plupart des cas, on ne précise pas les numéros
# tant qu'on respecte l'ordre des variables dans la méthode format()
nouvelle_chaine = "Je m'appelle {} {} et j'ai {} ans.".format(prenom, nom, age)

# 2ème SYNTAXE MÉTHODE FORMAT
adresse = """
{no_rue}, {nom_rue}
  {code_postal} {nom_ville} ({pays})
""".format(no_rue = 5, nom_rue = "rue des Postes", code_postal = 75003, nom_ville = "Paris", pays = "France")

print(adresse)  # 5, rue des Postes
  				#   75003 Paris (France)

help(str) # dans interpréteur pour toutes les autres méthodes de la classe 'str'

# CONCATÉNATION : symbole +
prenom = "Paul"
message = "Bonjour"
chaine = prenom + " " + message # "Paul Bonjour"
age = 21
message = "J'ai " + str(age) + " ans" # "J'ai 21 ans"

# PARCOURS DE CHAÎNE
chaine = "Salut les ZEROS !"
	
	# PAR INDICE
chaine[0] # 1ère lettre
chaine[-1] # dernière lettre
len(chaine) # 17
	
	# AVEC BOUCLE while
chaine = "Salut"
i = 0
while i < len(chaine):
	print(chaine[i]) # on affiche le caractère à chaque tour de boucle
	i += 1
	# si indice n'existe pas, IndexError

# SÉLECTION DE CHAÎNE
presentation = "Salut"
presentation[0:2] # sélection des 2 premières lettres
presentation[2:len(presentation)] # sélection de la chaîne sauf les 2 premières lettres
presentation[:2] # du début jusqu'à la 3ème lettre non-comprise
presentation[2:] # de la 3ème lettre (incluse) à la fin

mot = "lac"
mot = "b" + mot[1:]
print(mot) # "bac"

# COMPTAGE DE CHAÎNE : count()
	# str.count(sub, start=0, end=len(string))
str = "this is string example....wow!!!"
sub = "i"
str.count(sub, 4, 40) # 2
sub = "wow"
str.count(sub) # 1

# RECHERCHER DANS UNE CHAÎNE : find()
	# str.find(str, begin=0, end=len(string))
str1 = "this is string example....wow!!!"
str2 = "exam"
str1.find(str2) # 15
str1.find(str2, 10) # 15
str1.find(str2, 40) # -1 (pas trouvé)

# REMPLACER DANS UNE CHAÎNE : replace()
	# str.replace(old, new[, max])
str = "this is string example....wow!!! this is really string"
str.replace("is", "was")
# thwas was string example....wow!!! thwas was really string
str.replace("is", "was", 3) # 3ème occurrence non-incluse
# thwas was string example....wow!!! thwas is really string
