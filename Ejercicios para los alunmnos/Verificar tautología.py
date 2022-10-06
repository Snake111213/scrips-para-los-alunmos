'''Para que una expresión lógica sea una tautología, el resultado debe ser verdadero para 
todas las combinaciones de los valores lógicos de las variables.
Solución
Variables
a,b,c: cada variable tomará los valores lógicos: True y False
El lenguaje Python no tiene un operador para el enunciado ⇒ pero se puede usar una 
equivalencia lógica: p⇒q ≡p∨q. 
Con esta equivalencia, la expresión (a∧b)⇒(a∨c) se transforma a: ((a∧b)) ∨ (a∨c)vvv'''

#Verificar tautología
for a in [True,False]:
    for b in [True,False]:
        for c in [True,False]:
            p=not((a and b)) or (a or c)
            print(a,b,c,p)