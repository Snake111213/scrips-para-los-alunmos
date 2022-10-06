
from pickletools import int4


'''Ejemplo. Dado un número entero encuentre los dígitos de su equivalente en el sistema 
binario. El algoritmo para obtener los dígitos binarios de un número entero decimal 
consiste en dividirlo sucesivamente para 2. Los resíduos de la división entera tomados 
desde el final hacia arriba son los dígitos buscados. 
Para probar: Obtener los dígitos binarios del número 23
 
Entonces, 23 es equivalente a 1 0 1 1 1 en el sistema binario
Solución
Variables
n: Número entero positivo 
b: Cadena de caracteres que contiene los dígitos de n en el sistema binario.
 La cadena crece en forma recurrente de derecha a izquierda'''


n=int(input('Ingrese el numero positivo: '))
b=''
while n>0:
    d=n%2
    n=n//2
    b=str(d)+b
print('Numero binario: ',b)