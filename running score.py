a=[int(i)for i in input("enter values").split()]
ls=[]
for i in a:
    if i not in ls:
        ls.append(i)
z=max(ls)
ls.remove(z)
print(max(ls))
        


 
