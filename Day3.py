'''
Question
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world
'''
import re

# def sort_remove():
#     sentense = sorted(set((input().split(' '))))
#     print(' '.join(sentense))
#
# sort_remove()

'''
Question
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001
Then the output should be:

1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

# def check():
#     binary = input().split(',')
#     li=[]
#     for item in binary:
#         if int(item,2) % 5 == 0:
#             li.append(item)
#     print(','.join(li))
#
# check()

'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

# def check_even():
#     x, y = map(int,input().split(","))
#     li = []
#     for i in range(x, y):
#         if i % 2 == 0:
#             li.append(str(i))
#
#     print(','.join(li))
#
# check_even()

'''
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''


def cal_len():
    sentence = input()
    numbers = re.findall(r'\b\d+\b', sentence)
    letter = re.findall(r'[a-zA-Z]+', sentence)
    digits_len = sum(len(num) for num in numbers)
    letter_len = sum(len(word) for word in letter)

    print(f'LETTERS {letter_len}')
    print(f'DIGITS {digits_len}')


cal_len()
