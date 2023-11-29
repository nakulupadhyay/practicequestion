def display_info(name,rolln,sec='cd',clg='GLA'):
    data=f'''
name       :{name}
section    :{sec}
roll number:{rolln}
college    :{clg}
'''
    return data
out=display_info('ankit',4)
out1=display_info(4,'ankit')
print(out)
print(out1)
