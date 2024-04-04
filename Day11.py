'''
def tup():
  tup= (1,2,3,4,5,6,7,8,9,10)
  li1 , li2 = [],[]
  for i in range(0,5):
    li1.append(tup[i])
  for i in range(5,10):
    li2.append(tup[i])
  print(li1)
  print(li2)

tup()
'''
'''
def even_tup():
  tup=(1,2,3,4,5,6,7,8,9,10)
  li, even_li=[],[]
  for i in range(0,10):
    li.append(tup[i])
  for i in li:
    if i %2 == 0:
      even_li.append(i)
  print(tuple(even_li))

even_tup()
'''
'''
def check_s():
  s= (str(input())).lower()
  if s == 'yes':
    print('Yes')
  else:
    print('No')
    

check_s()
'''
'''
def sqt():
  li= [1,2,3,4,5,6,7,8,9,10]
  element= map(lambda x: x**2,li)
  print(list(element))

sqt()
'''
'''
def even_sqt():
  li= [1,2,3,4,5,6,7,8,9,10]
  even= filter(lambda x : x %2==0,li)
  element= map(lambda x: x**2,even)
  print(list(element))

even_sqt()
'''
'''
def even_li():
  li=[]
  for i in range(1,21):
    li.append(i)
  even_o= filter(lambda x: x%2==0,li)
  print(list(even_o))

even_li()

'''