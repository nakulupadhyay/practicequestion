c=int(input("enter the number:-"))
s=0
cp=c
while c!=0:
    r=c%10
    s=s*10+r
    c=c//10
    
print(f'reverse of {cp} is {s}')
