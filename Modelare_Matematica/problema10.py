p = float(input("Probabilitatea de succes (0...1): "))
n = int(input("Număr de încercări: "))
p_succes = 1 - (1 - p)**n
print(f"Probabilitatea de succes: {p_succes}")
