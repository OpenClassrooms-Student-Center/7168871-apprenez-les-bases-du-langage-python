fruit = 'osrange'
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print(f"Je ne connais pas ce fruit ({fruit}).")
