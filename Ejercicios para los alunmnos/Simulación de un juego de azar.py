'''o. Simular n intentos de un juego con un dado, con las siguientes reglas:
Si sale
6 Gana 4 dólares
 3 Gana 1 dólar
 1 Siga jugando
2,4 o 5 Pierde 2 dólares
Solución
Variables
n: dato (cantidad de intentos)
i: conteo de lanzamientos
x: cada número aleatorio
s: cantidad acumulada de dinero'''
#Simulación de un juego de azar
from random import*
n=int(input('Cantidad de intentos: '))
s=0
for i in range(n):
    x=randint(1,6)
    if x==6:
        s=s+4
    elif x==3:
        s=s+1
    elif x==2 or x==4 or x==5:
        s=s-2
print('Ganancia total: ', s)
