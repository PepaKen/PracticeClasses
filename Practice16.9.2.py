class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.height * self.width

    def getArguments(self):
        return f"Rectangle {self.width}, {self.height}"


rectangle_1 = Rectangle(7, 6)

print(rectangle_1.getArea())
print(rectangle_1.getArguments())
