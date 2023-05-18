# Manipulating Strings

## String Literals

```python
spam = 'That is Alice'
```

### Double Quotes

```python
spam = "That is Alice's cat."
```

### Escape Character

```python
spam = 'Say hi to Bob\'s mother.'
```

| Escape character | Prints as | 
|---|---|
| \' | Single quote| 
| \" | Double quote| 
| \t | Tab| 
| \n | Newline (line break)| 
| \\ | Backslash| 

```bash
>>> print("Hello there!\nHow are you?\nI\'m doing fine.")
Hello there!
How are you?
I'm doing fine.
```

### Raw Strings

A raw string completely ignores all escape characters and prints any backslash that appears in the string

```bash
>>> print(r'That is Carol\'s cat.')
That is Carol\'s cat.
```

### Multiline Strings with Triple Quotes

```python
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')
```

```bash
Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob
```

### Multiline Comments

```python
"""This is a test Python program.
Written by Al Sweigart al@inventwithpython.com
This program was designed for Python 3, not Python 2.
"""
def spam():
 """This is a multiline comment to help
 explain what the spam() function does."""
 print('Hello!')
 ```

### Indexing and Slicing Strings

```bash
>>> spam = 'Hello world!'
>>> spam[0]
'H'
>>> spam[4]
'o'
>>> spam[-1]
'!'
>>> spam[0:5]
'Hello'
>>> spam[:5]
'Hello'
>>> spam[6:]
'world!'
```

```bash
>>> spam = 'Hello world!'
>>> fizz = spam[0:5]
>>> fizz
'Hello'
```

### The in and not in Operators with Strings

```bash
>>> 'Hello' in 'Hello World'
True
>>> 'Hello' in 'Hello'
True
>>> 'HELLO' in 'Hello World'
False
>>> '' in 'spam'
True
>>> 'cats' not in 'cats and dogs'
False
```

## Useful String Methods


### The upper(), lower(), isupper(), and islower() String Methods

```bash
>>> spam = 'Hello world!'
>>> spam = spam.upper()
>>> spam
'HELLO WORLD!'
>>> spam = spam.lower()
>>> spam
'hello world!'
```

```python
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
 print('I feel great too.')
else:
 print('I hope the rest of your day is good.')
```

```bash
>>> spam = 'Hello world!'
>>> spam.islower()
False
>>> spam.isupper()
False
>>> 'HELLO'.isupper()
True
>>> 'abc12345'.islower()
True
>>> '12345'.islower()
False
>>> '12345'.isupper()
False
```

```bash
>>> 'Hello'.upper()
'HELLO'
>>> 'Hello'.upper().lower()
'hello'
>>> 'Hello'.upper().lower().upper()
'HELLO'
>>> 'HELLO'.lower()
'hello'
>>> 'HELLO'.lower().islower()
True
```

### The isX String Methods

```bash
>>> 'hello'.isalpha()
True
>>> 'hello123'.isalpha()
False
>>> 'hello123'.isalnum()
True
>>> 'hello'.isalnum()
True
>>> '123'.isdecimal()
True
>>> ' '.isspace()
True
>>> 'This Is Title Case'.istitle()
True
>>> 'This Is Title Case 123'.istitle()
True
>>> 'This Is not Title Case'.istitle()
False
>>> 'This Is NOT Title Case Either'.istitle()
False
```

```python
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')
 ```

 ### The startswith() and endswith() String Methods

```bash
 >>> 'Hello world!'.startswith('Hello')
True
>>> 'Hello world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
False
>>> 'Hello world!'.startswith('Hello world!')
True
>>> 'Hello world!'.endswith('Hello world!')
True
```

### The join() and split() String Methods

```bash
>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'
```

```bash
>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
```

```bash
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
```

```bash
>>> spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
Please do not drink it.
Sincerely,
Bob'''
>>> spam.split('\n')
['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the 
fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.', 
'Sincerely,', 'Bob']
```

### Justifying Text with rjust(), ljust(), and center()

```bash
>>> 'Hello'.rjust(10)
' Hello'
>>> 'Hello'.rjust(20)
' Hello'
>>> 'Hello World'.rjust(20)
' Hello World'
>>> 'Hello'.ljust(10)
'Hello '
```

```bash
>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'
```

```bash
>>> 'Hello'.center(20)
' Hello '
>>> 'Hello'.center(20, '=')
'=======Hello========'
```

```python
def printPicnic(itemsDict, leftWidth, rightWidth):
 print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
 for k, v in itemsDict.items():
 print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
134 Chapter 6
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
```

### Removing Whitespace with strip(), rstrip(), and lstrip()

```bash
>>> spam = ' Hello World '
>>> spam.strip()
'Hello World'
>>> spam.lstrip()
'Hello World '
>>> spam.rstrip()
' Hello World'
```

```bash
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
# Passing strip() the argument 'ampS' will tell it to strip occurences of a, m, p, and capital S from the ends of the string stored in spam
>>> spam.strip('ampS')
'BaconSpamEggs'
```
### Copying and Pasting Strings with the pyperclip Module

```bash
>>> import pyperclip
>>> pyperclip.copy('Hello world!')
>>> pyperclip.paste()
'Hello world!'
```

