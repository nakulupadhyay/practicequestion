def display_info(**dct):
    data=f'''
name       :{dct.get('name')}
section    :{dct.get('sec')}
roll number:{dct.get('rooln')}
college    :{dct.get('clg')}
'''
    return data
out=display_info(name='ankit')
print(out)
