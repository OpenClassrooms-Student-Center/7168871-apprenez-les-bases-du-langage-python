def main():
    nombre_a_gauche = input("Entrez un nombre entier : ")
    nombre_a_droite = input("Entrez un nombre entier : ")
    operation = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/'] : ")

    resultat = 0

    # Vérifie si les deux nombres sont valides avec la fonction
    # isinstance (soit un integer, soit un float)
    if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric():
        print("Erreur: les deux nombres doivent être des nombres entiers")
    else:
        nombre_a_gauche = int(nombre_a_gauche)
        nombre_a_droite = int(nombre_a_droite)
        
        match operation:
            case "+":
                resultat = nombre_a_gauche + nombre_a_droite
            case "-":
                resultat = nombre_a_gauche - nombre_a_droite
            case "*":
                resultat = nombre_a_gauche * nombre_a_droite
            case "/":
                # Vérifie si la variable `nombre_a_droite` n'est pas nulle pour la division
                if nombre_a_droite == 0:
                    print("Erreur: impossible de diviser par zéro.")
                else:
                    resultat = nombre_a_gauche / nombre_a_droite
            # Si on est dans le cas par défaut, c'est que le symbole est incorrect.
            case _:
                print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")

        # Affiche le résultat
        print(f"Le résultat de l'opération est: {resultat}")

if __name__ == "__main__":
    main()