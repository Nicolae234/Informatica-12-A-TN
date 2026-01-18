a,b=int(input('a=')),int(input('b='))
n=int(input('n='))
def suma_nr(x,y):
  return(x+y)
#produs numere
def produs_nr(x,y):
  return(x*y)
#media numere
def media_nr(x,y):
  return(x+y)/2
#cel mai mare divizor comun
def cmmdc(a,b):
  if a<0:
    a=-a
  if b < 0:
    b = -b
  while b !=0:
    r = a % b
    a = b
    b = r
  return a
#multiplu comuni
def cmmmc(a,b):
  if a==0 or b==0:
    return 0
  return (a*b)// cmmdc(a,b)
#min
def min_nr(x,y):
  return min(x,y)
#max
def max_nr(x,y):
  return max(x,y)

#Divizorii comuni
def divizori(n):
  if n<0:
    n=-n
  d=1
  lista=[]
  while d<=n:
    if n%d == 0:
      lista.append(d)
    d+=1
  return lista

def divizori_comuni(a, b):
    list_a = divizori(a)
    list_b = divizori(b)
    comuni = []
    for d in list_a:
        if d in list_b:
            comuni.append(d)
 #multipli comuni
    return comuni
def multipli_comuni(a, b):
    m = cmmmc(a, b)
    lista = []
    k = 1
    while k <= 5:
        lista.append(m * k)
        k += 1
    return lista
#cifre comune
def cifre_comune(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    sa = str(a)
    sb = str(b)
    rez = ""
    for cifra in sa:
        if cifra in sb and cifra not in rez:
            rez += cifra
    return rez
#cifre diferite de al 2
def cifre_diferite(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    sa = str(a)
    sb = str(b)
    rez = ""
    for cifra in sa:
        if cifra not in sb and cifra not in rez:
            rez += cifra
    return rez
#cifre prietene
def numar_divizori(n):
    if n < 0:
        n = -n
    d = 1
    nr = 0
    while d <= n:
        if n % d == 0:
            nr += 1
        d += 1
    return nr

def prietene(a, b):
    return numar_divizori(a) == numar_divizori(b)

if prietene(a, b):
    print("PRIETENE")
print("Cifre doar în primul:", cifre_diferite(a, b))
print("Cifre comune:", cifre_comune(a, b))
print("Cinci multipli comuni:", multipli_comuni(a, b))
print(f"Divizorii comuni ai lui {a} și {b} sunt: {divizori_comuni(a, b)}")
print(f"{a}*{b}={a*b}")
print(f"{a}+{b}={a+b}")
print("Maxim:",max_nr(a,b))
print("Minim:",min_nr(a,b))
print("CMMMC:",cmmmc(a,b))
print("CMMDC:",cmmdc(a,b))
print("Suma:",suma_nr(a,b))
print("Produsul:",produs_nr(a,b))
print("Media:",media_nr(a,b))
