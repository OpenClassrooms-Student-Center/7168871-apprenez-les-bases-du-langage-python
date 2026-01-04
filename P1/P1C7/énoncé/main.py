# 1. Création du dictionnaire fruits 
fruits = {"pomme": "rouge", "banane": "jaune", "orange": "orange"} 
fruits["kiwi"] = "vert"
couleur_banane = fruits["banane"] 
fruits["pomme"] = "vert" 
del fruits["orange"] 
print(fruits.keys())
