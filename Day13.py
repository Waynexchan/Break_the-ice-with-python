import math

'''
class Circle():
  def __init__(self, radius):
    self.radius= radius

  def area(self):
    pi = math.pi
    area = pi*2*self.radius
    print(area)

c = Circle(1)
c.area()
'''

'''

class Rectangle():
  def __init__(self,length,height):
    self.length = length
    self.height = height 

  def area(self):
    area= self.length* self.height
    print(area)

r= Rectangle(2,5)
r.area()

'''
'''
class Shape():
  def area(self):
    area = 0
    print(area)

class Square(Shape):
  def __init__(self, l):
    self.l = l

  def area(self):
    area = self.l **2
    print(area)

s= Square(5)
s.area()
'''

raise RuntimeError('Sth Wrong')
  