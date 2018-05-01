# CONVENTION DE NOMMAGE : Camel Case
# class NomDeLaClasse

# CONSTRUCTEUR __init__
class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    def __init__(self):  # Notre méthode constructeur ("self" renvoi à l'objet en train de se créer)
        """Constructeur de notre classe. Chaque attribut va être instancié
        avec une valeur par défaut... original"""

        self.nom = "Dupont"
        self.prenom = "Jean"  # Quelle originalité
        self.age = 33  # Cela n'engage à rien
        self.lieu_residence = "Paris"

jean = Personne()
jean.nom  # 'Dupont'
jean.prenom  # 'Jean'
jean.age  # 33
jean.lieu_residence  # 'Paris'
 # Jean déménage…
jean.lieu_residence = "Berlin"
jean.lieu_residence  # 'Berlin'
# Attributs de l'objet propres à l'objet créé

class PersonneBis:
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self.lieu_residence = "Paris"

bernard = PersonneBis("Micado", "Bernard")
bernard.nom  # 'Micado'
bernard.prenom  # 'Bernard'
bernard.age  # 33

# ATTRIBUTS DE CLASSE
class Compteur:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    objets_crees = 0  # Le compteur vaut 0 au départ

    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees += 1

Compteur.objets_crees  # 0
a = Compteur()  # On crée un premier objet
Compteur.objets_crees  # 1
b = Compteur()
Compteur.objets_crees  # 2

# LES MÉTHODES
class TableauNoir:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""

    def __init__(self):
        """Par défaut, notre surface est vide"""
        self.surface = ""

    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""

        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

tab = TableauNoir()
tab.surface  # ''
tab.ecrire("Coooool ! Ce sont les vacances !")
tab.surface  # "Coooool ! Ce sont les vacances !"
tab.ecrire("Joyeux Noël !")
tab.surface  # "Coooool ! Ce sont les vacances !\nJoyeux Noël !"
print(tab.surface)  # Coooool ! Ce sont les vacances !
                    # Joyeux Noël !

    # LE PARAMÈTRE self
# Quand on doit travailler dans une méthode de l'objet sur l'objet lui-même, on passe par self
class TableauNoirBis:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""

    def __init__(self):
        """Par défaut, notre surface est vide"""
        self.surface = ""

    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""

        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def lire(self):
        """Cette méthode se charge d'afficher, grâce à print,
        la surface du tableau"""

        print(self.surface)

    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.surface = ""

tab = TableauNoirBis()
tab.lire()
tab.ecrire("Salut tout le monde.")
tab.ecrire("La forme ?")
tab.lire()  # Salut tout le monde.
            # La forme ?
tab.effacer()
tab.lire()

    # MÉTHODES DE CLASSE
# Comme on trouve des attributs propres à la classe, on trouve aussi des méthodes de classe,
# qui ne travaillent pas sur l'instance self mais sur la classe elle-même (rare).
class CompteurBis:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    objets_crees = 0  # Le compteur vaut 0 au départ

    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees += 1

    def combien(cls):
        """Méthode de classe affichant combien d'objets ont été créés"""
        print("Jusqu'à présent, {} objets ont été créés.".format(
            # Une méthode de classe prend en 1er paramètre non passe self mais cls.
            cls.objets_crees))
    # Pour que Python reconnaisse une méthode de classe, il faut appeler la fonction classmethod
    # qui prend en paramètre la méthode que l'on veut convertir et renvoie la méthode convertie.
    combien = classmethod(combien)

CompteurBis.combien()  # Jusqu'à présent, 0 objets ont été créés.
a = CompteurBis()
a.combien()  # Jusqu'à présent, 1 objets ont été créés.
b = CompteurBis()
b.combien()  # Jusqu'à présent, 2 objets ont été créés.

    # MÉTHODES STATIQUES
# Elles ne prennent aucun premier paramètre, ni self ni cls.
# Elles travaillent donc indépendamment de toute donnée,
# aussi bien contenue dans l'instance de l'objet que dans la classe.
class Test:
    """Une classe de test tout simplement"""
    def afficher():
        """Fonction chargée d'afficher quelque chose"""
        print("On affiche la même chose.")
        print("peu importe les données de l'objet ou de la classe.")
    afficher = staticmethod(afficher)

# INTROSPECTION

    # LA FONCTION dir
# Prend en paramètre un objet et renvoie la liste de ses attributs et méthodes.
class TestBis:
    """Une classe de test tout simplement"""

    def __init__(self):
        """On définit dans le constructeur un unique attribut"""
        self.mon_attribut = "ok"

    def afficher_attribut(self):
        """Méthode affichant l'attribut 'mon_attribut'"""
        print("Mon attribut est {0}.".format(self.mon_attribut))

un_test = TestBis()
un_test.afficher_attribut()  # Mon attribut est ok.
dir(un_test)
# ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__g
# e__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '_
# _setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'affich
# er_attribut', 'mon_attribut']

    # L'ATTRIBUT SPÉCIAL __dict__
# Quand on développe une classe, tous les objets construits depuis cette classe posséderont un attribut spécial __dict__.
# Cet attribut est un dictionnaire qui contient en guise de clés les noms des attributs et, en tant que valeurs,
# les valeurs des attributs.
un_test = TestBis()
un_test.__dict__  # {'mon_attribut': 'ok'}
