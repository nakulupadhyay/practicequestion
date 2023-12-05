def apna_fun(num):
    count=0
    for i in range (1,len(num)+1):
        if num%i==0:
            count+=1
    if count==2:
        return True
    else:
        return False
lst=[4,6,7,8,6,2,3,11,34,67]
out=list(filter(apna_fun,lst))
print(out)
