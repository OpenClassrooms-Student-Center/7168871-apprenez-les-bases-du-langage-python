def main():
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire

    # 1. Créez deux variables `nombre_a_gauche` et `nombre_a_droite`, et demandez à l'utilisateur de les saisir.
    nombre_a_gauche = input("Entrez le premier nombre entier : ")
    nombre_a_droite = input("Entrez le deuxième nombre entier : ")

    # 2. Créez une variable `operation` pour stocker le symbole de l'opération.
    operation = input("Entrez l'opération (+, -, * ou /) : ")

    # 3. Initialisez la variable `resultat` à 0.
    resultat = 0

    # 4. Vérifiez si les deux nombres sont bien des entiers
    if not (nombre_a_gauche.isnumeric() and nombre_a_droite.isnumeric()):
        print("Erreur: les deux nombres doivent être des nombres entiers")
        return  # Quitte le programme si l'un des nombres n'est pas un entier
    else:
        # Convertissez les nombres en entiers
        nombre_a_gauche = int(nombre_a_gauche)
        nombre_a_droite = int(nombre_a_droite)

    # 5. Vérifiez le symbole d'opération et effectuez le calcul
    match operation:
        case "+":
            resultat = nombre_a_gauche + nombre_a_droite
        case "-":
            resultat = nombre_a_gauche - nombre_a_droite
        case "*":
            resultat = nombre_a_gauche * nombre_a_droite
        case "/":
            if nombre_a_droite == 0:
                print("Erreur: impossible de diviser par zéro.")
                return  # Quitte le programme si division par zéro
            else:
                resultat = nombre_a_gauche / nombre_a_droite
        case _:
            print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")
            return  # Quitte le programme si le symbole est incorrect

    # 6. Affichez le résultat
    print("Le résultat est :", resultat)


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()