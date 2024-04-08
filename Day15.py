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

def find_num():
  regex = r'\b\d+\b'
  senetence = input('Please enter the sentence: ')

  integer = re.findall(regex,senetence)
  print(integer)

find_num()