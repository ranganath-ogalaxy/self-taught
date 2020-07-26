class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Square:
    def __init__(self, l):
        self.length = l

    def calculate_perimeter(self):
        return 4 * self.length


rectangle = Rectangle(10, 2)
square = Square(4)
rectangle.calculate_perimeter()
square.calculate_perimeter()
