class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def setParameters(self, width, height):
        if (isinstance(width, int)) and (isinstance(height, int)):
            self.width = width
            self.height = height
        else:
            return print("Введите число!!!")
    
    def getArea(self):
        return self.width*self.height

area = Rectangle()
area.setParameters("a", 5)
print(area.getArea())

            
