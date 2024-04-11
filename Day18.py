import random

'''
def ran():
  s= int(input())
  e= int(input())
  li =random.choice([x for x in range(s,e+1,2)])
  print(li)

ran()
'''
'''
def ran():
  s= int(input())
  e= int(input())
  li =random.choice([x for x in range(s,e+1) if x %5 ==0 and x %7==0])
  print(li)

ran()
'''

def ran():
  s= int(input())
  e= int(input())
  li =random.sample([x for x in range(s,e+1)],5)
  print(li)

ran()

