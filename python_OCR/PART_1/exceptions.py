# TRY ... EXCEPT
try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")

# MOT-CLÉ as
try:
    # Bloc de test
except type_de_l_exception as exception_retournee:
    print("Voici l'erreur :", exception_retournee)

# MOT-CLÉ else
try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
else:
    print("Le résultat obtenu est", resultat)

# MOT-CLÉ finally
try:
    # Test d'instruction(s)
except type_de_l_exception:
    # Traitement en cas d'erreur
finally:
    # Instruction(s) exécutée(s) qu'il y ait eu des erreurs ou non

# MOT-CLÉ pass
try:
    # Test d'instruction(s)
except type_de_l_exception:  # Rien ne doit se passer en cas d'erreur
    pass

# LES ASSERTIONS
annee = input("Saisissez une année supérieure à 0 :")
try:
    annee = int(annee)  # Conversion de l'année
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")

# LEVER UNE EXCEPTION
annee = input()  # L'utilisateur saisit l'année
try:
    annee = int(annee)  # On tente de convertir l'année
    if annee <= 0:
        raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")
