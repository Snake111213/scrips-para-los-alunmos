

def calculo_de_tiempo():
    print('Veamos cuantos dias, minutos y segundos has vivido')

    name = input('Nombre: ')

    print('Ahora escribe tu edad: ')

    try:
        age = int(input('Edad: '))

        dias = age * 365

        minutos = age * 525948

        segundos = age * 31556926

    except ValueError:
        print('no insertaste un numero')
        return  calculo_de_tiempo()

    print(f'{name} has estado vivo por {dias} dias, {minutos} minutos, {segundos}')

print('                 bienevenido al calculo del tiempo de tu vida')

calculo_de_tiempo()

x =  input('presione 1 y enter para volver a ejecutarlo de nuevo o 0 para salir:\n ')

if x == "1":
    calculo_de_tiempo()
else:
    print('adios bay')
