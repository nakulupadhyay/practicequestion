rows=26
val=65
for i in range(1,rows+1):
    for j in range(i):
       print(chr(val),end='')
    for j in range(rows-i):
        print(' ',end='')
    for j in range(rows-i):
        print(' ',end='')    
    for j in range(i):
        print(chr(val),end='')
    if val>90:
        val=65
    val+=1
    print()
