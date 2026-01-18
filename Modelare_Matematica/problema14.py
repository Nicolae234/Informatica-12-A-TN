c0 = float(input("Tarif fix: "))
c = float(input("Cost per km: "))
L = float(input("Distanță (km): "))
delta_t = float(input("Întârziere (minute/ore): "))
k = float(input("Penalizare per unitate de timp: "))

cost_total = c0 + c * L + k * max(0, delta_t)
print(f"Cost total: {cost_total}")
