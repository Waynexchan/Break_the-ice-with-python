from collections import Counter

def check(t):

    return Counter(t)

def dict_viewer(char_count):
    for x, y in char_count.items():
        print(f'{x},{y}')

text = input(">")
char_count = check(text)
dict_viewer(char_count)
    
      