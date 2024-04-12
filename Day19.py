import random
import zlib
'''
def ran():
  s= int(input())
  e= int(input())

  print(random.randrange(s, e+1))

ran()
'''
'''
s='hello world!hello world!hello world!hello world!'
y = bytes(s, 'utf-8')
t= zlib.compress(y)
print(t)
print(zlib.decompress(t))
'''

import datetime

before = datetime.datetime.now()

for i in range(100):
  x=1+1

after = datetime.datetime.now()
execution_time = after - before
print(execution_time)


lst = [3,6,7,8]
random.shuffle(lst)
print(lst)

subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]

for sub in subjects:
    for verb in verbs:
        for obj in objects:
            print("{} {} {}".format(sub,verb,obj))