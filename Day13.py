import math

class Circle():
  def __init__(self, radius):
    self.radius= radius

  def area(self):
    pi = math.pi
    area = pi*2*self.radius
    print(area)

c = Circle(1)
c.area()