
a = input("entre le nombre 1: ")# premier nombre 
b = input("Entre le nombre 2: ")# deuxieme nombre
if not a.isnumeric() or not b.isnumeric() :
    print("Les desux nombres sont entiers")
    raise SystemExit("Fin du programme")
a = int(a)
b = int(b)

op = input("Entre l'opération:  [ +, - , *,  / ]: ")
if op not in ["+", "-", "/", "*" ]:
    print("Erreur signe invalide")
    raise SystemExit("Fin du programme")
if op == "+":
    res = a+b

elif op == "*":
    res = a*b

elif op == "-":
    res = a -b

elif op == "/":
    if b ==0:
        print("Erreur impossible de divisé par zéro")
        raise SystemExit("Fin Du programme")

    res = round(a/b, 2)

print(f"Le resultat de {a} {op} {b} est : {round(res,2)} ")

