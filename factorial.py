def python_def_factorial(n):
    if n == 1:
        return n
    else:
        return n*python_def_factorial(n-1)
 

num = 6
 
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", python_def_factorial(num))
