'''Describa en notación Python una solución al siguiente problema: Dado un 
entero positivo n, se desea verificar que la suma de los primeros n números impares es 
igual a n2
Ej. n = 5: 1 + 3 + 5 + 7 + 9 = 52
Solución
Variables
 n: Cantidad de números impares
 k: Cada número impar
 s: Suma de impares
 i: Conteo de ciclos '''

n=int(input('Ingrese la cantidad de impares: '))
s=0
for i in range(1,n+1):
    k=2*i-1
    s=s+k
if s==n**2:
    print('Verdadero')
else:
    print('Falso')