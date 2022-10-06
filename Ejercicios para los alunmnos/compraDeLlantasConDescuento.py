'''Leer el número de llantas de una compra y mostrar el valor que debe pagarse. El almacén 
las vende con la siguiente política: Si se compran menos de 5 llantas, el precio unitario es 
80. Si se compran 6 o 7, el precio unitario es 70, y si se compran más de 7 llantas, el 
precio unitario es 60.
Solución
Variables
 n: Cantidad de llantas compradas
 p: Precio unitario (80, 70, o 60)
 t: Valor de la compra'''

#Compra de llantas con descuento
n=int(input('Cantidad de llantas: '))
if n<5:
    p=80
elif n==5 or n==6:
    p=70
else:
    p=60
t=n*p
print('Valor a pagar: ', t)