import re

file = open('sample.txt', 'r')
fileStr = file.read()
file.close()

newFileStr = fileStr

while True:
    reg = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB', re.IGNORECASE)
    mo = reg.search(newFileStr)

    if mo == None:
        break;
    
    print(f'Enter an {mo.group().lower()}')
    word = input()

    newFileStr = reg.sub(word, newFileStr, 1)

print(newFileStr)

file = open('mad_sample.txt', 'w') 
file.write(newFileStr)

