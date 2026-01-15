n = int(input("Introduceți n: "))
if n == 1:
    a_n = 1
elif n == 2:
    a_n = 2
else:
    a_prev2 = 1
    a_prev1 = 2  
    for i in range(3, n + 1):
        a_n = a_prev1 + a_prev2
        a_prev2 = a_prev1
        a_prev1 = a_n

print("Elementul a_n este:", a_n)
