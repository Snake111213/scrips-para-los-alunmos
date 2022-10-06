'''Ejemplo. Dado un número entero, genere una secuencia numérica con la siguiente regla. 
Esta secuencia se denomina de Ulam. Esta secuencia siempre llega al número 1
x / 2, x par
x
3x 1, x impar
 = 
 +
Una prueba manual de esta definición
x
20 Valor inicial 
10 par
5 impar
16 par
8 par
4 par
2 par
1 valor final
Solución
Variable
x: número entero positivo'''
x=int(input('Ingrese el dato inicial: '))
while x>1:
    if x%2 == 0:
        x=x//2
    else:
        x=3*x+1
    print(x)