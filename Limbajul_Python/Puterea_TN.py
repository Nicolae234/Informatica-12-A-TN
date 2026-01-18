A = int(input("Da A: "))
B = int(input("Da B: "))
def putere_iterativ(a, b):
    p = 1
    for _ in range(b):
        p *= a
    return p
def putere_recursiv(a, b):
    if b == 0:
        return 1
    return a * putere_recursiv(a, b - 1)
print(f"{A}^{B} recursiv =", putere_recursiv(A, B))
print(f"{A}^{B} iterativ =", putere_iterativ(A, B))
