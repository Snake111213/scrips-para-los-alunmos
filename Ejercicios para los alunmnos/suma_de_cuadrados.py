'''o. Se necesita sumar los cuadrados de los primeros n números naturales.
Solución
Variables
n: número final
i: cada número natural
s: suma de los cuadrados'''

#Suma de cuadrados
n=int(input('Ingrese el valor final: '))
s=0
for i in range(1,n+1):
    c=i**2
    s=s+c
print('La suma es: ', s)