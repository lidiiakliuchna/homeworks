import abc

class Shape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calc_perimeter(self, input):
        return

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim
class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc_perimeter(self):
        perim = self.a * self.b
        print("Consider me implemented", perim)
        return perim
class Square( Rectangle):
    def __init__(self, a):
        self.a = a


    def calc_perimeter(self):
        perim = self.a * 4
        print("Consider me implemented", perim)
        return perim

print(Triangle(3,4,5).calc_perimeter())
print(Rectangle(3,7).calc_perimeter())
print(Square(6).calc_perimeter())