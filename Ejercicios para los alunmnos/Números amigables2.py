''' Escriba un programa que busque todas las parejas de números “amigables”
entre los numeros naturales menores a 500.
Solución
Variables
a, b: Variables que toman cada valor entero entre 1 y 500
n: Cada número natural
s: Suma de los divisores menores que a
t: Suma de los divisores menores que b
Cada suma de los divisores de a se compara con cada suma de los divisores de b'''

#Números amigables
for a in range(1,500):
    s=0
    for n in range(1,a):
        if a%n==0:
            s=s+n          # Suma los divisores de a
    for b in range(1,500):  # Para cada suma de a se calcula
        t=0                   # la suma de los divisores de b
        for n in range(1,b):
            if b%n==0:
                t=t+n           # Suma los divisores de b
        if s==b and t==a and a!=b:     # Compara las sumas
            print(a,b)