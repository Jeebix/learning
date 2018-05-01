# Les méthodes spéciales sont des méthodes d'instance que Python reconnaît
# et sait utiliser, dans certains contextes.
# Surcharge d'opérateurs.

# ÉDITION DE L'OBJET ET ACCÈS AUX ATTRIBUTS

	# __init__
class Exemple:
    """Un petit exemple de classe"""
    def __init__(self, nom):
        """Exemple de constructeur"""
        self.nom = nom
        self.autre_attribut = "une valeur"
    
    # __del__
    def __del__(self):
        """Méthode appelée quand l'objet est supprimé"""
        print("C'est la fin ! On me supprime !")

    # __repr__
# Elle affecte la façon dont est affiché l'objet quand on tape directement son nom.
# On la redéfinit quand on souhaite faciliter le debug sur certains objets.
# <__main__.XXX object at 0x00B46A70> avec print
class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Personne: nom({}), prénom({}), âge({})".format(
                self.nom, self.prenom, self.age)

p1 = Personne("Micado", "Jean")
p1 # Personne: nom(Micado), prénom(Jean), âge(33)

    # __str__
class PersonneBis:
    """Classe représentant une personne"""
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        return "{} {}, âgé de {} ans".format(
                self.prenom, self.nom, self.age)

p2 = PersonneBis("Micado", "Jean")
print(p2) # Jean Micado, âgé de 33 ans

    # OBTENIR UNE CHAINE
p1 = Personne("Micado", "Jean")
repr(p1) # 'Personne: nom(Micado), prénom(Jean), âge(33)'
chaine = str(p2)
chaine # 'Jean Micado, âgé de 33 ans'

# ACCÈS AUX ATTRIBUTS DE NOTRE OBJET

    # LA MÉTHODE __getattr__
# Méthode d'accès à nos attributs plus large que celle que Python.
# Appelée quand on veut accéder à un attribut non-défini dans l'objet.
class Protege:
    """Classe possédant une méthode particulière d'accès à ses attributs :
    Si l'attribut n'est pas trouvé, on affiche une alerte et renvoie None"""
    
    def __init__(self):
        """On crée quelques attributs par défaut"""
        self.a = 1
        self.b = 2
        self.c = 3
    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
        cette méthode. On affiche une alerte"""
        
        print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))

pro = Protege()
pro.a # 1
pro.c # 3
pro.e # Alerte ! Il n'y a pas d'attribut e ici !

    # LA MÉTHODE __setattr__
# Cette méthode définit l'accès à un attribut destiné à être modifié.
def __setattr__(self, nom_attr, val_attr):
        """Méthode appelée quand on fait objet.nom_attr = val_attr.
        On se charge d'enregistrer l'objet"""
        
        object.__setattr__(self, nom_attr, val_attr)
        self.enregistrer() # exemple
# On appelle la méthode __setattr__ de la classe mère "object" pour la modifier.
# Sinon bouclerait à l'infini sur elle-même (en s'appelant pour la modification).

    # LA MÉTHODE __delattr__
# Cette méthode spéciale est appelée quand on souhaite supprimer un attribut de l'objet.
def __delattr__(self, nom_attr):
        """On ne peut supprimer d'attribut, on lève l'exception
        AttributeError"""
        
        raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")

    # QULEQUES FONCTIONS
# objet = MaClasse() # On crée une instance de notre classe
# getattr(objet, "nom") # Semblable à objet.nom
# setattr(objet, "nom", val) # = objet.nom = val ou objet.__setattr__("nom", val)
# delattr(objet, "nom") # = del objet.nom ou objet.__delattr__("nom")
# hasattr(objet, "nom") # Renvoie True si l'attribut "nom" existe, False sinon

# LES MÉTHODES DE CONTENEUR

    # ACCÈS AUX ÉLÉMENTS D'UN CONTENUEUR
# Objets conteneurs: chaînes de caractères, dictionnaires, listes, ...
# __getitem__   objet[index]
# __setitem__   objet[index] = valeur
# __delitem__   del objet[index]
class ZDict:
    """Classe enveloppe d'un dictionnaire"""
    def __init__(self):
        """Notre classe n'accepte aucun paramètre"""
        self._dictionnaire = {}
    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""
        return self._dictionnaire[index]
    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""
        self._dictionnaire[index] = valeur
    def __delitem__(self, index):
        """Méthode appelée quand on écrit del objet[index]
        On redirige vers del self._dictionnaire[index]"""
        del self._dictionnaire[index]

    # LA MÉTHODE DERRIÈRE in : __contains__
ma_liste = [1, 2, 3, 4, 5]
8 in ma_liste # Revient au même que ...
ma_liste.__contains__(8)

    # LA MÉTHODE __len__
# Pour connaître la taille d'un objet conteneur
# len(objet) équivaut à objet.__len__()

