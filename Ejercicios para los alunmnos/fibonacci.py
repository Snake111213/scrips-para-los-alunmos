def fib():
    a, b = -1, 1
    while True:
        c = a + b
        yield c
        a, b = b, c

 
    for i in range(7):
        print(next(c))   