class Celsius:
    def __get__(self, obj, objtype):
        return self.value
    def __set__(self,obj, value):
        self.value = float(value)
    

# Add temperature class implementation below.        
class Temperature:
    celsius = Celsius()
    def __init__(self, value):
        self.fahrenheit = float(value)
    
class A:

    def __init__(self, value):
        self.x = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Only Int or float is allowed')
        self.__x = value

a = A(7)
a.x = 'George'
print(a.x)
