''' Liste todas las ternas (a, b, c) de números enteros entre 1 y 20 que cumplen la 
propiedad Pitagórica: a2 + b2 = c2
Solución
Variables
a, b, c: números enteros entre 1 y 20'''


#Ternas Pitagóricas 
for a in range(1,21):
    for b in range(1,21):
        for c in range(1,21):
            if a**2+b**2==c**2:
                print(a,b,c)