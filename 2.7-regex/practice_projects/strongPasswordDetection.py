# Strong Password Detection
# Write a function that uses regular expressions to make sure the password 
# string it is passed is strong. A strong password is defined as one that is at 
# least eight characters long, contains both uppercase and lowercase characters, 
# and has at least one digit. You may need to test the string against multiple regex 
# patterns to validate its strength.

import re

def passwordisstrong(pwd):

    mt = re.compile(r'^.{8,100}$')
    if mt.search(pwd) == None:
        print('Should have at least eight characters long')
        return False
    
    mt = re.compile(r'\d')
    if mt.search(pwd) == None:
        print('Should have at least one digital')
        return False
    
    mt = re.compile(r'[A-Z]')
    if mt.search(pwd) == None:
        print('Should have at least upper case')
        return False
    
    mt = re.compile(r'[a-z]')
    if mt.search(pwd) == None:
        print('Should have at least lower case')
        return False
    
    print('valid')
    return True

passwordisstrong('abc')
passwordisstrong('abcdefgh')
passwordisstrong('abcd1234')
passwordisstrong('ABCD1234')
passwordisstrong('ABCD1234abcd')
