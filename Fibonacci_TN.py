n=int(input('Da nr:'))
def fibonacci_recursiv(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursiv(n - 1) + fibonacci_recursiv(n - 2)
def fibonacci_iterativ(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print('factorial recursiv',fibonacci_recursiv(n))
print('factorial iterativ',fibonacci_recursiv(n))
