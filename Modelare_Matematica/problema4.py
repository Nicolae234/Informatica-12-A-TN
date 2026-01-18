p = float(input("Preț inițial: "))
r = float(input("Reducere procentuală (%): "))
C = p * (1 - r / 100)
print(f"Cost final: {C}")
