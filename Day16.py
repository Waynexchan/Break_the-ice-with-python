'''
def f(n):
  if n == 0:
    return 0
  return f(n-1)+100

n = int(input('please enter n: '))
print(f(n))
'''
'''
def f(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  return f(n-1) + f(n-2)

n = int(input('please enter n: '))
print(f(n))
'''
'''
def f(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  return f(n-1) + f(n-2)

def print_flist(n):
  fibo_list =[str(f(i)) for i in range(0, n+1)]
  return print (','. join(fibo_list))

n = int(input('please enter n: '))
print_flist(n)
'''
'''
def even(n):
  i = 0
  while i < n+1:
    if i %2 == 0:
      yield i
    i+=1

n = int(input())

li=[]
for num in even(n):
  li.append(str(num))

print(','.join(li))
'''

def check(n):
  i = 0
  while i < n+1:
    if i %5 ==0 and i %7 ==0:
      yield i
    i+=1

n = int(input())
li = []
for num in check(n):
  li.append(str(num))

print(','.join(li))
    