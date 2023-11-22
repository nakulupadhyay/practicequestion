def python_def_prime(n):
    x = 2
    count = 0
    while count < n:
        for d in range(2, x, 1):
            if x % d == 0:
                x += 1
        else:
            print(x)
            x += 1
            count += 1
 

n = 10
 

print("First 10 prime numbers are:  ")
python_def_prime(n)
