import random
import zlib
'''
def ran():
  s= int(input())
  e= int(input())

  print(random.randrange(s, e+1))

ran()
'''
s='hello world!hello world!hello world!hello world!'
y = bytes(s, 'utf-8')
t= zlib.compress(y)
print(t)
print(zlib.decompress(t))