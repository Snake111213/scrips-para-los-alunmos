'''El siguiente ejemplo trivial se usará para describir el procedimiento de validación. 
Suponer que se debe sumar una cantidad de datos enteros desde el teclado. 
Si algún dato no es entero, se producirá una excepción (error) y el programa se detendría:'''

#sumar datos
from re import X


n=int(input('Cantidad de datos: '))
s=0
for i in range(n):
    x=int(input('Ingrese dato: '))
    s=s+x 
print('Suma: ', s)