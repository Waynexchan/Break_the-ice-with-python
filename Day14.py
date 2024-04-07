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