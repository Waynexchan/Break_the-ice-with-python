'''
Question:
Define a function which can compute the sum of two numbers.

Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

def add():
  num1, num2 = int(input()),int(input())
  total = num1+num2
  print(total)

add()

'''
'''
Define a function that can convert a integer into a string and print it in console.

Hints:
Use str() to convert a number to string.

def to_s():
  s = str(int(input()))
  print(s)

to_s()
'''
'''
Question:
Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

Hints:
Use int() to convert a string to integer.

def to_i():
  i = int(input())
  print(i)

to_i()
'''

'''
Define a function that can accept two strings as input and concatenate them and then print it in console.

Hints:
Use + sign to concatenate the strings.

def concatenate():
  s1,s2 = input(),input()
  print(s1 + s2)

concatenate()
'''
'''
Question:
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

Hints:
Use len() function to get the length of a string.

def length():
  s1,s2 = input(),input()
  if len(s1) > len(s2):
    print(s1)
  elif len(s2) > len(s1):
    print(s2)
  else:
    print(s1)
    print(s2)

length()
'''

  
