import requests

from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
resp = requests.get(url)

# print(resp)

# print(html.content)
# print(html.text)
page = resp.content

soup = BeautifulSoup(page, "html.parser")

# print("Titre: ", soup.title)
# print("Titre: ", soup.title.string)
# print()

class_name = "gem-c-document-list__item-title"
titles = soup.find_all("div", class_=class_name)

class_name = "gem-c-document-list__item-description"
descr = soup.find_all("p", class_=class_name)

print(str(len(titles)) + " titres &", str(len(descr)) + " descriptions:")
print()

for n in range(len(titles)):
    print(titles[n].a.string)
    print(descr[n].string)
    print("-" * 68)

# for t,d in titles, descr:
#     print (t.string)
# for d in descr:
#     print(d.string)
# print(len(titles))
# for t in titles:
#     pass
# print(t.a.string)


# print(soup.find_all("a"))
# print()
# # print(soup.find(id="lien1").string)
# # print()
# print(soup.find_all("p", class_="title"))

# print("-" * 68)
