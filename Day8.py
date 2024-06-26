'''
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

def count_frequency():
  word_count={}
  s = input().split(' ')
  for item in s:
    if item in word_count:
      word_count[item] += 1
    else:
      word_count[item] = 1

  for word, count in sorted(word_count.items()):
    print(f'{word} : {count}')

count_frequency()

'''
'''
Question:
Write a method which can calculate square value of number

Hints:
Using the ** operator which can be written as n**p where means n^p

def sqt():
  n = int(input())
  value =n ** 2
  print(value)

sqt()
'''
'''
Question:
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function

Hints:
The built-in document method is __doc__
'''
''''''
'''
def get_value():
  """
  convert input in to a absolute integer
  """
  no = abs(int(input()))
  print(no)
  print(get_value.__doc__)

get_value()
'''
'''
Question:
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter or set the value later


class Animal():
  def __init__(self,name= None,age= 0):
    self.name = name
    self.age = age

x = Animal('John',18)
print(f'{x.name},{x.age}')
'''
