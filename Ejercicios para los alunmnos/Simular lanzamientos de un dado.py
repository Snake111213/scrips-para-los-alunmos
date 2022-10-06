from random import*
c=0
while True:
    x=randint(1,6)
    print(x)
    c=c+1
    if x==5: break
print('Lanzamiento en el cual salio el 2: ', c)