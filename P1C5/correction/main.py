# 1. Création de la liste fruits
fruits = ["pomme", "banane", "orange"]

# 2. Ajout de "kiwi"
fruits.append("kiwi")

# 3. Suppression de "orange"
fruits.remove("orange")

# 4. Modification du deuxième élément en "ananas"
fruits[1] = "ananas"

# 5. Affichage de la longueur de la liste
print("La liste fruits contient", len(fruits), "éléments.")

# 6. Tri de la liste par ordre alphabétique et affichage
fruits.sort()
print(fruits)