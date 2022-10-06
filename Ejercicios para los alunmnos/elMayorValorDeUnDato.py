from re import X


'''n: cantidad de datos
i: conteo de ciclos
x: cada dato ingresado desde el teclado
t: el mayor valor
La variable t que contendrá el mayor valor se la inicia con cero. En un ciclo se ingresará 
cada dato y se lo comparará con t, si es mayor, la variable t es asignada con el valor del 
dato ingresado. Al finalizar el ciclo t contendra el mayor valor'''


n=int(input('Cantidad de datos: '))
t=0
for i in range(n):
    x=float(input('Ingrese el siguiente dato: '))
    if x>t:
        t=x
print('El mayor valor es: ', t)