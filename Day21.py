s = input()
li = s.split()
index= [0,4,5]
new_li= list(x for (i,x) in enumerate(li) if i  not in index)
print(new_li)