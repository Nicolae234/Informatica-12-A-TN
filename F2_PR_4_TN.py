import math
a = float(input("Introdu lungimea laturii a: "))
b = float(input("Introdu lungimea laturii b: "))
c = float(input("Introdu lungimea laturii c: "))

def este_triunghi(a, b, c):
    return a + b > c and a + c > b and b + c > a

def aria(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def inaltime(latura, A):
    return (2 * A) / latura

if este_triunghi(a, b, c):
    A = aria(a, b, c)
    ha = inaltime(a, A)
    hb = inaltime(b, A)
    hc = inaltime(c, A)

    print("Laturile pot forma un triunghi.")
    print("Aria triunghiului:", A)
    print("Înălțimea pe latura a:", ha)
    print("Înălțimea pe latura b:", hb)
    print("Înălțimea pe latura c:", hc)
else:
    print("Laturile NU pot forma un triunghi.")
