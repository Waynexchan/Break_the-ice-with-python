import random
'''
def even():
  s= input()
  s_li = s.split(',')

  for i in s_li:
    assert int(i)%2 ==0, 'It contains odds number'

even()
'''

'''
def expression():
  expression = input()
  result = eval(expression)

  print(result)

expression()
'''
'''
def binary_search(li,item):
  low = 0
  high = len(li) -1

  while low <= high:
    mid = round((low + high)/2)
    if li[mid] ==item:
      return mid
    elif li[mid] <= item:
      low = mid +1
    else:
      high = mid -1
  return None


lst = [1,3,5,7,]
print(binary_search(lst, 9))   
'''

'''
def ran():
  start = int(input())
  end = int(input())
  ran_no = random.uniform(start, end)
  print(ran_no)

ran()
'''