li= [5,6,77,45,22,12,24]
new_li =[x for x in li if x %2 !=0 ]
print(new_li)

li2 = [12,24,35,70,88,120,155]

newli2= list(filter(lambda x : x%5 !=0 and x%7 !=0, li2))

print(newli2)