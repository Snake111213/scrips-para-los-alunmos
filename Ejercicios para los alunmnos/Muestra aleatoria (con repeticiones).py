'''Dado un conjunto de enteros numerados 1 a n, elegir una muestra aleatoria de 
m números, m≤n
Solución
Variables
n: Tamaño de la población (dato)
m: Tamaño de la muestra (dato)
i: Variable para el conteo de repeticiones
x: Contiene cada número aleatorio seleccionado para la muestra'''

#Muestra aleatoria (con repeticiones)
from random import*
n=int(input('Ingrese tamano de la poblacion '))
m=int(input('Ingrese tamano de la nuestra '))
for i in range(m):
    x=randint(1,n)
    print(x)