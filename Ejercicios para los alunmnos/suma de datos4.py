'''En el intento final, se protege el ingreso de la cantidad de datos y de los datos para sumar. 
En el ciclo de la suma se usa un ciclo while debido a que si ingresa un dato equivocado no 
debe contarse como un ciclo válido'''

#suma de datos
while True:
    try:
        n=int(input('Cantidad de datos:  '))
    except ValueError:
        print('Cantidad incorrecta')
        continue
    break
s=0
i=0
while True:
    try:
        x=int(input('Ingrese el dato: '))
    except:
        print('Dato incorrecto')
        continue
    i=i+1
    s=s+x
    if i==n:break
print('Suma: ',s)