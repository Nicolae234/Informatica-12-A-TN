n=int(input('Da nr:'))
def factorial_recursiv(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursiv(n - 1)
def factorial_iterativ(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
print('factorial recursiv',factorial_recursiv(n))
print('factorial iterativ',factorial_recursiv(n))
