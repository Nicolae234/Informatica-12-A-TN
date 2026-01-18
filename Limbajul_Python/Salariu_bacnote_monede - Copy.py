bancnote = [1000, 500, 200, 100, 50, 20, 10, 5, 1]  
monede = [50, 25, 10, 5]                             
salariu = float(input("Introdu salariul (lei MDL): "))

def descompune_salariul(suma, bancnote, monede):
    lei = int(suma)
    bani = round((suma - lei) * 100)

    print("\nDescompunerea salariului în bancnote și monede MDL:")
  
    for b in bancnote:
        nr = lei // b
        if nr > 0:
            print(f"{b} lei: {nr} bancnote")
        lei %= b

    if bani > 0:
        print("\nMonede:")
        for m in monede:
            nr = bani // m
            if nr > 0:
                print(f"{m} bani: {nr} monede")
            bani %= m

descompune_salariul(salariu, bancnote, monede)
