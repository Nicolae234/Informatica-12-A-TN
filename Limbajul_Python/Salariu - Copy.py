bancnote = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
salariu = int(input("Introdu salariul (lei MDL): "))
def descompune_salariul(salariu, bancnote):
    print("\nDescompunerea salariului în bancnote MDL:")
    for b in bancnote:
        nr = salariu // b
        if nr > 0:
            print(f"{b} lei: {nr} bancnote")
        salariu %= b

descompune_salariul(salariu, bancnote)
