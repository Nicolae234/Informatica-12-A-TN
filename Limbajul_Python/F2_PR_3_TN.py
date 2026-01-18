import math
a = float(input("Introdu lungimea laturii a: "))
b = float(input("Introdu lungimea laturii b: "))
c = float(input("Introdu lungimea laturii c: "))

def este_triunghi(a, b, c):
    return a + b > c and a + c > b and b + c > a

def mediana(a, b, c):
    return 0.5 * math.sqrt(2 * b**2 + 2 * c**2 - a**2)

if este_triunghi(a, b, c):
    ma = mediana(a, b, c)
    mb = mediana(b, a, c)
    mc = mediana(c, a, b)

    print("Laturile pot forma un triunghi.")
    print("Mediana corespunzătoare laturii a:", ma)
    print("Mediana corespunzătoare laturii b:", mb)
    print("Mediana corespunzătoare laturii c:", mc)
else:
    print("Laturile NU pot forma un triunghi.")
