def intersection(arr1,arr2):
    c=[]
    for i in arr1:
        if i in arr2:
            c.append(i)
    return c

def union(arr1,arr2):
    x=[]
    for i in arr1+arr2:
        if i not in x:
            x.append(i)
    return x

def symmatric_diffrenece(arr1,arr2):
    un=union(ls1,ls2)
    inter=intersection(ls1,ls2)
    for i in inter:
        un.remove(i)
    return un

ls1=[1,3,6]
ls2=[3,8,9,1]
re1=intersection(ls1,ls2)
print(re1)

re2=union(ls1,ls2)
print(re2)

re3=symmatric_diffrenece(ls1,ls2)
print(re3)
