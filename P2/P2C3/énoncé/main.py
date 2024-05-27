def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12


def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4


def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

def main():
    salaire_annuel = 18000
    heures_par_semaine = 35

    salaire_hebdo = salaire_hebdomadaire(salaire_mensuel(salaire_annuel))
    
    print(salaire_horaire (salaire_hebdo, heures_par_semaine))

main()