# LES MÉTHODES MATHÉMATIQUES
class Duree:
    """Classe contenant des durées sous la forme d'un nombre de minutes
    et de secondes"""
    
    def __init__(self, min=0, sec=0):
        """Constructeur de la classe"""
        self.min = min # Nombre de minutes
        self.sec = sec # Nombre de secondes
    def __str__(self):
        """Affichage un peu plus joli de nos objets"""
        return "{0:02}:{1:02}".format(self.min, self.sec)

        # __add__
# d1 + 4 équivaut à d1.__add__(4)
def __add__(self, objet_a_ajouter):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        nouvelle_duree = Duree()
        # On va copier self dans l'objet créé pour avoir la même durée
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec
        # On ajoute la durée
        nouvelle_duree.sec += objet_a_ajouter
        # Si le nombre de secondes >= 60
        if nouvelle_duree.sec >= 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60
        # On renvoie la nouvelle durée
        return nouvelle_duree

d1 = Duree(12, 8)
print(d1) # 12:08
d2 = d1 + 54 # d1 + 54 secondes
print(d2) # 13:02

        # __sub__: surcharge de l'opérateur -

        # __mul__: surcharge de l'opérateur *

        # __truediv__: surcharge de l'opérateur /

        # __floordiv__: surcharge de l'opérateur // (division entière)

        # __mod__: surcharge de l'opérateur % (modulo)

        # __pow__: surcharge de l'opérateur ** (puissance)

        # Si préfixé par un r :
        # def __radd__(self, objet_a_ajouter):
        #     """Cette méthode est appelée si on écrit 4 + objet et que
        #     le premier objet (4 dans cet exemple) ne sait pas comment ajouter
        #     le second. On se contente de rediriger sur __add__ puisque,
        #     ici, cela revient au même : l'opération doit avoir le même résultat,
        #     posée dans un sens ou dans l'autre"""
        #     return self + objet_a_ajouter

        # __iadd__: surcharge de l'opérateur +=
        # def __iadd__(self, objet_a_ajouter):
        #     """L'objet à ajouter est un entier, le nombre de secondes"""
        #     # On travaille directement sur self cette fois
        #     # On ajoute la durée
        #     self.sec += objet_a_ajouter
        #     # Si le nombre de secondes >= 60
        #     if self.sec >= 60:
        #         self.min += self.sec // 60
        #         self.sec = self.sec % 60
        #     # On renvoie self
        #     return self

        # __isub__: surcharge de l'opérateur -+

# LES MÉTHODES DE COMPARAISON
# def __eq__(self, objet_a_comparer):
    # Opérateur d'égalité (equal). Renvoie True si self et objet_a_comparer sont égaux, False sinon.

# def __ne__(self, objet_a_comparer):
    # Différent de (non equal). Renvoie True si self et objet_a_comparer sont différents, False sinon.

# def __gt__(self, objet_a_comparer):
    # Teste si self est strictement supérieur (greater than) à objet_a_comparer.

# def __ge__(self, objet_a_comparer):
    # Teste si self est supérieur ou égal (greater or equal) à objet_a_comparer.

# def __lt__(self, objet_a_comparer):
    # Teste si self est strictement inférieur (lower than) à objet_a_comparer.

# def __le__(self, objet_a_comparer):
    # Teste si self est inférieur ou égal (lower or equal) à objet_a_comparer.

def __eq__(self, autre_duree):
        """Test si self et autre_duree sont égales"""
        return self.sec == autre_duree.sec and self.min == autre_duree.min
def __gt__(self, autre_duree):
        """Test si self > autre_duree"""
        # On calcule le nombre de secondes de self et autre_duree
        nb_sec1 = self.sec + self.min * 60
        nb_sec2 = autre_duree.sec + autre_duree.min * 60
        return nb_sec1 > nb_sec2

# DES MÉTHODES SPÉCIALES UTILES À PICKLE

    # __getstate__
# Méthode appelée au moment de sérialiser l'objet.

    # __setstate__
# Méthode appelée au moment de désérialiser l'objet.

class Temp:
    """Classe contenant plusieurs attributs, dont un temporaire"""
    
    def __init__(self):
        """Constructeur de notre objet"""
        self.attribut_1 = "une valeur"
        self.attribut_2 = "une autre valeur"
        self.attribut_temporaire = 5
   
    def __getstate__(self):
        """Renvoie le dictionnaire d'attributs à sérialiser"""
        dict_attr = dict(self.__dict__)
        dict_attr["attribut_temporaire"] = 0
        return dict_attr

    def __setstate__(self, dict_attr):
        """Méthode appelée lors de la désérialisation de l'objet"""
        dict_attr["attribut_temporaire"] = 0
        self.__dict__ = dict_attr

# Dans le premier cas, on modifie le dictionnaire des attributs avant la sérialisation.
# Le dictionnaire des attributs enregistré est celui que nous avons modifié
# avec la valeur de notre attribut temporaire à 0.

# Dans le second cas, on modifie le dictionnaire d'attributs après la désérialisation.
# Le dictionnaire que l'on récupère contient un attribut attribut_temporaire avec une valeur quelconque
# (on ne sait pas laquelle) mais après avoir récupéré l'objet qui est déjà instancié
# (et avant le retour de la désérialisation !), on met cette valeur à 0.



