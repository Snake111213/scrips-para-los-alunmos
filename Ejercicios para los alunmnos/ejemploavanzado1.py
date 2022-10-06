'''Escriba un programa para simular el siguiente juego: una rana es colocada 
aleatoriamente en la casilla central de una caja cuadriculada de tamaño 9x9 dm. La rana 
realiza saltos aleatoriamente de 1 dm. en cualquiera de las cuatro direcciones: arriba, 
abajo, izquierda o derecha. Determine la cantidad de saltos realizados hasta llegar a 
alguno de los bordes de la caja.
Solución
La casilla central coincidirá con las coordenadas (0, 0)
Variables
x,y: coordenadas de las casillas
d: dirección del salto (aleatoria)
i: conteo de intentos'''

from random import*
x=0
y=0
i=0
while -5<x<5:
    d=randint(1,4)
    i=i+1
    if d==1:
        x=x+1
    elif d==2:
        x=x-1
    elif d==3:
        y=y+1
    else:
        y=y-1
    print(x,y)
print('Cantidad de intentos: ',i)