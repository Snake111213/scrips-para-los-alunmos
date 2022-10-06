''' Escriba un programa para representar mediante barras de asteriscos, 10 
números aleatorios con valores enteros entre 1 y 20.
Solución
Variables
i: variable para el conteo de repeticiones
n: número aleatorio
barra: barra de n asteriscos'''

from random import*
for i in range(10):
    n=randint(1,20)
    barra=''
    for j in range(1,n+1):
        barra=barra+'*'
    print('%4d' %n,barra)