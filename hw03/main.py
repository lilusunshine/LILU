#定义形状的类 
class Shape(object):
    @property
    def area(self):
        pass
 
#椭圆         
class Ellipse(Shape):
    pi = 3.1415926
    def __init__(self, m=0, n=0):
        super().__init__()
        self.m = m
        self.n = n

    @property
    def area(self):
        return self.m * self.n * self.pi


#矩形                
class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        super().__init__()
        self.width = width
        self.height = height
         
    @property
    def area(self):
        return self.width * self.height

#正方形         
class Square(Rectangle):
    def __init__(self, p=0):
        super().__init__(p, p)
              

#圆形                 
class Circle(Ellipse):
    def __init__(self, c=0):
        super().__init__(c, c)
         
         
shapes = [Ellipse(10,20),Rectangle(20,15),Square(15), Circle(5)]     
def compute_area(a):
    areas=0
    for x in a:
        areas+=x.area
    return areas
  
total_area = compute_area(shapes)
print(total_area)
