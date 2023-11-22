#q7
marks={'math':26,
     'english':27,
     'iot':28,
     'physic':29,
     'python':30}


val=max(marks.values())
val1=min(marks.values())
key=[]
key1=[]
for i in marks:
    m=marks[i]
    if marks[i]==val:
        key.append(i)
    if marks[i]==val1:
        key1.append(i)
    
print('maximum',key,val)
print('minimum',key1,val1)
