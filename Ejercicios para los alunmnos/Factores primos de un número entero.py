'''Dado un entero positivo encuentre sus factores primos
Los factores primos son los números primos que conforman el mayor conjunto de divisores 
enteros positivos de un número, tales que su producto es igual al número dado. 
Ejemplo: si el dato es 120, sus factores primos son: 2, 2, 2, 3, 5 pues su producto es 120
Solución 
Variables
x: Dato entero positivo
n: Cada número natural se probará como posible divisor de x
Se usará un ciclo para probar cada número natural n comenzando en 2 hasta llegar a x. 
Si n es un divisor de x se mostrará este divisor y se reducirá el valor de x dividiéndolo 
para este divisor n. Esto se realizará en un ciclo pues el número x puede ser divisible 
para n más de una vez.'''

#Factores primos de un número entero



x = int(input('Ingrese el dato: '))
n = 2
while n<=x:
    while x%n == 0:
        print('Divisor: ', n)
        x=x/n
    n=n+1
