'''
def even():
  s= input()
  s_li = s.split(',')

  for i in s_li:
    assert int(i)%2 ==0, 'It contains odds number'

even()
'''


def expression():
  expression = input()
  result = eval(expression)

  print(result)

expression()