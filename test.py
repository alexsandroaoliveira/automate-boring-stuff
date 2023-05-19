import re

reg = re.compile(r'''^
    (
        (
            \d{1,3},
            (\d{3},)?
            (\d{3},)?
            (\d{3},)?
            (\d{3},)?
            \d{3}
        )
        |
        (\d{1,3})
    )$
    ''', re.VERBOSE)

s1 = '42'
match = reg.search(s1) != None
print(s1.rjust(10) + ': ' + str(match))

s1 = '1,234'
match = reg.search(s1) != None
print(s1.rjust(10) + ': ' + str(match))

s1 = '6,368,745'
match = reg.search('6,368,745') != None
print(s1.rjust(10) + ': ' + str(match))

s1 = '12,34,567'
match = reg.search('12,34,567') != None
print(s1.rjust(10) + ': ' + str(match))

s1 = '1234'
match = reg.search('1234') != None
print(s1.rjust(10) + ': ' + str(match))

s1 = '123,231,322,324'
match = reg.search('1234') != None
print(s1.rjust(10) + ': ' + str(match))
