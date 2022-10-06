'''Calcule y muestre el promedio de un grupo de datos ingresados desde el teclado
Solución
Variables
n: cantidad de datos
i: conteo de ciclos
x: cada dato ingresado desde el teclado
s: suma de los datos
p: promedio'''

n=int(input('Cantidad de datos: '))
s=0
for i in range(n):
    x=float(input('Ingrese el siguiente dato: '))
    s=s+x
p=s/n
print('El promedio es: ', p)