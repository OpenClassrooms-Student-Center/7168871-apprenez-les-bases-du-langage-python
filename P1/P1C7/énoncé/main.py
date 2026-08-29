fruits = {
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange"# Écrivez votre code ici !
  fruits["kiwi"] = "vert"
couleur_banane = fruits["banane"]
fruits["pomme"] = "vert"
del fruits["banane"]
print(fruits.keys())
