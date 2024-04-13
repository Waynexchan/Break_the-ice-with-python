'''
li= [5,6,77,45,22,12,24]
new_li =[x for x in li if x %2 !=0 ]
print(new_li)

li2 = [12,24,35,70,88,120,155]

newli2= list(filter(lambda x : x%5 !=0 and x%7 !=0, li2))

print(newli2)
'''
'''
li= [12,24,35,70,88,120,155]
index = [0, 2, 4, 6]
new_li = [i for (j, i) in enumerate(li) if j not in index ]
print(new_li)
'''

li= [12,24,35,70,88,120,155]
index =[2,3,4]
new_li= [ i for (j, i) in enumerate(li) if j not in index]
print(new_li)