#Generator

def arithmetic_series(a,r):
    'generator'
    while a< 50:
        yield a
        a+=r

def fib_gen():
    'generate fibonnaci numbers'
    while 1 :
        yield 


for x in arithmetic_series(3,10):
    print(x)


    
