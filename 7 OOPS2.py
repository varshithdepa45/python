class Circle():
    pi=3.14
    def __init__(self,radius=1):#pre def
        self.radius = radius
        self.area = radius*radius*Circle.pi
    def get_circumference(self):
        return self.radius*self.pi*2
my_circle = Circle(30)
print(f"{my_circle.radius} {my_circle.get_circumference()} {my_circle.area}")
