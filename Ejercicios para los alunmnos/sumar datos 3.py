#suma de datos
while True:
    try:
        n=int(input('Cantidad de datos: '))
    except ValueError:
        print('Cantidad inconrrecta')
        continue
    break
s=0
for i in range(n):
    x=int(input('Ingrese dato: '))
    s=s+x
print('Suma: ',s)