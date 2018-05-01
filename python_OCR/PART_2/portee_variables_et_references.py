# LA PORTÉE DES VARIABLES

	# L'ESPACE LOCAL D'UNE FONCTION
# Cet espace contient les paramètres qui sont passés à la fonction
# et les variables définies dans son corps.
# Si la variable n'existe pas dans l'espace local d'une fonction, Python
# va regarder dans l'espace local dans lequel la fonction a été appelée.

# 1 fonction ne peux pas affecter de nouvelles valeurs aux paramètres.

# 1 fonction ne peut modifier, par affectation, la valeur d'une variable extérieure à son espace local.

# 1 fonction peux modifier l'objet derrière le paramètre en appelant une méthode de cet objet.
def ajouter(liste, valeur_a_ajouter):
    """Cette fonction insère à la fin de la liste la valeur que l'on veut ajouter"""
    liste.append(valeur_a_ajouter)

ma_liste = ['a', 'e', 'i']
ajouter(ma_liste, 'o')
ma_liste  # ['a', 'e', 'i', 'o']

	# LES RÉFÉRENCES
# 1 variable est un nom identifiant, pointant vers la référence d'un objet
# 2 variables peuvent pointer vers le même objet
ma_liste1 = [1, 2, 3]
ma_liste2 = ma_liste1
ma_liste2.append(4)
print(ma_liste2)  # [1, 2, 3, 4]
print(ma_liste1)  # [1, 2, 3, 4]
# ma_liste1 et ma_liste2 pointent vers le même objet

# Les ints, les floats et les strings de caractères n'ont aucune méthode travaillant sur l'objet lui-même.
# Ils ne modifient pas l'objet appelant mais renvoient un nouvel objet modifié.

ma_liste1 = [1, 2]
ma_liste2 = [1, 2]
ma_liste1 == ma_liste2  # On compare le contenu des listes
True
ma_liste1 is ma_liste2  # On compare leur référence
False

# LES VARIABLES GLOBALES : global
# Moyen de modifier, dans une fonction, des variables extérieures à celle-ci.

i = 4  # Une variable, nommée i, contenant un entier
def inc_i():
    """Fonction chargée d'incrémenter i de 1"""
    global i  # Python recherche i en dehors de l'espace local de la fonction
    i += 1

i  # 4
inc_i()
i  # 5
