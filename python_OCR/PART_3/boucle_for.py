# LES ITÉRATEURS
ma_liste = [1, 2, 3]
for element in ma_liste:
    print(ma_liste)

    # UTILISATION
# Quand Python tombe sur une ligne du type for element in ma_liste:, il va appeler l'itérateur de ma_liste.
# L'itérateur, c'est un objet qui va être chargé de parcourir l'objet conteneur, ici une liste.

# L'itérateur est créé dans la méthode spéciale __iter__ de l'objet. Ici, c'est donc la méthode __iter__
# de la classe list qui est appelée et qui renvoie un itérateur permettant de parcourir la liste.

# À chaque tour de boucle, Python appelle la méthode spéciale __next__ de l'itérateur, qui doit renvoyer
# l'élément suivant du parcours ou lever l'exception StopIteration si le parcours touche à sa fin.

# Python utilise deux fonctions pour appeler et manipuler les itérateurs : iter permet d'appeler
# la méthode spéciale __iter__ de l'objet passé en paramètre et next appelle la méthode spéciale __next__
# de l'itérateur passé en paramètre.

ma_chaine = "test"
iterateur_de_ma_chaine = iter(ma_chaine)
iterateur_de_ma_chaine # <str_iterator object at 0x00B408F0>
next(iterateur_de_ma_chaine) # 't'
next(iterateur_de_ma_chaine) # 'e'
next(iterateur_de_ma_chaine) # 's'
next(iterateur_de_ma_chaine) # 't'
next(iterateur_de_ma_chaine)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

    # CRÉATION
class RevStr(str):
    """Classe reprenant les méthodes et attributs des chaînes construites
    depuis 'str'. On se contente de définir une méthode de parcours
    différente : au lieu de parcourir la chaîne de la première à la dernière
    lettre, on la parcourt de la dernière à la première.
    
    Les autres méthodes, y compris le constructeur, n'ont pas besoin
    d'être redéfinies"""
    
    def __iter__(self):
        """Cette méthode renvoie un itérateur parcourant la chaîne
        dans le sens inverse de celui de 'str'"""
        
        return ItRevStr(self) # On renvoie l'itérateur créé pour l'occasion

class ItRevStr:
    """Un itérateur permettant de parcourir une chaîne de la dernière lettre
    à la première. On stocke dans des attributs la position courante et la
    chaîne à parcourir"""
    
    def __init__(self, chaine_a_parcourir):
        """On se positionne à la fin de la chaîne"""
        self.chaine_a_parcourir = chaine_a_parcourir
        self.position = len(chaine_a_parcourir)
    def __next__(self):
        """Cette méthode doit renvoyer l'élément suivant dans le parcours,
        ou lever l'exception 'StopIteration' si le parcours est fini"""
        
        if self.position == 0: # Fin du parcours
            raise StopIteration
        self.position -= 1 # On décrémente la position
        return self.chaine_a_parcourir[self.position]

ma_chaine = RevStr("Bonjour")
ma_chaine # 'Bonjour'
for lettre in ma_chaine:
    print(lettre)
# r
# u
# o
# j
# n
# o
# B

# LES GÉNÉRATEURS

    # LES GÉNÉRATEURS SIMPLES : yield
    # Ce mot-clé ne peut s'utiliser que dans le corps d'une fonction et il est suivi d'une valeur à renvoyer.
    # Les générateurs sont avant tout un moyen plus pratique de créer et manipuler des itérateurs.
def intervalle(borne_inf, borne_sup):
    """Générateur parcourant la série des entiers entre borne_inf et borne_sup.
    
    Note: borne_inf doit être inférieure à borne_sup"""
    
    borne_inf += 1
    while borne_inf < borne_sup:
        yield borne_inf
        borne_inf += 1

for nombre in intervalle(5, 10):
    print(nombre)
# 6
# 7
# 8
# 9

    # LES GÉNÉRATEURS COMME CO-ROUTINES
    # Les co-routines sont un moyen d'altérer le parcours… pendant le parcours.
    # Par exemple, dans notre générateur intervalle, on pourrait vouloir passer directement de 5 à 10.
    # Le système des co-routines en Python est contenu dans le mot-clé yield.

        # INTERROMPRE LA BOUCLE : close()
generateur = intervalle(5, 20)
for nombre in generateur:
    if nombre > 17:
        generateur.close() # Interruption de la boucle

        # ENVOYER DES DONNÉES AU GÉNÉRATEUR : send()
        # On étend notre générateur pour qu'il accepte de recevoir des données pendant son exécution.
def intervalle2(borne_inf, borne_sup):
    """Générateur parcourant la série des entiers entre borne_inf et borne_sup.
    Notre générateur doit pouvoir "sauter" une certaine plage de nombres
    en fonction d'une valeur qu'on lui donne pendant le parcours. La
    valeur qu'on lui passe est la nouvelle valeur de borne_inf.
    
    Note: borne_inf doit être inférieure à borne_sup"""
    borne_inf += 1
    while borne_inf < borne_sup:
        # variable = (yield valeur_a_renvoyer)
        valeur_recue = (yield borne_inf)
        if valeur_recue is not None: # Notre générateur a reçu quelque chose
            borne_inf = valeur_recue
        borne_inf += 1

generateur = intervalle(10, 25)
for nombre in generateur:
    if nombre == 15: # On saute à 20
        generateur.send(20)
    print(nombre, end=" ")