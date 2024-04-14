from collections import Counter
'''
def check(t):

    return Counter(t)

def dict_viewer(char_count):
    for x, y in char_count.items():
        print(f'{x},{y}')

text = input(">")
char_count = check(text)
dict_viewer(char_count)
'''
'''
def rev():
  s = input()
  l = s[::-1]
  print(l)

rev()
'''
'''
s= 'H1e2l3l4o5w6o7r8l9d'
l= s[::2]
print(l)
'''
import itertools
list = [1,2,3]

permutations = itertools.permutations(list)

for perm in permutations:
  print(perm)


def animal_counter(lst):
    chickens = 0	
    rabbits = 0
    for i in lst:
        if i == 2:
            chickens += 1
        elif i == 4:
            rabbits += 1
    print(f"Number of chickens is {chickens}\nNumber of rabbits is {rabbits}")


def animal_calculator(total_legs, total_heads, legs_of_each_species):
    combinations = itertools.combinations_with_replacement(legs_of_each_species, total_heads)
    correct_combos = []
    for i in list(combinations):
        if sum(i) == total_legs:
            correct_combos.append(i)
    print(correct_combos)
    for i in correct_combos:
        animal_counter(i)

animal_calculator(94, 35, legs_of_each_species=[2,4])

      