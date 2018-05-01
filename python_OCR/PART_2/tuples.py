# CHAÎNES AUX LISTES : split()
ma_chaine = "Bonjour à tous"
ma_chaine.split(" ")  # ['Bonjour', 'à', 'tous']

# LISTES AUX CHAÎNES : join()
ma_liste = ['Bonjour', 'à', 'tous']
" ".join(ma_liste)  # 'Bonjour à tous'

# APPLICATION PRATIQUE
def afficher_flottant(flottant):
    """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant
	la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.
    De plus, on va remplacer le point décimal par la virgule"""

    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    return ",".join([partie_entiere, partie_flottante[:3]])

afficher_flottant(3.99999999999998)
# '3,999'
afficher_flottant(1.5)
# '1,5'

# LES LISTES ET PARAMÈTRES DE FONCTIONS

	# LES FONCTIONS DONT LE NB DE PARAMÈTRES EST INCONNU : *paramètres
	# def fonction(*parametres):
def fonction_inconnue(*parametres):
    """Test d'une fonction pouvant être appelée avec un nombre variable de paramètres"""

    print("J'ai reçu : {}.".format(parametres))

fonction_inconnue()  # sans paramètres : 'J'ai reçu: ().'
fonction_inconnue(33)  # J'ai reçu: (33,).
fonction_inconnue('a', 'e', 'f')  # J'ai reçu : ('a', 'e', 'f').
var = 3.5
fonction_inconnue(var, [4], "...")  # J'ai reçu : (3.5, [4], '...').

# def fonction_inconnue(nom, prenom, *commentaires)
	# paramètres nom et prénom obligatoires
	# autre(s) argument(s) commentaires facultatif(s)


def afficher(*parametres, sep=' ', fin='\n'):
    """Fonction chargée de reproduire le comportement de print.
    
    Elle doit finir par faire appel à print pour afficher le résultat.
    Mais les paramètres devront déjà avoir été formatés. 
    On doit passer à print une unique chaîne, en lui spécifiant de ne rien mettre à la fin :

    print(chaine, end='')"""

    # Les paramètres sont sous la forme d'un tuple
    # Or on a besoin de les convertir
    # Mais on ne peut pas modifier un tuple
    # On a plusieurs possibilités, ici je choisis de convertir le tuple en liste
    parametres = list(parametres)
    # On va commencer par convertir toutes les valeurs en chaîne
    # Sinon on va avoir quelques problèmes lors du join
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    # La liste des paramètres ne contient plus que des chaînes de caractères
    # À présent on va constituer la chaîne finale
    chaine = sep.join(parametres)
    # On ajoute le paramètre fin à la fin de la chaîne
    chaine += fin
    # On affiche l'ensemble
    print(chaine, end='')

	# TRANSFORMER UNE LISTE EN PARAMÈTRES DE FONCTION
liste_des_parametres = [1, 4, 9, 16, 25, 36]
print(*liste_des_parametres)  # 1 4 9 16 25 36
# revient à print(1, 4, 9, 16, 25, 36)
# Si tuple ou liste contenant des paramètres qui doivent être passés à une fonction,
# on peut les transformer en paramètres lors de l'appel

# LES COMPRÉHENSIONS DE LISTES (list comprehensions)
# moyen de filtrer ou modifier une liste très simplement

	# PARCOURS SIMPLE
liste_origine = [0, 1, 2, 3, 4, 5]
[nb * nb for nb in liste_origine]  # [0, 1, 4, 9, 16, 25]
# nb * nb : valeur de retour

	# FILTRAGE AVEC UN BRANCHEMENT CONDITIONNEL
liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[nb for nb in liste_origine if nb % 2 == 0]  # [2, 4, 6, 8, 10]

	# COMBINAISON DES DEUX
qtt_a_retirer = 7  # On retire chaque semaine 7 fruits de chaque sorte
fruits_stockes = [15, 3, 18, 21]  # Par exemple 15 pommes, 3 melons...
[nb_fruits - qtt_a_retirer for nb_fruits in fruits_stockes if nb_fruits > qtt_a_retirer]
# [8, 11, 14]

	# EXERCICE : trier cette liste en fonction de la quantité de chaque fruit
inventaire = [
	("pommes", 22),
	("melons", 4),
	("poires", 18),
	("fraises", 76),
	("prunes", 51),
]

		# 1ère SOLUTION
new_inventory = sorted(inventaire, key = lambda qte_fruit: qte_fruit[1], reverse = True)

		# 2ème SOLUTION
# On change le sens de l'inventaire, la quantité avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit, qtt in inventaire]
# On n'a plus qu'à trier dans l'ordre décroissant l'inventaire inversé
# On reconstitue l'inventaire trié
inventaire = [(nom_fruit, qtt) for qtt, nom_fruit in sorted(inventaire_inverse, reverse = True)]

		# 3ème SOLUTION
# On change le sens de l'inventaire, la quantité avant le nom
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit, qtt in inventaire]
# On trie l'inventaire inversé dans l'ordre décroissant
inventaire_inverse.sort(reverse = True)
# Et on reconstitue l'inventaire
inventaire = [(nom_fruit, qtt) for qtt, nom_fruit in inventaire_inverse]

