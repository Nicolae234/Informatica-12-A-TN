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

        rezultat.append((denumire, df, de, pret_init, pret_actual))
    return rezultat

produse = citire_produse("Produse.txt")
data_curenta = "2025-11-11"
rezultat = calculeaza_preturi(produse, data_curenta)

print("Lista produselor:\n")
for r in rezultat:
    print(r)
