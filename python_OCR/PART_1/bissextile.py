# -*- coding:utf-8 -*

import os # module os qui dispose de variables
          # et de fonctions utiles pour dialoguer
          # avec votre système d'exploitation

# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non

annee = input("Saisissez une année : ") # on attends que l'utilisateur fournisse l'année

try:
	annee = int(annee) # risque d'erreur si l'utilisateur n'a pas saisi un nombre
	assert annee > 0
	# Autre solution que assert
	# if annee <= 0
	# 	raise ValueError("L'année saisie est négative ou nulle.")

	if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
		print("L'année saisie est bissextile.")
	else:
		print("L'année saisie n'est pas bissextile.")

except ValueError:
	print("Vous n'avez pas saisi un nombre.")
except AssertionError:
	print("L'année saisie est inférieure ou égale à 0.")

    # On met le programme en pause pour éviter qu'il ne se referme
# os.system("pause")

