# PREMIÈRE APPROCHE DU TRI : 2 MÉTHODES

    # MÉTHODE DE LISTE : sort()
    # Uniquement sur liste
    # Travaille sur la liste elle-même et change son ordre

    # FONCTION BUILTIN (PRÉSENTE DANS PYTHON) : sorted()
    # Travaille sur n'importe quel type de séquence (tuples, list, ...)
    # Ne modifie pas l'objet d'origine, mais renvoi un nouveau

prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
prenoms.sort()
prenoms # ['Albert', 'André', 'Jacques', 'Laure', 'Sophie', 'Victoire']
# Et avec la fonction 'sorted'
prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
sorted(prenoms) # ['Albert', 'André', 'Jacques', 'Laure', 'Sophie', 'Victoire']
prenoms # ['Jacques', 'Laure', 'André', 'Victoire', 'Albert', 'Sophie']

# APERÇU DES CRITÈRES DE TRI

    # PYHTHON TRI PAR TYPE
sorted([1, 8, -2, 15, 9]) # [-2, 1, 8, 9, 15]
sorted(["1", "8", "-2", "15", "9"]) # ['-2', '1', '15', '8', '9']

    # SI PLUSIEURS TYPES, ERREUR
sorted([1, "8", "-2", "15", 9])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unorderable types: str() < int()

# TRIER AVEC DES CLÉS PRÉCISES
etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

sorted(etudiants) # Tri se fait sur 1ère colonne des tuples
[
    ('Charles', 12, 15),
    ('Clément', 14, 16),
    ('Damien', 12, 15),
    ('Oriane', 14, 18),
    ('Thomas', 11, 12)
]

sorted(etudiants, key = lambda colonnes: colonnes[2])
[
    ('Thomas', 11, 12), 
    ('Charles', 12, 15), 
    ('Damien', 12, 15), 
    ('Clément', 14, 16),
    ('Oriane', 14, 18)
]

# TRIER UNE LISTE D'OBJETS
class Etudiant:

    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={})>".format(
                self.prenom, self.age, self.moyenne)

    # Trier la liste d'étudiants en fonction de leur moyenne :
sorted(etudiants, key=lambda etudiant: etudiant.moyenne)
# [
#     <Étudiant Thomas (âge=11, moyenne=12)>,
#     <Étudiant Charles (âge=12, moyenne=15)>,
#     <Étudiant Damien (âge=12, moyenne=15)>,
#     <Étudiant Clément (âge=14, moyenne=16)>,
#     <Étudiant Oriane (âge=14, moyenne=18)>
# ]

# TRIER DANS L'ORDRE INVERSE
sorted(etudiants, key=lambda etudiant: etudiant.age, reverse=True)
# [
#     <Étudiant Clément (âge=14, moyenne=16)>,
#     <Étudiant Oriane (âge=14, moyenne=18)>,
#     <Étudiant Charles (âge=12, moyenne=15)>,
#     <Étudiant Damien (âge=12, moyenne=15)>,
#     <Étudiant Thomas (âge=11, moyenne=12)>
# ]

# PLUS RAPIDE ET PLUS EFFICACE

    # LES FONCTIONS DU MODULE operator : itemgetter & attrgetter

        # TRIER UNE LISTE DE TUPLES
from operator import itemgetter
sorted(etudiants, key = itemgetter(2)) # équivaut à sorted(etudiants, key = lambda colonnes: colonnes[2])

        # TRIER UNE LISTE D'OBJETS
from operator import attrgetter
sorted(etudiants, key = attrgetter("moyenne")) # équivaut à sorted(etudiants, key=lambda etudiant: etudiant.moyenne)

    # TRIER SELON PLUSIEURS CRITÈRES
sorted(etudiants, key=attrgetter("age", "moyenne"))
# [
#     <Étudiant Thomas (âge=11, moyenne=12)>,
#     <Étudiant Charles (âge=12, moyenne=15)>,
#     <Étudiant Damien (âge=12, moyenne=15)>,
#     <Étudiant Clément (âge=14, moyenne=16)>,
#     <Étudiant Oriane (âge=14, moyenne=18)>
# ]
# Stabilité : si deux éléments de la séquence à comparer sont identiques, leur ordre est conservé.

        # CHAÎNAGE DE TRI
class LigneInventaire:

    """Classe représentant une ligne d'un inventaire de vente.

    Attributs attendus par le constructeur :
        produit -- le nom du produit
        prix -- le prix unitaire du produit
        quantite -- la quantité vendue du produit.

    """

    def __init__(self, produit, prix, quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return "<Ligne d'inventaire {} ({}X{})>".format(
                self.produit, self.prix, self.quantite)

# Création de l'inventaire
inventaire = [
    LigneInventaire("pomme rouge", 1.2, 19),
    LigneInventaire("orange", 1.4, 24),
    LigneInventaire("banane", 0.9, 21),
    LigneInventaire("poire", 1.2, 24),
]

# Trier cette liste par prix et par quantité :
from operator import attrgetter
sorted(inventaire, key=attrgetter("prix", "quantite"))
# [
#     <Ligne d'inventaire banane (0.9X21)>,
#     <Ligne d'inventaire pomme rouge (1.2X19)>,
#     <Ligne d'inventaire poire (1.2X24)>,
#     <Ligne d'inventaire orange (1.4X24)>
# ]

# Trier par prix croissant et par quantité décroissante :
inventaire.sort(key=attrgetter("quantite"), reverse=True)
sorted(inventaire, key=attrgetter("prix"))
# [
#     <Ligne d'inventaire banane (0.9X21)>,
#     <Ligne d'inventaire poire (1.2X24)>,
#     <Ligne d'inventaire pomme rouge (1.2X19)>,
#     <Ligne d'inventaire orange (1.4X24)>
# ]

