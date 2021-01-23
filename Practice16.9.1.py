class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArguments(self):
        return f"Rectangle {self.x}, {self.y}, {self.width}, {self.height}"


rectangle_1 = Rectangle(3, 5, 9, 7)

print(rectangle_1.getArguments())
