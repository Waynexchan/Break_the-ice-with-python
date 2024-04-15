'''def second():
  n= int(input())
  arr = map(int,input().split())
  arr = list(set(arr))
  arr.sort()
  print(arr[-2])

second()
'''

import textwrap

string = input()
width = int(input())

print(textwrap.fill(string,width))