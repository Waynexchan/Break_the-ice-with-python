'''
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
Consider use range(#begin, #end) method.
'''
import math

'''
def divisibly_by7():
    list = []
    for no in range(2000, 3201):
        if no % 7 == 0 and no % 5 != 0:
            list.append(no)
    print(list)


divisibly_by7()
'''

'''
Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated
sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''


def factorial_no(no):
    no = int(no)
    result = 1
    for i in range(1, no + 1):
        result *= i
    return result


def math_factorial(no):
    return math.factorial(no)


print(factorial_no(8))


'''
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral 
number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to 
the program: 8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''


def pow(no):
    no =int(no)
    dict = {}
    for i in range(1, no + 1):
        dict[i] = i * i
    print(dict)


pow(8)
