'''La instrucción continue se usa en los ciclos para regresar al comienzo del ciclo ignorando 
todas las instrucciones restantes en la iteración actual.
Ejemplo. El siguiente programa suma los elementos de una lista ignorando los valores 
negativos.'''

#uso de continue

from tkinter import N


x=[23,45,-34,27,-82,56]
s=0
for n in x:
    if n<0:
        continue
    s=s+n
print(s)