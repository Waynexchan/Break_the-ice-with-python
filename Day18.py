import random

def ran():
  s= int(input())
  e= int(input())
  li =random.choice([x for x in range(s,e+1,2)])
  print(li)

ran()