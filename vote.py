def vote(a,b):
    if b>=18:
        print(a,"give vote")
    else:
        print(a,"donot give vote")

name=input("enter your name ")
age=int(input("enter your age:"))
vote(name,age)
