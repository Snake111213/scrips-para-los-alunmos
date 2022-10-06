'''. Diseñe un programa para el juego de adivinar un entero generado al azar. 
Incluya un mensaje de ayuda y un conteo de intentos.
Solución
Variables
x: número aleatorio entero
n: número ingresado 
i: conteo de intentos
Programa
Se usa un ciclo while con la condición True. Esto mantiene el ciclo activo hasta 
que adivine el número. La instrucción break forza la finalización del ciclo'''

from random import*
x=randint(1,100)
i=0
while True:
    i=i+1
    n=int(input('Adivina el numero: '))
    if n==x:
        print('Adinino en ',i,' intentos')
        break
    else:
        if n<x:
            print('Muy pequeno')
        else:
            print('Muy grande')