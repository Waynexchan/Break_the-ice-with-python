'''def second():
  n= int(input())
  arr = map(int,input().split())
  arr = list(set(arr))
  arr.sort()
  print(arr[-2])

second()
'''

import textwrap

string = input()
width = int(input())

print(textwrap.fill(string,width))

import string
def print_rangoli(size):
    n = size
    alph = string.ascii_lowercase
    width = 4 * n - 3

    ans = []
    for i in range(n):
        left = '-'.join(alph[n - i - 1:n])
        mid = left[-1:0:-1] + left
        final = mid.center(width, '-')
        ans.append(final)

    if len(ans) > 1:
        for i in ans[n - 2::-1]:
            ans.append(i)
    ans = '\n'.join(ans)
    print(ans)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

import calendar

month, day, year = map(int, input().split())

dayId = calendar.weekday(year, month, day)
print(calendar.day_name[dayId].upper())
