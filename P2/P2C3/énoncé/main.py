# Ecrivez votre code ici
# DEFINITION DE LA SALAIRE MENSUEL

def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

# DEFINITION DE LA FONCTION SALAIRE HEBDOMADAIRE

def salaire_hebdomadaire(salaire_hebdomadaire):
    return salaire_mensuel / 4

# DIFINITION DE LA FONCTION SALAIRE HORAIRE 

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

# DEMANDER A L'UTILISATEUR DE SAISIR SON SALAIRE ANNUEL

salaire_annuel = float(input("Entrez votre salaire annuel : "))

# DEMANDE A L'UTILISATEUR DE SAISIR LE NOMBRE D'HEURES TRAVAILLEES PAR SEMAINE

heures_travaillees = float(input("Entrez le nombre d'heures travaillees par semaine : "))

# CALCUL DU SALAIRE HORAIRE

mensuel = salaire_mensuel(salaire_annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, heures_travaillees)

# AFFICHE DU RESULTAT

print("Votre salaire horaire est de", horaire, "francs CFA.")
