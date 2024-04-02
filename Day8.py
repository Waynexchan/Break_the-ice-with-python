'''
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

Suppose the following input is supplied to the program:

New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:

2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

def count_frequency():
  word_count={}
  s = input().split(' ')
  for item in s:
    if item in word_count:
      word_count[item] += 1
    else:
      word_count[item] = 1

  for word, count in sorted(word_count.items()):
    print(f'{word} : {count}')

count_frequency()

'''