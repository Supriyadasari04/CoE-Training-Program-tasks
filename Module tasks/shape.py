class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0  
class Square(Shape):
    def __init__(self, length):
        super().__init__()  
        self.length = length
    def area(self):
        return self.length ** 2  
shape = Shape()
print("Area of shape:", shape.area())  
square = Square(2)
print("Area of square:", square.area()) 
