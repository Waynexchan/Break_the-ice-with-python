'''
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which
contains every number.Suppose the following input is supplied to the program:

34,67,55,33,12,98
Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.tuple() method can convert list to tuple
'''
import math
from itertools import combinations

# def transform():
#     data= (input('Enter a sequence of comma-separated numbers: '))
#     lst = data.split(',')
#     tpl = tuple(lst)
#     print(lst)
#     print(tpl)
#
# transform()

'''
Question:
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use init method to construct some parameters
'''

# class Transform():
#
#     def __init__(self):
#         self.s = None
#
#     def get_string(self):
#         self.s = input('Enter: ') #Enter string
#
#     def print_string(self):
#         print(self.s.upper()) #transform to upper case
#
#
# x = Transform()
# x.get_string()
# x.print_string()

'''
Question:
Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma 
separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24
Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it 
should be printed as 26).In case of input data being supplied to the question, it should be assumed to be a console input.
'''


# def calculate_q(d_values, c=50, h=30):
#     q_value = [str(int(math.sqrt((2 * c * int(d)) / h))) for d in d_values]
#     return ','.join(q_value)
#
#
# d_values = input('enter d: ').split(',')
# print(calculate_q(d_values))

'''
Question:
_Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.


'''

# def arr():
#
#     x,y = map(int,input('enter x,y value: ').split(','))
#     li = []
#
#     for i in range(x):
#         inner_li= []
#         for j in range(y):
#             inner_li.append(i * j)
#         li.append(inner_li)
#     print(li)
#
# arr()

# def arr():
#
#     x,y = map(int,input('enter x,y value: ').split(','))
#     li = [[i*j for j in range(y)] for i in range(x)]
#     print(li)
#
# arr()

'''
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

# def li_sort():
#     li = input('please enter the string: ').split(',')
#     li.sort()
#     print(','.join(li))
#
# li_sort()

'''
Question:
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.


'''

