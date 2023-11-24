def factor(num):
    lst=[]
    for i in range(1,num):
        if num%i==0:
            lst.append(i)
    return lst
num=int(input())
d=factor(num)
print(d)
