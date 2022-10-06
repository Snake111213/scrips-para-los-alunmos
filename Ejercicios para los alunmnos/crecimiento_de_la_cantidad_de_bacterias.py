'''. Describa en notación Python una solución para el siguiente problema usando la 
estructura de ciclos condicionada. 
En un cultivo se tiene una cantidad inicial de bacterias. Cada día esta cantidad se duplica. 
Determine en que día la cantidad excede a un valor máximo.
Solución
Variables
 x: Cantidad inicial de bacterias
 m: Cantidad máxima de bacterias
 d: Día'''
#crecimiento de la cantidad de bacterias
x=int(input('Ingrese la cantidad inicial  '))
m=int(input('Ingrese la cantidad maxima  '))
d=0
while x<=m:
    x=2*x
    d=d+1
print('La cantidad exede al maximo en el dia: ', d)