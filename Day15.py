import re
'''


def divide_email():
  regex = r'^(.+?)@([^.]+)\..+$'
  email = input('Please enter the email address: ')

  match = re.match(regex, email)

  if match:
    print(match.group(2))
  else:
    print('not found')

divide_email()
'''
'''
def find_num():
  regex = r'\b\d+\b'
  senetence = input('Please enter the sentence: ')

  integer = re.findall(regex,senetence)
  print(integer)

find_num()
'''
'''
def unicode():
  word = input('Please enter the word: ')

  for character in word:
    print(f'{character}: {ord(character)}')

unicode()
'''
'''
def convert_u():
  s = input('Please enter the string: ')
  u = s.encode('utf-8')
  print(u)

convert_u()
'''
'''
# -*- coding: utf-8 -*-

'''

def cal(n):
  print(round(sum(map(lambda x: x/(x+1),range(1, n+1))),2))

cal(5)