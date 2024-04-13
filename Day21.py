'''
s = input()
li = s.split()
index= [0,4,5]
new_li= list(x for (i,x) in enumerate(li) if i  not in index)
print(new_li)
'''

li=  [12,24,35,24,88,120,155]
new_li =[x for x in li if x != 24]
print(new_li)