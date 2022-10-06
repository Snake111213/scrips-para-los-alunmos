'''Escriba un programa que genere un número aleatorio de un dado. Si sale 6 
muestre el mensaje: ‘Afortunado’, caso contrario muestre el número que se obtuvo y el 
mensaje: ‘No hubo suerte hoy’
Solución
Variable
n: número aleatorio entre 1 y 6'''

#numero de un dado
from random import*
n=randint(1,6)
if n==6:
    print('Afortunado')
else:
    print('Salio: ' , n)
    print('Hoy no hubo suerte')