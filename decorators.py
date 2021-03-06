
def outer(func):
    def inner():
        print('Accessing :', func.__name__)
        return func()
    return inner

@outer
def greet(msg):
    return 'Hello!'


def smart_divide(func):
    def wrapper(*args):
        a, b = args
        if b == 0:
            print('oops! cannot divide')
            return
        return func(*args)
    return wrapper

@smart_divide
def divide(a, b):
    return a / b

print(divide.__name__)
print(divide(4, 16))

print(divide(8,0))

def bind(func):
    func.data = 9
    return func

@bind
def add(x, y):
    return x + y

print(add(3, 10))
print(add.data)
