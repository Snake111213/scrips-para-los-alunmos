'''Se dice que dos números son “amigables” si el primero es la suma de los 
divisores del segundo y viceversa. Escriba un programa que lea dos números y determine 
si so “amigables”.
Prueba: Los números 220 y 284 son “amigables” pues se cumple que:
Los divisores de 220 son: {1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110} y la suma es 284.
Los divisores de 284 son: {1, 2, 4, 71, 142} y la suma es 220.
Solución
Variables
a,b: Datos (números enteros positivos)
n: Cada posible divisor
s: Suma de los divisores menores que a
t: Suma de los divisores menores que b
La suma de los divisores de a se compara con la suma de los divisores de b'''

#Números amigables
a=int(input('Primer numero: '))
b=int(input('Segundo numero: '))
s=0
for n in range(1,a):
    if a%n==0:
        s=s+n
t=0
for n in range(1,b):
    if b%n==0:
        t=t+n
if s==b and t==a:
    print('Son numeros amigables')
else:
    print('No son numeros amigables')