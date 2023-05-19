# Regex Version of strip()
# Write a function that takes a string and does the same thing as the strip()
# string method. If no other arguments are passed other than the string to 
# strip, then whitespace characters will be removed from the beginning and 
# end of the string. Otherwise, the characters specified in the second argument 
# to the function will be removed from the string.

import re

def regexStrip(str, chr = '\s'):
    
    pat = rf'''^
        {chr}*
        ([^{chr}]*)
        {chr}*$'''
    
    mt = re.compile(pat, re.VERBOSE)

    sr = mt.search(str)
    if sr == None:
        return str
    
    print(sr.groups())
    return sr.group(1)


print(regexStrip('  abc'))
print(regexStrip('abc   '))
print(regexStrip('  abc   '))
print(regexStrip('___abc___', '_'))
