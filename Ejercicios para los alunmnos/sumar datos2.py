'''En el siguiente intento se evita la interrupción del programa. En caso de error en la 
cantidad de datos se muestra un mensaje y no entrarán los datos para realizar la suma. Se 
usa la variable correcto para registrar si hubo error al ingresar el dato'''

try:
    n=int(input('Cantidad de datos: '))
    correcto=True
except ValueError:
    correcto=False
if not correcto:
    print('Cantidad incorrecta')
    n=0
s=0
for i in range(n):
    x=int(input('Ingrese dato: '))
    s=s+x
print('Suma: ',s)