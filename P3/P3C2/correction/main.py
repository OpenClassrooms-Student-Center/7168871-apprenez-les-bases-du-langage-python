from bs4 import BeautifulSoup

# Étape 1 : Extraction des informations souhaitées avec Beautiful Soup
with open("index.html", 'r') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extraction du titre de la page
title = soup.title.string

# Extraction du texte de la balise h1
h1_text = soup.h1.string

# Extraction des noms et des prix des produits dans la liste
products = soup.find_all('li')
products_list = []
for product in products:
    name = product.h2.string
    price = product.find('p', string=lambda s: 'Prix' in s).string
    products_list.append((name, price))

# Extraction des descriptions des produits dans la liste
descriptions_list = []
for product in products:
    description = product.find('p', string=lambda s: 'Description' in s).string
    descriptions_list.append(description)

# Étape 2 : Affichage des informations extraites
print("Titre de la page :", title)
print("Texte de la balise h1 :", h1_text)
print("Liste des produits :", products_list)
print("Liste des descriptions de produits :", descriptions_list)

# Étape 3 : Conversion des prix en dollars
for i, (name, price) in enumerate(products_list):
    euro_price = int(price.split()[2].replace("€",""))
    dollar_price = euro_price * 1.2
    products_list[i] = (name, f"{dollar_price}$")

# Étape 4 : Affichage de la nouvelle liste avec les prix en dollars
print("Liste des produits :", products_list)