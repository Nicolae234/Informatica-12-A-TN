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
print('fibonacci recursiv',fibonacci_recursiv(n))
print('fibonacci iterativ',fibonacci_recursiv(n))

print("Șirul Fibonacci până la n:")
a, b = 0, 1
for i in range(n+1):
    print(a, end=" ")
    a, b = b, a + b
