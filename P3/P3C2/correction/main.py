from bs4 import BeautifulSoup

# Extraction des informations souhaitées avec Beautiful Soup
with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extraction du titre de la page
title = soup.title.string
print("Titre de la page:", title)

# Extraction du texte de la balise h1
h1_text = soup.find("h1").string
print("Texte de la balise h1:", h1_text)

# Dictionnaire pour stocker les produits
all_products = dict()

# Extraction des noms et des prix des produits dans la liste
products = soup.find_all("li")
for product in products:
    name = product.find("h2").string
    price_str = product.find("p", class_="price").string
    # On sépare la chaine avec " " en liste de mots
    price_list = price_str.split(" ")
    # On récupère le prix (= deuxième mot)
    all_products[name] = {"prix": price_list[1]}
    
    # Extraction de la description du produit
    # La description eest le dernier élément de la liste des paragraphes
    description = product.find_all("p")[-1].string
    all_products[name]["description"] = description

# Affichage des informations extraites
print("Produits:", all_products)

# Transformation des prix en dollars
for name in all_products.keys():
    price_str = all_products[name]["prix"]
    # Supprimer le symbole €
    price = price_str.strip("€")
    # Convertir en float
    price = float(price)
    dollar_price = price * 1.2
    all_products[name]["prix_dollar"] = f"{dollar_price}$"

# Affichage avec les prix en dollars
print("Tous les produits:", all_products)
