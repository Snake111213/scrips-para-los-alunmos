'''Simular lanzamientos de un dado. Determinar la cantidad de lanzamientos hasta 
que salga el 5.
Solución usando la estructura while
La estructura while se puede usar para mantener la repetición mientras se cumple
una condición, y no se necesita usar la instrucción break
Variables
n: cantidad de intentos
c: conteo de repeticiones
x: número aleatorio entre 1 y 6'''

#Simular lanzamientos de un dado
from random import*
c=0
x=0
while x!=5:
    x=randint(1,6)
    print(x)
    c=c+1
print('Lanzamiento en el cual salio el 5: ', c)