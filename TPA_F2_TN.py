b = int(input("Introdu baza (între 2 și 9): "))
n1 = input("Introdu primul număr în baza " + str(b) + ": ")
n2 = input("Introdu al doilea număr în baza " + str(b) + ": ")

def verifica(numar, b):
    for cifra in numar:
        if int(cifra) >= b:
            return False
    return True

def baza_b_in_10(numar, b):
    putere = 1
    rezultat = 0
    for cifra in reversed(numar):
        rezultat = rezultat + int(cifra) * putere
        putere = putere * b
    return rezultat

def baza_10_in_b(numar, b):
    if numar == 0:
        return "0"
    rezultat = ""
    while numar > 0:
        rest = numar % b
        rezultat = str(rest) + rezultat
        numar = numar // b
    return rezultat

def aduna(a, b1, baza):
    x = baza_b_in_10(a, baza)
    y = baza_b_in_10(b1, baza)
    return baza_10_in_b(x + y, baza)

def scade(a, b1, baza):
    x = baza_b_in_10(a, baza)
    y = baza_b_in_10(b1, baza)
    diferenta = x - y
    if diferenta < 0:
        return "-" + baza_10_in_b(-diferenta, baza)
    else:
        return baza_10_in_b(diferenta, baza)

def inmulteste(a, b1, baza):
    x = baza_b_in_10(a, baza)
    y = baza_b_in_10(b1, baza)
    return baza_10_in_b(x * y, baza)

if verifica(n1, b) and verifica(n2, b):
    print("Adunare:", aduna(n1, n2, b))
    print("Scădere:", scade(n1, n2, b))
    print("Înmulțire:", inmulteste(n1, n2, b))
else:
    print("Unul dintre numere nu este valid în baza", b)
