def lst(l):
    if all(l[i]<=l[i+1] for i in range(len(l)+1)):
        return 1
    elif all(l[i]>=l[i+1] for i in range(len(l)+1)):
        return -1
    else:
      return -1
s=0
le=[]
while s<5:
   l=int(input("enter the number"))
   le.append(l)
   s+=1
s=lst(le)
print(s)

        
