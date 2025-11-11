def zile_totale(data):
    parti = data.split('-')
    an = int(parti[0])
    luna = int(parti[1])
    zi = int(parti[2])
    return an * 365 + luna * 30 + zi 

def citire_produse(nume_fisier):
    produse = []
    with open(nume_fisier, "r") as f:
        n = int(f.readline().strip())  
        for _ in range(n):
            linie = f.readline().strip().split()
            if len(linie) == 4:
                denumire, data_fab, data_exp, pret_init = linie
                produse.append((denumire, data_fab, data_exp, float(pret_init)))
    return produse

def calculeaza_preturi(produse, data_curenta):
    rezultat = []
    zile_curente = zile_totale(data_curenta)

    for denumire, df, de, pret_init in produse:
        zf = zile_totale(df)
        ze = zile_totale(de)
        termen_total = ze - zf
        trecute = zile_curente - zf
        pret_actual = pret_init

        if zile_curente > ze:
            pret_actual = 0.0
        elif trecute >= termen_total * 0.75:
            pret_actual = pret_init * 0.5
        elif trecute >= termen_total * 0.5:
            pret_actual = pret_init * 0.8

        rezultat.append((denumire, df, de, pret_init, pret_actual, termen_total ))
    return rezultat

produse = citire_produse("Produse.txt")
data_curenta = "2025-11-11"
rezultat = calculeaza_preturi(produse, data_curenta)

expirate = [p for p in rezultat if p[4] == 0.0]
reducere_50 = [p for p in rezultat if p[4] == 0.5 * p[3]]
reducere_20 = [p for p in rezultat if p[4] == 0.8 * p[3]]
cel_putin_1_an = [p for p in rezultat if p[5] >= 365]
cel_mult_1_luna = [p for p in rezultat if p[5] <= 30]

lista_finala = [
    ("expirate", expirate),
    ("reducere_50%", reducere_50),
    ("reducere_20%", reducere_20),
    ("termen >= 1 an", cel_putin_1_an),
    ("termen <= 1 lună", cel_mult_1_luna)
]

print("Lista produselor:\n")
for r in rezultat:
    print(r)

print("\nListele de tupluri pe categorii:\n")
for denumire_categorie, lista in lista_finala:
    print(f"{denumire_categorie}:")
    for p in lista:
        print(p)
    print()

