'''Suma de los cuadrados de los primeros números naturales
Solución
Variables
n: dato (número natural hasta el que se llegará)
s: suma de cuadrados
i: cada número natural'''

#Suma de cuadrados

n=int(input('Ingrese el valor final: '))
s=0
i=1
while i<=n:
    c=i**2
    s=s+c
    i=i+1
print('La suma es: ', s)