print("\n\n---------Looping While dengan if & Operator modulus (sisa bagi) %-------------")
bil1 = 1
print("\n\n---------Bilangan Ganjil-------------\n")
while (bil1 <= 10):
    if (bil1 % 2 == 1):
        print("Bilangan Ganjil ", bil1)
    bil1 += 1

print("\n\n---------Bilangan Genap-------------\n")
bil = 10
while (bil >= 1):
    if (bil % 2 == 0):
        print("Bilangan Genap ", bil)
    bil -= 1