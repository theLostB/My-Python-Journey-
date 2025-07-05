class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def area(self):
        return self.x * self.y
        #If we want to modify this area method  in child class we can modify it in child class
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)
        
    def area(self):
        return 3.14 * super().area()

sq = shape(3, 5)
print(sq.area())
c = circle(5)
print(c.area())
