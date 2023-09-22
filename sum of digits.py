n= int(input("enter your number more than two digit:"))
s=0
while n!=0:
    r=n%10
    s=s+r
    n=n//10
print('sum of digitsis',s)
    
