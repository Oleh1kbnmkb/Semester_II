class Shape:
    def __init__(self) -> None:
        self.area = 0


    def calc_area(self):
        print('It returns area')


class Rectangle(Shape):
    def __init__(self, a, b) -> None:
        super().__init__
        self.a = a
        self.b = b


    def calc_area(self):
        self.area = self.a * self.b
        return self.area
    

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__
        self.r = radius


    def calc_area(self):
        self.area = 3.14 * self.r**2
        return self.area
    

s = Shape()
s.calc_area()


r = Rectangle(2, 5)
print(r.calc_area())


c = Circle(4)
print(c.calc_area())







class Shape:
    def __init__(self) -> None:
        self.perimeter = 0

    def calc_perimeter(self):
        print('It returns perimeter')


class Rectangle(Shape):
    def __init__(self, a, b) -> None:
        super().__init__()
        self.a = a
        self.b = b

    def calc_perimeter(self):
        self.perimeter = 2 * (self.a + self.b)
        return self.perimeter


class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.r = radius

    def calc_perimeter(self):
        self.perimeter = 2 * 3.14 * self.r
        return self.perimeter


s = Shape()
s.calc_perimeter()

r = Rectangle(2, 5)
print(r.calc_perimeter())

c = Circle(4)
print(c.calc_perimeter())


        