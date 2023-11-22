def in_both(wd1, wd2):
        "Takes two strings, returns a sorted list of common characters" 
        common = []
        for c in wd1:
            if c in wd2:
                common.append(c)			
        return sorted(common)
d=in_both('pear', 'apple')
e=in_both('linguistics', 'economics')
print(d)
print(e)
