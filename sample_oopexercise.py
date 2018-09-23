
import unittest

class TestIsEvenMethod(unittest.TestCase):
    def isEven(x):
        if x % 2 == 0 :
            return 1
        else:
            return 0

class Point :
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, p):
        return (p.x-self.x)**2 + (p.y-self.y)**2 + (p.z -self.z)**2

    def __add__(self, p):
        return Point(self.x+p.x , self.y+p.y , self.z+p.z)

    def __str__(self):
        return 'point : (x, y, z) '

p1 = Point(4,2,9)
p2 = Point(1,1,1)
print(p1)
print(p1.distance(p2))
p3 = p1 + p2
print(p3.x, p3.y, p3.z)

print(TestIsEvenMethod(3))
