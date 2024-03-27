def main():
    # Récupérer la saisie de l'utilisateur
    liste = input("Saisissez une liste de nombres séparés par des virgules : ")

    # Séparer l'ensemble des nombres et les insérer dans une liste
    liste = liste.split(",")
    # Afficher la liste des nombres
    print("Liste des nombres :", liste)

    # Calculer la somme des nombres
    somme = 0
    for nombre in liste:
        somme += int(nombre)
    print("Somme des nombres :", somme)

    # Effectuer la moyenne à l'aide de la somme des nombre
    moyenne = somme / len(liste)
    print("Moyenne des nombres :", moyenne)

    # Trouver le nombre d'entier supérieur à la moyenne
    nombre_sup_moyenne = 0
    for nombre in liste:
        if int(nombre) > moyenne:
            nombre_sup_moyenne += 1
    print("Nombre de nombres supérieurs à la moyenne :", nombre_sup_moyenne)

    # Trouver le nombre d'entier pair
    nombre_pairs = 0
    i = 0
    while i < len(liste):
        if int(liste[i]) % 2 == 0:
            nombre_pairs += 1
        i += 1
    print("Nombre de nombres pairs :", nombre_pairs)

# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()