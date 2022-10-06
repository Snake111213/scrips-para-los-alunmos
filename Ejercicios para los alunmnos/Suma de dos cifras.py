'''. Dado un número entero de dos cifras, escriba un programa en Python para 
sumar las cifras.
Solución
Variables
n: dato entero de dos cifras
d: dígito de las decenas
u: dígito de las unidades
s: suma de dígitos'''

#Suma de dos cifras
n=int(input('Ingrese un entero: '))
d=n//10
u=n%10
s=d+u
print('Respuesta: ',s)