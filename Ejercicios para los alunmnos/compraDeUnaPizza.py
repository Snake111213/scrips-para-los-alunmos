''''El precio de una pizza depende de su tamaño según la siguiente tabla:
 Tamaño Precio
1 $500
2 $800
3 $1200
Cada ingrediente adicional cuesta $1.5. 
Escriba un programa en Python que lea el tamaño de la pizza y el número de ingredientes
adicionales y muestre el precio que debe pagar
Solución
Variables
 t: Tamaño de pizza
 n: Número de ingredientes
 p: Valor a pagar'''

#Compra de una pizza
t=int(input('Tamano de la pizza: '))
n=int(input('Numero de ingredientes adicionales: '))
if t==1:
    p=500+1.5*n
elif t==2:
    p=800+1.5*n
elif t==3:
    p=12+1.5*n
else:
    p=0

print('Valor a pagar: ', p)