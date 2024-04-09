'''
def f(n):
  if n == 0:
    return 0
  return f(n-1)+100

n = int(input('please enter n: '))
print(f(n))
'''

def f(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  return f(n-1) + f(n-2)

n = int(input('please enter n: '))
print(f(n))