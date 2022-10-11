#import math library
import math

#print the value of pi
print(math.pi)

class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 3.14 * (self.radius ** 2)
    def perimeter(self):
        return 2*3.14*self.radius
obj = Circle(int(input("Enter Radius:")))
#obj = Circle()
print("Area of circle:",obj.area())
print("Perimeter of circle:",obj.perimeter())