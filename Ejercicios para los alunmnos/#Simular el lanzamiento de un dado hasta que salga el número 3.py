'''o. Simular lanzamientos de un dado. Muestre el resultado en cada intento. Finalice 
cuando salga el número 3.
Solución
Variable
 x: resultado del dado en cada lanzamiento. Inicialmente un valor nulo para entrar al 
 ciclo. Note este artificio útil para usar la estructura while'''

#Simular el lanzamiento de un dado hasta que salga el número 3
from random import*
x=0
while x!=3:
    x=randint(1,6)
    print(x)