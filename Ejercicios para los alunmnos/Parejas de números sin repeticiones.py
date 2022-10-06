'''Liste todas las parejas de números con valores enteros del 1 al 3 pero sin que 
hayan parejas repetidas
Solución
Variables
 a: contendrá los enteros 1, 2, 3
b: contendrá los enteros desde el valor de a hasta 3
Se usará un rango para el ciclo interno que se inicie con el valor del rango del ciclo 
externo. Esto evita que el ciclo interno use valores anteriores que ya fueron considerados'''

#Parejas de números sin repeticiones
for a in range(1,4):
    for b in range(a,4):
        print(a,b)