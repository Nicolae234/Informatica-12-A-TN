V = float(input("Volum de umplut: "))
q_in = float(input("Debit intrare (L/min): "))
q_out = float(input("Debit ieșire (L/min): "))

if q_in > q_out:
    t = V / (q_in - q_out)
    print(f"Timp necesar: {t} minute")
else:
    print("Rezervorul nu se poate umple (debitul de ieșire e prea mare).")
