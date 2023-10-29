# bottle neck problem
a=[int(i) for i in input().split()]
a2=[]
for i in a:
    z=a.count(i)
    if z>=2:
        a2.append(z)
print(a2)
        

