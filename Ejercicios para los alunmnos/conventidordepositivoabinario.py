
'''o. Dado un número entero positivo, encuentre todos sus divisores enteros 
positivos.
Solución
Variables
n: número entero positivo (dato)
d: cada número entero entre 1 y n, posible divisor de n'''

n=int(input('Ingrese un entero positivo: '))
for d in range (1,n+1):
    if n%d==0:
        print('Divisor: ', d)