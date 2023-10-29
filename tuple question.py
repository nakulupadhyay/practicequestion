# Write a Python program to create a tuple
t=(10,)
print(t,type(t))


#Write a Python program to add an item in a tuple
t=(10,22,25,78)
t1=(10,)
t3=t+t1
print(t3)



#Write a Python program to get the 4th element and 4th element from last of a tuple.

t=(10,15,16,'hi',56,8,89)
print(t,t[4:5],t[-4:-3])



#Write a Python program to find the repeated items of a tuple
t=(10,15,16,'hi',56,89,89)
for i in t:
    t1=t.count(i)
    if t1>=2:
         print(i,t1)


#Write a Python program to check whether an element exists within a tuple.
t=(10,14,'hi','say',16,25,26)
t2=input("enter a tuple:")
if t2 in t:
    print("element is exist")
else:
    print("element is not exist")






