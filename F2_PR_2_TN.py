print('Dati numerele reale a1...a10')
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))
a5 = float(input("a5 = "))
a6 = float(input("a6 = "))
a7 = float(input("a7 = "))
a8 = float(input("a8 = "))
a9 = float(input("a9 = "))
a10 = float(input("a10 = "))

def Maxim(a,b):
    return max(a,b)

def Minim(a,b):
    return min(a,b)

def Suma():
   global a1 
   global a2 
   global a3 
   global a4 
   global a5 
   global a6 
   global a7 
   global a8 
   global a9 
   global a10
   return Minim(a1,a2)+Minim(a3,a4)+Minim(a5,a6)+Minim(a7,a8)+Minim(a9,a10)+Maxim(a1,a2)+Maxim(a3,a4)+Maxim(a5,a6)+Maxim(a7,a8)+Maxim(a9,a10)

def Total():
    global a1 
    global a2 
    global a3 
    global a4 
    global a5 
    global a6 
    global a7 
    global a8 
    global a9 
    global a10
    return max(Minim(a1,a2),Maxim(a3,a4))+min(Maxim(a5,a6),Minim(a7,a8))

print("SUMA=",Suma())
print("Total=",Total())
