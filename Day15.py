import re
def divide_email():
  regex = r'^(.+?)@([^.]+)\..+$'
  email = input('Please enter the email address: ')

  match = re.match(regex, email)

  if match:
    print(match.group(2))
  else:
    print('not found')

divide_email()