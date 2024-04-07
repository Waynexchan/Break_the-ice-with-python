'''
def test():
  try:
    a, b = int(input()),int(input())
    if a > b:
      print('True')
    else:
      print('False')
  except ValueError as e:
    print('Value Error')


test()
'''

class CustomException(Exception):
  '''
    Attributes:
      message:
  '''
  def __init__(self,message):
    self.message = message

num = int(input())

try:
  if num < 10:
    raise CustomException(" num is less than 10")
  elif num >20:
    raise CustomException(" num is greater than 10")
except CustomException as err:
  print('The error raises: '+ err.message)