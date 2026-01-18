v0 = float(input("Valoare inițială: "))
d = float(input("Depreciere anuală (%): "))
n = int(input("Număr de ani: "))
vn = v0 * (1 - d / 100)**n
print(f"Valoarea după {n} ani: {vn}")
