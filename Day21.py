'''
s = input()
li = s.split()
index= [0,4,5]
new_li= list(x for (i,x) in enumerate(li) if i  not in index)
print(new_li)
'''
'''
li=  [12,24,35,24,88,120,155]
new_li =[x for x in li if x != 24]
print(new_li)
'''
'''
li = [1,3,6,78,35,55] 
lib = [12,24,35,24,88,120,155]
s1= set(li)
s2= set(lib)
intersection = set.intersection(s1,s2)
print(intersection)
'''

li= [12,24,35,24,88,120,155,88,120,155]
s1= set(li)
new_li =[]
for x in s1:
  new_li.append(x)

print(new_li)