nombre1 = input("Entrez un nombre entier: ")
nombre2 = input("Entrez un nombre entier: ")

# isnumeric() permet de vérifier si la chaîne de caractères est un nombre
if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Erreur: les deux nombres doivent être des nombres entiers")
    raise SystemExit("Fin du programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

operation = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/']: ")

if operation not in ["+", "-", "*", "/"]:
    print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme")


if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    # Vérifie si la variable `nombre2` n'est pas nulle pour la division
    if nombre2 == 0:
        print("Erreur: impossible de diviser par zéro.")
        raise SystemExit("Fin du programme")

    resultat = round(nombre1 / nombre2, 2)

# Affiche le résultat
print(f"Le résultat de l'opération est: {round(resultat, 2)}")
