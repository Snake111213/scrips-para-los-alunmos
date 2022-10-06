'''. Dado un número entero, determine cuantas cifras tiene.
Variables
n: dato (entero positivo)
c: cantidad de cifras de n
El número n es reducido dividiéndolo sucesivamente para 10 en un ciclo. La varible c se 
usa para determinar cuantas veces se realizó la reducción.'''

#conteo de las cifras de un numero
n=int(input('Ingrese un entero positivo: '))
c=0
while n>0:
    n=n//10
    c=c+1
print('Cantidad de cifras: ',c)