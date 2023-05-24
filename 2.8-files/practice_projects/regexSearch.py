import sys
import re
import os

pat = sys.argv[1]
print(pat)

reg = re.compile(pat)

files = os.listdir('./')

for fileName in files:
    if not fileName.endswith(r'.txt'):
        continue
    
    file = open(fileName, 'r')
    fileStr = file.read()
    file.close()

    results = reg.findall(fileStr)
    if results != None:
        for item in results:
            print(f'{fileName}: {item}')
