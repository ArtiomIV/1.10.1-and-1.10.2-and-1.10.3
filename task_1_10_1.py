class Rectangle:
    def __init__(self, x = 0, y = 0, width = 0, height = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def setParameters(self, x, y, width, height):
        if (x > 0 and isinstance(x, int)) and (y > 0 and isinstance(y, int)) and (width > 0 and isinstance(width, int)) and (height > 0 and isinstance(height, int)):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            #return "Rectagnle " + str((self.x, self.y, self.width, self.height))
            return f"Rectangle ({self.x}, {self.y}, {self.width}, {self.height})"
        else:
            print("Один из параметров некорректен")
            return False

rec1 = Rectangle()
print(rec1.setParameters(5, 10, 50, 100))

rec2 = Rectangle()
print(rec2.setParameters(10, 20, 100, 200))