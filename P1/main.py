import pprint

ct1 = {
    "prenom": "Michael",
    "nom": "Jackson",
    "telephone": "123-456-7890",
    "email": "jackson.michael@email.com",
}
ct2 = {
    "prenom": "Paul",
    "nom": "Young",
    "telephone": "123-456-7890",
    "email": "paul.young@email.com",
}

cts = []
cts.append(ct1)
cts.append(ct2)

# cts.remove(ct1)

pprint.pprint(cts)
print(72 * "x")
pprint.pprint(cts, sort_dicts=False)
