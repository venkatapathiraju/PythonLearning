def TokenIssuer():
    tokenid = 0
    while True:
        name = yield
        tokenid+=1
        print('Token number of ',name,':',tokenid)


t = TokenIssuer()

next(t)
t.send('George')

t.send('Rosy')

t.send('Smith')

def coroutine_decorator(func):

    def wrapper(*args, **kwdargs):

        c = func(*args, **kwdargs)

        next(c)

        return c

    return wrapper


def linear_equation(a, b):
    while True:
        x=yield
        print('Expression, {}*x^2 + {}, with x being {} equals {}'.format(a,b,x,a*(x**2)+b))
