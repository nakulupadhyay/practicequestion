ch=input("enter the string")
reg=''
for i in ch:
    c=ch.count(i)
    if (c >=2) and i not in reg:
        reg+=i
        print(i,end='')
    
        
        
