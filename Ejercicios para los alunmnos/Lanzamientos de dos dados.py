'''. Simule n lanzamientos de dos dados. Muestre cuantas veces los dos dados 
tuvieron el mismo resultado.
Solución
Variables
n: dato (cantidad de lanzamientos)
i: conteo de lanzamientos
a,b: contendrán números aleatorios enteros entre 1 y 6
c: cantidad de veces en las que a fue igual a b'''
#Lanzamientos de dos dados
from random import*
n=int(input('cantidad de lanzamientos: '))
c=0
for i in range(n):
    a=randint(1,6)
    b=randint(1,6)
    if a==b:
        c=c+1
print('cantidad de repetidos: ',c)