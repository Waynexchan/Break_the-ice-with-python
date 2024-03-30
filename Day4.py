'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

'''

def count_letters():
  upper_count= 0
  lower_count= 0
  sentence = input()
  for letter in sentence:
    if ord(letter) > 96 and ord(letter)< 123:
      lower_count += 1
    elif ord(letter) > 64 and ord(letter) < 91:
      upper_count += 1
    else:
      pass
  print(f'UPPER CASE {upper_count}')
  print(f'LOWER CASE {lower_count}')

count_letters()

'''

'''
Question:

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''

def cal_a():
  val= int(input())
  total = val + val*11 +val*111 + val*1111
  print (total)

cal_a()

def cal_b():
  val= input()
  total = int(val) + int(val*2) +int(val*3)+ int(val*4)
  print (total)

cal_b()