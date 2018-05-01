# Penser à help(list)

# INSTANCIATION
ma_liste = list()
ma_liste = []

type(ma_liste)  # <class 'list'>

# listes de type mutable (!= de class str)
ma_liste = [1, 3.5, "test", []]
ma_liste[1] = 4
print(ma_liste)  # [1, 4, "test", []]

# INSERTION D'ÉLÉMENT DANS UNE LISTE

	# AJOUTER 1 ÉLÉMENT À LA FIN D'UNE LISTE : append()
ma_liste = [1, 2, 3]
ma_liste.append(56)
print(ma_liste)  # [1, 2, 3, 56]

	# INSÉRER UN ÉLÉMENT DANS LA LISTE : insert()
ma_liste = ['a', 'b', 'd', 'e']
ma_liste.insert(2, 'c')  # on insère 'c' à l'indice 2
print(ma_liste)  # ['a', 'b', 'c', 'd', 'e']

# CONCATÉNATION DE LISTES : extend()
ma_liste1 = [3, 4, 5]
ma_liste2 = [8, 9, 10]
ma_liste1.extend(ma_liste2)  # On insère ma_liste2 à la fin de ma_liste1
print(ma_liste1)  # [3, 4, 5, 8, 9, 10]

ma_liste1 = [3, 4, 5]
ma_liste1 + ma_liste2  # [3, 4, 5, 8, 9, 10]

ma_liste1 += ma_liste2  # Identique à extend
print(ma_liste1)  # [3, 4, 5, 8, 9, 10]

# SUPPRESSION D'ÉLÉMENTS D'UNE LISTE

	# MOT-CLÉ del
ma_liste = [1, 2, 3]
del ma_liste[1]  # supprime 2ème élément de la liste (2)

	# MÉTHODE remove()
	# En paramètre : l'élément à supprimer (1ère occurrence)
ma_liste = [1, 2, 3]
ma_liste.remove(3)  # supprime 3
print(ma_liste)  # [1, 2]

# LE PARCOURS DE LISTES

	# WHILE
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0
while i < len(ma_liste):
    print(ma_liste[i])
    i += 1  # On incrémente i
    # a b c d e f g h

    # FOR ... IN ...
for elt in ma_liste:  # elt va prendre les valeurs successives des éléments de ma_liste
    print(elt)  # a b c d e f g h

    # FONCTION enumerate
	# Pour avoir les indices et les objets d'une listes, fonction enumerate
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i, elt in enumerate(ma_liste):
    print("À l'indice {} se trouve {}.".format(i, elt))
    #  À l'indice 0 se trouve a.
    #  À l'indice 1 se trouve b.
    #  À l'indice 2 se trouve c.
    #  À l'indice 3 se trouve d.
    #  À l'indice 4 se trouve e.
    #  À l'indice 5 se trouve f.
    #  À l'indice 6 se trouve g.
    #  À l'indice 7 se trouve h.
# Enumerate prend en paramètre une liste et renvoi un objet
# qui peut être associé à une liste contenant 2 valeurs par élément :
# l'indice et l'élément de la liste parcourue.
for elt in enumerate(ma_liste):
    print(elt)
    #  (0, 'a')
    #  (1, 'b')
    #  (2, 'c')
    #  (3, 'd')
    #  (4, 'e')
    #  (5, 'f')
    #  (6, 'g')
    #  (7, 'h')
    #  Tuples générés (séquences non-modifiables une fois créés)
autre_liste = [[1, 'a'], [4, 'd'], [7, 'g'], [26, 'z']]
for nb, lettre in autre_liste:
    print("La lettre {} est la {}e de l'alphabet.".format(lettre, nb))
    #  La lettre a est la 1e de l'alphabet.
    #  La lettre d est la 4e de l'alphabet.
    #  La lettre g est la 7e de l'alphabet.
    #  La lettre z est la 26e de l'alphabet.

# TRIER UNE LISTE

    # MÉTHODE sort()
    # Renvoi la même liste en la triant

    	# SANS PARAMÈTRE
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.sort()
print("List : ", aList)  # List : [123, 'abc', 'xyz', 'xyz', 'zara']

		# AVEC PARAMÈTRE 'KEY'
def takeSecond(elem):
    return elem[1]

random = [(2, 2), (3, 4), (4, 1), (1, 3)]
random.sort(key = takeSecond)  # [(4, 1), (2, 2), (1, 3), (3, 4)]

		# AVEC PARAMÈTRE 'REVERSE'
random.sort(key = takeSecond, reverse = True)  # [(3, 4), (1, 3), (2, 2), (4, 1)]

	# FONCTION sorted()
	# Retourne une nouvelle liste triée

		# SANS PARAMÈTRE
sorted([5, 2, 3, 1, 4])  # [1, 2, 3, 4, 5]

		# AVEC PARAMÈTRE 'KEY'
sorted("This is a test string from Andrew".split(), key = str.lower)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key = lambda student: student[2])  # trié par âge
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
sorted(list, key = len)  # utilise fonction len en key pour le tri d'une liste

		# AVEC PARAMÈTRE 'REVERSE'
sorted(student_tuples, key = lambda student: student[2], reverse = True)
#  [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]


# INTRODUCTION AUX TUPLES
# Tuple est comme une liste mais avec des parenthèses comme délimiteur
tuple_vide = ()
tuple_non_vide = (1,)  # équivalent à ci-dessus
tuple_non_vide = 1
tuple_avec_plusieurs_valeurs = (1, 2, 5)
# tuple avec unique élément : virgule après sinon interprété comme variable

	# CAS D'UTILISATION DES TUPLES : AFFECTATION MULTIPLE
a, b = 3, 4
a  # 3
b  # 4
# équivaut à
(a, b) = (3, 4)

	# UNE FONCTION RENVOYANT PLUSIEURS VALEURS
def decomposer(entier, divise_par):
    """Cette fonction retourne la partie entière et le reste de
    entier / divise_par"""

    p_e = entier // divise_par  # // opérateur de division qui renvoi la partie entière
    reste = entier % divise_par
    return p_e, reste

partie_entiere, reste = decomposer(20, 3)  # on passe par des tuples
partie_entiere  # 6
reste  # 2
# on capture un tuple contenant 2 éléments : p_e et le reste
retour = decomposer(20, 3)
