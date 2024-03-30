import math
'''
def square_odd():
  sentence = input().split(',')
  list= [str(int(math. pow(int(item),2))) for item in sentence if int(item) %2 != 0]

  print(','.join(list))
  
square_odd()
'''

def trans():
  total= 0
  
  while True:
    sentence = input().split()
    if not sentence:
      break
    status, num = map(str, sentence)


    if status== 'D':
      total += int(num)
    elif status == 'W':
      total -= int(num)

  print(total)

trans()
  
  
   