import math
u = 5
d = 3
H = 15

h0_a = 0
N_a = max(1, math.ceil((H - h0_a - u) / (u - d)) + 1)
print(f"a) Buburuza ajunge în vârful stâlpului în {N_a} zile.")

h0_b = 6
N_b = max(1, math.ceil((H - h0_b - u) / (u - d)) + 1)
print(f"b) Pornind de la 6m, ajunge în {N_b} zile.")

h0_c = 6 - d
N_c = max(1, math.ceil((H - h0_c - u) / (u - d)) + 1)
print(f"c) Începând cu noaptea de la 6m, ajunge în {N_c} zile.")
