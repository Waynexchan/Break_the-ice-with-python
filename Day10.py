'''
def dict_square():
  d ={}
  for i in range(int(input("enter start: ")),int(input("enter end: "))+1):
    d[i] = i**2
  print(d)

dict_square()
'''
'''
def dict_square():
  d ={}
  for i in range(int(input("enter start: ")),int(input("enter end: "))+1):
    d[i] = i**2

  for key, value in d.items():
    print(f"Key: {key}")

dict_square()
'''
'''
def gen_list():
  li=[]
  for i in range(int(input("enter start: ")),int(input("enter end: "))+1):
    li.append(i**2)
  print(li)

gen_list()
'''
'''
def gen_list():
  li=[]
  for i in range(int(input("enter start: ")),int(input("enter end: "))+1):
    li.append(i**2)
  print(li[0:5])

gen_list()
'''
'''
def gen_list():
  li=[]
  for i in range(int(input("enter start: ")),int(input("enter end: "))+1):
    li.append(i**2)
  print(li[-5:])

gen_list()
'''
'''
def gen_list():
  li=[]
  for i in range(int(input("enter start: ")),int(input("enter end: "))+1):
    li.append(i**2)
  print(li[5:])

gen_list()
'''

def gen_tup():
  tup= tuple([i**2 for i in range(int(input("enter start: ")),int(input("enter end: "))+1) ])
  print(tup)

gen_tup()



