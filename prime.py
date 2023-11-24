def prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return count==2
num=int(input("enter a number"))
b=prime(num)
print(b)
