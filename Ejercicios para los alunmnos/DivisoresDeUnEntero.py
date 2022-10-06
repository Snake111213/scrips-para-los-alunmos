'''o. Dado un número entero, cuente sus divisores enteros exactos.
Solución
Variables
n: número entero positivo (dato)
x: cada número entero entre 1 y n, posible divisor de n
c: cantidad de divisores'''

n=int(input('Ingrese un entero positivo: '))
c=0
for d in range (1,n+1):
    if n%d==0:
        c=c+1
print('Cantidad de divisores: ',c)