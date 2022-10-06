'''o. Simule n lanzamientos de un dardo en un cuadrado de 1 m de lado. Determine 
cuantos intentos cayeron dentro de un círculo inscrito en el cuadrado.
Solución
Variables
n: dato (cantidad de intentos)
i: conteo de lanzamientos
x,y: coordenadas para cada lanzamiento (números aleatori'''

#Puntos aleatorios dentro de un círculo
from random import*
n=int(input('Cantidad de intentos: '))
c=0
for i in range(n):
    x=random()
    y=random()
    if x**2 + y**2 <= 1:
        c=c+1
print('Dentro del circulo: ',c)