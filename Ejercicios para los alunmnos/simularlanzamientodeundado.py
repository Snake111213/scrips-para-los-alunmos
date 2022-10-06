'''o. Simule n lanzamientos de un dado. Muestre cuantas veces se obtuvo el 3.
Solución
Variables
n: dato (cantidad de lanzamientos)
i: conteo de lanzamientos
x: cada número aleatorio
c: cantidad de veces que se obtuvo el 3'''

from random import*
n=int(input('Cantidad de lanzamientos: '))
c=0
for i in range(n):
    x=randint(1,6)
    if x==3:
        c=c+1
print('Conteo de resultados favoables: ',c)