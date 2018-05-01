# HÉRITAGE SIMPLE
class A:
    """Classe A, pour illustrer notre exemple d'héritage"""
    pass # On laisse la définition vide, ce n'est qu'un exemple

class B(A): # syntaxe pour classe B qui hérite de A
    """Classe B, qui hérite de A.
    Elle reprend les mêmes méthodes et attributs (dans cet exemple, la classe
    A ne possède de toute façon ni méthode ni attribut)"""
    pass

    # Si aucune méthode n'a été redéfinie dans la classe, on cherche dans la classe mère.
    # On peut ainsi redéfinir une certaine méthode dans une classe et laisser d'autres directement hériter
    # de la classe mère.

    # EXEMPLE
class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):
    """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""
    
    def __init__(self, nom, matricule):
        """Un agent se définit par son nom et son matricule"""
        self.nom = nom
        self.matricule = matricule
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)

agent = AgentSpecial("Fisher", "18327-121")
agent.nom # 'Fisher'
print(agent) # Agent Fisher, matricule 18327-12
agent.prenom
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'AgentSpecial' object has no attribute 'prenom'
# => AgentSpecial a redéfinit une méthode __init__, ne contenant pas d'attribut 'prenom'...

class Personne2:
    """Classe représentant une personne"""
    def __init__(self, nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial2(Personne2):
    """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""
    
    def __init__(self, nom, matricule):
        """Un agent se définit par son nom et son matricule"""
        # On appelle explicitement le constructeur de Personne :
        Personne2.__init__(self, nom)
        self.matricule = matricule
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)

agent = AgentSpecial("Fisher", "18327-121")
agent.nom # 'Fisher'
print(agent) # Agent Fisher, matricule 18327-121
agent.prenom # 'Martin'

    # PRÉCISION
def __setattr__(self, nom_attribut, valeur_attribut):
        """Méthode appelée quand on fait objet.attribut = valeur"""
        print("Attention, on modifie l'attribut {0} de l'objet !".format(nom_attribut))
        object.__setattr__(self, nom_attribut, valeur_attribut)
        """En redéfinissant la méthode __setattr__, on ne peut, dans le corps de cette méthode,
        modifier les valeurs de nos attributs comme on le fait habituellement (self.attribut = valeur)
        car alors, la méthode s'appellerait elle-même. On fait donc appel à la méthode __setattr__
        de la classe object, cette classe dont héritent implicitement toutes nos classes.
        On est sûr que la méthode de cette classe sait écrire une valeur dans un attribut."""

    # FONCTION issubclass()
issubclass(AgentSpecial, Personne) # AgentSpecial hérite de Personne
# True
issubclass(AgentSpecial, object) # True
issubclass(Personne, object) # True
issubclass(Personne, AgentSpecial) # Personne n'hérite pas d'AgentSpecial
# False

    # FONCTION isinstance()
agent = AgentSpecial("Fisher", "18327-121")
isinstance(agent, AgentSpecial) # Agent est une instance d'AgentSpecial
# True
isinstance(agent, Personne) # Agent est une instance héritée de Personne
# True

# HÉRITAGE MULTIPLE
# class MaClasseHeritee(MaClasseMere1, MaClasseMere2):

    # RECHERCHE DE MÉTHODES
    # La recherche des méthodes se fait dans l'ordre de la définition de la classe.

# RETOUR SUR LES EXCEPTIONS
# Help on class AttributeError in module builtins:

# class AttributeError(Exception)
#  |  Attribute not found.
#  |
#  |  Method resolution order:
#  |      AttributeError
#  |      Exception
#  |      BaseException
#  |      object

# L'exception AttributeError hérite de Exception, qui hérite elle-même de BaseException.

# Ecrire except TypeException implique qu'on peut intercepter toutes les exceptions du type TypeException
# mais aussi celles des classes héritées de TypeException.

    # CRÉATION D'EXCEPTIOSN PERSONNALISÉES

        # POSITION DANS LA HIÉRARCHIE

            # BaseException : la classe mère de toutes les exceptions.
            # Utilisée pour modéliser une exception qui ne sera pas foncièrement une erreur,
            # par exemple une interruption dans le traitement de votre programme.

            # Exception : c'est de cette classe que vos exceptions hériteront la plupart du temps.
            # C'est la classe mère de toutes les exceptions « d'erreurs ».

        # Classe Exception doit contenir 2 choses : constructeur et méthode __str__
class MonException(Exception):
    """Exception levée dans un certain contexte… qui reste à définir"""
    def __init__(self, message):
        """On se contente de stocker le message d'erreur"""
        self.message = message
    def __str__(self):
        """On renvoie le message"""
        return self.message

raise MonException("OUPS... j'ai tout cassé")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# __main__.MonException: OUPS... j'ai tout cassé

        # Plusieurs paramètres dans l'instanciation :
class ErreurAnalyseFichier(Exception):
    """Cette exception est levée quand un fichier (de configuration)
    n'a pas pu être analysé.
    
    Attributs :
        fichier -- le nom du fichier posant problème
        ligne -- le numéro de la ligne posant problème
        message -- le problème proprement dit"""
    
    def __init__(self, fichier, ligne, message):
        """Constructeur de notre exception"""
        self.fichier = fichier
        self.ligne = ligne
        self.message = message
    def __str__(self):
        """Affichage de l'exception"""
        return "[{}:{}]: {}".format(self.fichier, self.ligne, \
                self.message)

raise ErreurAnalyseFichier("plop.conf", 34, "Il manque une parenthèse à la fin de l'expression")
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# __main__.ErreurAnalyseFichier: [plop.conf:34]: il manque une parenthèse à la fin de l'expression
