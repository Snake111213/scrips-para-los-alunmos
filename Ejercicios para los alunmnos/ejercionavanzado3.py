'''Para cada mes muestre una lista numerada de las cuatro semanas.
Solución
Variables
 m: contendrá el nombre del mes
s: contendrá los números de las semanas'''

for m in ['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','nov','dic']:
    print('mes: ',m)
    for s in range(1,5):
        print(' semana: ',s)