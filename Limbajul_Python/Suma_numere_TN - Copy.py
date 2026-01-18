n = int(input('Da nr: '))
# Suma numerelor pare 
def suma_pare_iterativ(n):
    s = 0
    for i in range(2, n+1, 2):
        s += i
    return s
def suma_pare_recursiv(n):
    if n <= 1:
        return 0
    if n % 2 == 1:
        n -= 1
    return n + suma_pare_recursiv(n - 2)
# Suma numerelor impare
def suma_impare_iterativ(n):
    s = 0
    for i in range(1, n+1, 2):
        s += i
    return s
def suma_impare_recursiv(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        n -= 1
    return n + suma_impare_recursiv(n - 2)
# Suma numerelor din 5 in 5
def suma_5_iterativ(n):
    s = 0
    for i in range(5, n+1, 5):
        s += i
    return s
def suma_5_recursiv(n):
    if n < 5:
        return 0
    if n % 5 != 0:
        n -= n % 5
    return n + suma_5_recursiv(n - 5)

print("Suma pare iterativ:", suma_pare_iterativ(n))
print("Suma pare recursiv:", suma_pare_recursiv(n))

print("Suma impare iterativ:", suma_impare_iterativ(n))
print("Suma impare recursiv:", suma_impare_recursiv(n))

print("Suma din 5 în 5 iterativ:", suma_5_iterativ(n))
print("Suma din 5 în 5 recursiv:", suma_5_recursiv(n))
