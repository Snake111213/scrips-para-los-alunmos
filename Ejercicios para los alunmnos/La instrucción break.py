'''La instrucción break interrumpe las iteraciones de un ciclo. Para salir de un ciclo doble se 
puede usar un artificio como se muestra en el siguiente programa. Suponer que se desea 
salir de ambos ciclos la primera vez que el valor asignado a la variable n sea divisible por 7'''

from tkinter.tix import Tree


salida= False
for i in range(1,10):
    for j in range(1,10):
        n=2*i**3+3*j**2
        if n%7==0:
            print(i,j,n)
            salida = True
            break #sale el ciclo interno
    if salida:
        break     #sale del ciclo externo