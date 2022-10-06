''' Escriba en el lenguaje Python un programa para traducir el algoritmo que calcula 
el área de un triángulo ingresando el valor de sus tres lados
Algoritmo: Área de un triángulo dados sus lados
Variables
a, b, c: Lados del triángulo (Datos desconocidos)
s: Área del triángulo (Es el resultado esperado)
t: Semiperímetro (Valor usado para la fórmula del área
s t(t a)(t b)(t c) = −−− , (Fórmula del área del triángulo)
siendo t = (a + b + c)/2'''
#Programa calcular el área de un triángulo
from math import*
a=float(input('Primer lado: '))
b=float(input('Segundo lado: '))
c=float(input('Tercer laso: '))
t=(a+b+c)/2
s=sqrt(t*(t-a)*(t-b)*(t-c))
print('Respuesta: ',s)