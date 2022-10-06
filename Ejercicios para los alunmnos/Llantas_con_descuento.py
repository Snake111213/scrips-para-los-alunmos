'''Calcular el valor total que una persona debe pagar por la compra de llantas en un almacén
que tiene la siguiente promoción: Si la cantidad de llantas comprada es mayor a 4, el 
precio unitario tiene un descuento de 10%. El programa debe ingresar como datos la 
catidad de llantas y el precio inicial de cada llanta. Mediante una comparación el programa 
deberá aplicar el descuento.
Solución
Variables
 n: Cantidad de llantas
 p: Precio unitario
 t: Valor a pagar'''



#compra de llantas con descuento
n=int(input('Cantidad de llantas: '))
p=float(input('Precio unitario: '))
while n and p:
    if n>4:
        p=0.9*p
    t=n*p
print('Valor a pagar: ',t)