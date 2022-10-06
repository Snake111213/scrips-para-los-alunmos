'''Use decisiones consecutivas para resolver el ejemplo del pago de la cuenta en 
un restaurante revisado en la sección anterior.
Variables
 c: Valor de la cuenta a pagar
En la solución se usarán decisiones consecutivas para seleccionar el caso respectivo
Programv'''

#pago de una cuenta
c=float(input('Ingrese el valor de la cuenta: '))
if c<50:
    print('Pago en efectivo')
elif 50<=c<=100:
    print('Pago en bitcoin')
elif 100<=c<=200:
    print('Pago con la targeta de credito')
else:
    print('Pago con la targeta de credito')