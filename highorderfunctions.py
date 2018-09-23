def greet():
    return 'Hello everyone'

def add(x,y):
    return x+y

def do(func,x,y):
    return func(x,y)

def outer():
    def inner():
        s = 'hello'
        return s
    return inner


def multiple_of(x):
    def multiple(y):
        return x*y
    return multiple

def multipliers():
    return [lambda x : i * x for i in range(4)]

print([m(2) for m in multipliers()])

'''
x = multiple_of(3)
print(x(4))
print(multiple_of(4)(4))
        
print (outer())
func = outer()
print(type(func))
print(func())
print(do(add,1,2))
'''
