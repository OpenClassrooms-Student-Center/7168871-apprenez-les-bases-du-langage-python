# def main():
# l = input("Saisissez une liste de nombres séparés par des virgules : ")
l = "1,2,3,4,5"
print(l)
l = l.split(",")
print(l)

s=0
for n in l:
    s += int(n)

print("Somme des nombres:", s)
m = s/len(l)
print("Moyenne des nombres:", m)
count = sum(1 for n in l if int(n) > m)
print("Nombre de nombres supérieurs à la moyenne:", count)
count2 = sum(1 for n in l if not int(n) %2)
print("Nombre de nombres pairs:", count2)

# Ne touchez pas le code ci-dessous
# if __name__ == "__main__":
#     main()
