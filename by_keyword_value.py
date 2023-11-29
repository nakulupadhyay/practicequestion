def display_info(name,rolln,sec,clg):
    data=f'''
name       :{name}
section    :{sec}
roll number:{rolln}
college    :{clg}
'''
    return data
out=display_info(rolln=4,sec='cd',clg='GLA',name='ankit')
print(out)
