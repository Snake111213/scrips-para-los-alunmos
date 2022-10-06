'''Describa en Python un programa para resolver el siguiente problema: 
Durante el semestre un estudiante debe realizar tres evaluaciones. Cada evaluación tiene
una calificación y la nota total que recibe el estudiante es la suma de las dos mejores 
calificaciones
Escriba un programa que lea las tres calificaciones y determine cual es la calificación total 
que recibirá el estudiante.
Solución
Variables
 a, b, c: Variables que recibirán los datos de las tres calificaciones
 t: Variable con la suma de las dos mejores calificaciones
Solamente hay tres casos posibles y son excluyentes, por lo que se usarán dos decisiones 
anidadas para verificar dos casos y el tercero será la cláusula else.'''

#suma de calificaciones
a=int(input('Ingrese su primera calificacion: '))
b=int(input('Ingrese su segunda calificacion: '))
c=int(input('Ingrese su tercera calificacion: '))
if a>=c and b>=c:
    t=a+b
else:
    if a>=b and c>=b:
        t=a+c
    else:
        t=b+c
print(f'Su calificacion total es: ', {t/2})