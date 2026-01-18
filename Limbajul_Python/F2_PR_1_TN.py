import math
a = int(input("Introdu a: "))
b = int(input("Introdu b: "))
c = int(input("Introdu c: "))
d = int(input("Introdu d: "))

def este_triunghi(x, y, z):
    return x + y > z and x + z > y and y + z > x

def perimetru(x, y, z):
    return x + y + z

def aria(x, y, z):
    p = (x + y + z) / 2
    return math.sqrt(p * (p - x) * (p - y) * (p - z))

comb = [(a, b, c), (a, b, d), (a, c, d), (b, c, d)]

i = 1
for x, y, z in comb:
    print("Combinația", i, ":", x, y, z)
    if este_triunghi(x, y, z):
        print("Pot forma un triunghi.")
        print("Perimetru:", perimetru(x, y, z))
        print("Arie:", aria(x, y, z))
    else:
        print("Nu pot forma un triunghi.")
    i = i + 1
