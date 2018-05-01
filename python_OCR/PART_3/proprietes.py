# LES PROPRIÉTÉS

    # L'ENCAPSULATION
# L'encapsulation est un principe qui consiste à cacher ou protéger certaines données de notre objet.
# Pour accéder aux attributs, méthodes spéciales: accesseurs et mutateurs.
# Les accesseurs donnent accès à l'attribut. Les mutateurs permettent de le modifier.

# En Python, il n'y a pas d'attributs privés. Tout est public.
# Les propriétés sont un moyen transparent de manipuler des attributs d'objet.

# Une propriété ne se crée pas dans le constructeur mais dans le corps de la classe.
# Son nom est property.
# Elle attend quatre paramètres, tous optionnels:
# la méthode donnant accès à l'attribut,
# la méthode modifiant l'attribut,
# la méthode appelée quand on souhaite supprimer l'attribut,
# la méthode appelée quand on demande de l'aide sur l'attribut.

# La convention veut qu'on n'accède pas, depuis l'extérieur de la classe, à un attribut commençant par un souligné _.

class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom ;
    - son prénom ;
    - son âge ;
    - son lieu de résidence"""

    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Paris"  # Notez le souligné _ devant le nom

    def _get_lieu_residence(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut 'lieu_residence'"""

        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence

    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format(
            self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence
    # On va dire à Python que notre attribut lieu_residence pointe vers une propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)


jean = Personne("Micado", "Jean")
jean.nom  # 'Micado'
jean.prenom  # 'Jean'
jean.age  # 33
jean.lieu_residence  # On accède à l'attribut lieu_residence !
# 'Paris'
# Attention, il semble que Jean déménage à Berlin.
jean.lieu_residence = "Berlin"
jean.lieu_residence  # On accède à l'attribut lieu_residence !
# 'Berlin'

# Les propriétés permettent de contrôler l'accès à certains attributs d'une instance.

# Elles se définissent dans le corps de la classe en suivant cette syntaxe:
# nom_propriete = property(methode_accesseur, methode_mutateur, methode_suppression, methode_aide).

# On y fait appel ensuite en écrivant objet.nom_propriete comme pour n'importe quel attribut.

# Si l'on souhaite juste lire l'attribut, c'est la méthode définie comme accesseur qui est appelée.

# Si l'on souhaite modifier l'attribut, c'est la méthode mutateur, si elle est définie, qui est appelée.

# Chacun des paramètres à passer à property est optionnel.
