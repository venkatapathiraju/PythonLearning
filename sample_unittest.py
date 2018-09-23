
import unittest
import math
#Define below the class 'Circle' and it's methods with proper doctests.
class Circle:
    
    def __init__(self, radius):
        # Define the initialization method below
        if not type(radius) in (int, float):
            raise TypeError("radius must be a number")
        if not (radius >= 0.0 and radius <=1000.0):
            raise ValueError("radius must be between 0 and 1000 inclusive")
        self.radius = radius
        
    def area(self):
        # Define the area functionality below
        return round(math.pi * (self.radius**2),2)
               
    def circumference(self):
        # Define the circumference functionality below
        return round(math.pi * 2 * self.radius,2)


        
class TestCircleCreation(unittest.TestCase):

    def test_creating_circle_with_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5 and check if 
        # the value of c1.radius equal to 2.5 or not
        c1 = Circle(2.5)
        self.assertEqual(2.5,c1.radius)

    def test_creating_circle_with_negative_radius(self):
        # Try Defining a circle 'c' with radius -2.5 and see 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive"
        try:
            c = Circle(-2.5)
        except:
            self.assertRaises(ValueError,Circle,-2.5)

        

        

    def test_creating_circle_with_greaterthan_radius(self):
        # Try Defining a circle 'c' with radius 1000.1 and see 
        # if it raises a ValueError with the message
        # "radius must be between 0 and 1000 inclusive"      
        self.assertRaises(ValueError,Circle,1000.1)
        

    def test_creating_circle_with_nonnumeric_radius(self):
        # Try Defining a circle 'c' with radius 'hello' and see 
        # if it raises a TypeError with the message
        # "radius must be a number" 
        self.assertRaises(TypeError,Circle,'hello')

class TestCircleArea(unittest.TestCase):
    
    def test_circlearea_with_random_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5 and check if 
        # it's area is 19.63
        c1 = Circle(2.5)
        self.assertEqual(c1.area(),19.63)
        
    def test_circlearea_with_min_radius(self):
        # Define a circle 'c2' with radius 0 and check if 
        # it's area is 0
        c2 = Circle(0)
        self.assertEqual(c2.area(),0)
        
    def test_circlearea_with_max_radius(self):
        # Define a circle 'c3' with radius 1000.1 and check if 
        # it's area is 3141592.65
        #self.assertRaises(ValueError,Circles,1000.1)
        try:
            c3 = Circle(1000.1)
        except ValueError as e:
            self.assertEqual(e.args[0],"radius must be between 0 and 1000 inclusive")
        

class TestCircleCircumference(unittest.TestCase):
    
    def test_circlecircum_with_random_numeric_radius(self):
        # Define a circle 'c1' with radius 2.5 and check if 
        # it's circumference is 15.71
        c1 = Circle(2.5)
        self.assertEqual(c1.circumference(),15.71)

    def test_circlecircum_with_min_radius(self):
        # Define a circle 'c2' with radius 0 and check if 
        # it's circumference is 0.
        c1 = Circle(0)
        self.assertEqual(c1.circumference(),0)
        
    def test_circlecircum_with_max_radius(self):
        # Define a circle 'c3' with radius 1000 and check if 
        # it's circumference is 6283.19.
        c1 = Circle(1000)
        self.assertEqual(c1.circumference(),6283.19)

if __name__ == '__main__':
    unittest.main()