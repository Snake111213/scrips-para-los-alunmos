'''. Describa en Python la siguiente decisión para pagar una cuenta en un 
restaurante: Si la cuenta es menor a $50 pago en efectivo. Sinó, si es de $50 hasta $100 
pagaré con el celular(dinero electrónico). Pero si es mayor a 100 hasta $200, usaré la 
tarjeta de débito. Caso contrario, pagaré con la tarjeta de crédito. 
Solución
Variables
 c: Valor de la cuenta a pagar
En la solución se usarán decisiones anidadas para seleccionar el caso que corresponda al 
valor de la cuenta. También se usará una forma abreviada que permite Python para 
expresar elrango para una variable en la condición'''


#Pago de una cuenta
c=float(input('Ingrese el valor de la cuenta: '))
if c<50:
    print('Pago en efectivo')
else:
    if 50<=c<=100:
        print('Pago con el celular (Moni electronico)')
    else:
        if 100<=c<=200:
            print('Pago con la targeta de debido')
        else:
            print('Sali sin Dinero')