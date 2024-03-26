# 1. Création du dictionnaire fruits 
fruits = {"pomme": "rouge", "banane": "jaune", "orange": "orange"} 

# 2. Ajout de la clé "kiwi" 
fruits["kiwi"] = "vert"

 # 3. Accès à la valeur correspondant à la clé "banane" 
couleur_banane = fruits["banane"] 

# 4. Modification de la valeur associée à la clé "pomme" 
fruits["pomme"] = "vert" 

# 5. Suppression de la clé "orange" 
del fruits["banane"] 

# 6. Affichage des clés restantes dans le dictionnaire
print(fruits.keys())