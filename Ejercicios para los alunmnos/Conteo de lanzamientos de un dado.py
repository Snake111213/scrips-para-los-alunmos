'''Simular lanzamientos de un dado. Determinar la cantidad de lanzamientos que 
se realizaron hasta que se obtuvo el número 3.
Solución
Variables
x: Resultado del dado en cada lanzamiento. Al inicio el valor 0 para entrar al ciclo
c: Conteo de repeticiones'''
#Conteo de lanzamientos de un dado
from random import*
c=0
x=0
while x!=3:
    x=randint(1, 6)
    c=c+1
print('cantidad de lanzamientos hasta que salio el 3: ', c)