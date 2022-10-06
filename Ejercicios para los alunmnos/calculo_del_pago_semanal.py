'''Describa en lenguaje Python un programa para resolver el siguiente problema: 
Para el pago semanal a un obrero se consideran los siguientes datos: horas trabajadas, 
tarifa por hora y descuentos. Si la cantidad de horas trabajadas en la semana es mayor a 
40, se le debe pagar las horas en exceso con una bonificación de 50% adicional al pago 
normal. 
Solución
Variables
 c: Cantidad de horas trabajadas en la semana
 t: Tarifa por hora
 d: Descuentos que se aplican al pago semanal
 p: Pago que recibe el obrero'''
#calculo del pago semanal
c=float(input('Horas trabajadas: '))
t=float(input('Tarifa por hora: '))
d=float(input('Descuentos: '))

if c<=40:
    p=c*t - d
else:
    p=c*t + 1.5*t*(c - 40) - d

print('Valor a pagar', p)