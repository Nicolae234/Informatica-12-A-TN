a,b,c,d=int(input('a=')),int(input('b=')),int(input('c=')),int(input('d='))
def suma_nr(a1,b1,c1,d1):
  return a1+b1+c1+d1
def media_nr(i,j,k,m):
  return (i+j+k+m)/4
def min_nr(a2,b2,c2,d2):
  return min(a2,b2,c2,d2)
sir=(input("da sirul:"))
def vocale(s):
  vocala='aeiouăîâAEIOUĂÎÂ'
  nr=0
  for a in s:
    if a in vocala:
      nr+=1

  return nr
def nr_consoane(s):
  consoane='b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm','n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z','B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M','N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
  nr=0
  for b in s:
    if b in consoane:
      nr+=1

  return nr
def radacina_lin(a,b):
  if a==0 and b==0:
    return "infinit de solutii"
  if a==0 and b !=0:
    return "nicio solutie"
  return -b/a
n=int(input('n='))
def cel_mai_mic_div(n):
  d=2
  while d<=n:
    if n%d==0:
      return d
    d+=1
def cmdc(a,b):
  if a<0:
    a=-a
  if b < 0:
    b = -b
  while b !=0:
    r = a % b
    a = b
    b = r
  return a
def cmmmc(a,b):
  if a==0 or b==0:
    return 0
  
  return (a*b)// cmdc(a,b)

def ultima_cifra(n):
  if n<0:
    n=-n

  return n%10

def cate_cifre(n):
  if n<0:
    n=-n
  if n==0:
    return 1
  nr = 0
  while n > 0:
    nr+=1
    n//=10

  return nr

def cifra_superior(n):
  if n<0:
    n=-n
  while n>=10:
    n//=10

  return n

caracter=(input('caracter necesar='))
def nr_aparitii(sir, caracter):
  nr = 0
  for litera in sir:
    if litera==caracter:
      nr+=1
    
  return nr

print('m)','numarul de aparitii ale caracterului dat',nr_aparitii(sir,caracter))
print('l)','cifra superioara in notatia zecimala',cifra_superior(n))
print('k)','cate cifre sunt in notatia zecimala',cate_cifre(n))
print('j)','ultima cifra in notatie zecimala a nr intreg',ultima_cifra(n))
print('i)','cel mai mic multiplu comun',cmmmc(a,b))
print('h)','cel mai mare divizor comun',cmdc(a,b))
print('g)','cel mai mic divizor',cel_mai_mic_div(n))
print('f)','radacina ecuatiei',radacina_lin(a,b))
print('e)','nr de consoane din sir',nr_consoane(sir))
print('d)','nr de vocale din sir',vocale(sir))
print('a)','suma numerelor reale',suma_nr(a,b,c,d))
print('b)','media numerelor intregi',media_nr(a,b,c,d))
print('c)','minimul din numerele',min_nr(a,b,c,d))
