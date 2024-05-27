from bs4 import BeautifulSoup

with open("index.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

title = soup.find("title").string
h1_text = soup.find("h1").string

products = soup.find_all("li")
products_list = []
description_list = []
for product in products:
    name = product.h2.string
    price = product.find("p", string=lambda s: "Prix" in s).string
    description = product.find("p", string=lambda s: "Description" in s).string
    products_list.append((name, price))
    description_list.append(description)

print(f"Titre la page: {title}")
print(f"Texte de la balise H1: {h1_text}")
print('Liste des produits:', products_list)
print('Liste des descriptions:',description_list)


for i, (name, price) in enumerate(products_list):
    euro_price_str = ''.join(filter(str.isdigit, price.split()[2]))
    dollar_price=int(euro_price_str)*1.2
    products_list[i] = (name, f"${dollar_price}")

    # print (f'{name}: ${int(euro_price_str)*1.2}')
print("Liste des produits :", products_list)
