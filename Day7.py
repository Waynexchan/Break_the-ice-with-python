import math
'''
class Generator():
  def __init__(self, start, end):
    self.start = start
    self.end = end
  def divisible_by_7(self):
    for no in range(self.start, self.end+1):
      if no %7 ==0:
        yield no 

s,end= input("enter start and end: ").split()
a= Generator(int(s),int(end))
for no in a.divisible_by_7():
  print(no)
'''

def movement():
  x,y= 0,0
  while True:
    direct_v = input().split()
    if not direct_v:
      break
    if direct_v[0] == 'UP':
      y -= int(direct_v[1])
    elif direct_v[0] == 'DOWN':
      y += int(direct_v[1])
    elif direct_v[0] == 'LEFT':
      x -= int(direct_v[1])
    elif direct_v[0] == 'RIGHT':
      x += int(direct_v[1])
  print(round(math.sqrt((x**2+y**2))))

movement()
      
  
  

    