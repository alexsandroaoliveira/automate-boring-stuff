# Lists

## The List Data Type

```batch
>>> [1, 2, 3]
[1, 2, 3]
>>> ['cat', 'bat', 'rat', 'elephant']
['cat', 'bat', 'rat', 'elephant']
>>> ['hello', 3.1415, True, None, 42]
['hello', 3.1415, True, None, 42]
>>> spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> spam[0]
['cat', 'bat']
>>> spam[0][1]
'bat'
>>> spam[1][4]
50
```

### Negative Indexes

```batch
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[-1]
'elephant'
>>> spam[-3]
'bat'
```

### Getting Sublists with Slices

```batch
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0:4]
['cat', 'bat', 'rat', 'elephant']
>>> spam[1:3]
['bat', 'rat']
>>> spam[0:-1]
['cat', 'bat', 'rat']
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[:2]
['cat', 'bat']
>>> spam[1:]
['bat', 'rat', 'elephant']
Lists 83
>>> spam[:]
['cat', 'bat', 'rat', 'elephant']
```


### Getting a List’s Length with len()

```batch
>>> spam = ['cat', 'dog', 'moose']
>>> len(spam)
3
```

### Changing Values in a List with Indexes

```batch
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[1] = 'aardvark'
>>> spam
['cat', 'aardvark', 'rat', 'elephant']
>>> spam[2] = spam[1]
>>> spam
['cat', 'aardvark', 'aardvark', 'elephant']
>>> spam[-1] = 12345
>>> spam
['cat', 'aardvark', 'aardvark', 12345]
```

### List Concatenation and List Replication

```batch
>>> [1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
>>> ['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
>>> spam = [1, 2, 3]
>>> spam = spam + ['A', 'B', 'C']
>>> spam
[1, 2, 3, 'A', 'B', 'C']
```

### Removing Values from Lists with del Statements

```batch
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat', 'elephant']
>>> del spam[2]
>>> spam
['cat', 'bat']
```

## Working with Lists

```python
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + 
        ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)
```

### Using for Loops with Lists

```python
for i in range(4):
    print(i)

for i in [0, 1, 2, 3]:
    print(i)
```

### The in and not in Operators

```batch
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
True
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam
False
>>> 'howdy' not in spam
False
>>> 'cat' not in spam
True
```

### The Multiple Assignment Trick

```batch
>>> cat = ['fat', 'black', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]
```

is equals to:

```batch
>>> cat = ['fat', 'black', 'loud']
>>> size, color, disposition = cat
```

## Augmented Assignment Operators

| Augmented assignment statement|Equivalent assignment statement|
|---|---|
| spam = spam + 1 | spam += 1 |
| spam = spam - 1 | spam -= 1 |
| spam = spam * 1 | spam *= 1 |
| spam = spam / 1 | spam /= 1 |
| spam = spam % 1 | spam %= 1 |

```batch
>>> spam = 'Hello'
>>> spam += ' world!'
>>> spam
'Hello world!'
Lists 89
>>> bacon = ['Zophie']
>>> bacon *= 3
>>> bacon
['Zophie', 'Zophie', 'Zophie']
```

## Methods

### Finding a Value in a List with the index() Method

```batch
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> spam.index('hello')
0
>>> spam.index('heyas')
3
>>> spam.index('howdy howdy howdy')
Traceback (most recent call last):
 File "<pyshell#31>", line 1, in <module>
 spam.index('howdy howdy howdy')
ValueError: 'howdy howdy howdy' is not in list
```

### Adding Values to Lists with the append() and insert() Methods

```batch
rem append
>>> spam = ['cat', 'dog', 'bat']
>>> spam.append('moose')
90 Chapter 4
>>> spam
['cat', 'dog', 'bat', 'moose']

rem insert
>>> spam = ['cat', 'dog', 'bat']
>>> spam.insert(1, 'chicken')
>>> spam
['cat', 'chicken', 'dog', 'bat']
```

### Removing Values from Lists with remove() 
```batch
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'elephant']

>>> spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
>>> spam.remove('cat')
>>> spam
['bat', 'rat', 'cat', 'hat', 'cat']
```

### Sorting the Values in a List with the sort() Method

```batch
>>> spam = [2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']

Rem  Reverse
>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']

Rem  Must be same type
>>> spam = [1, 3, 2, 4, 'Alice', 'Bob']
>>> spam.sort()
Traceback (most recent call last):
 File "<pyshell#70>", line 1, in <module>
 spam.sort()
TypeError: unorderable types: str() < int()

Rem  sort() uses “ASCIIbetical order” 
>>> spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

Rem to use regular alphabetical order
>>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort(key=str.lower)
>>> spam
['a', 'A', 'z', 'Z']
```

## Exceptions to Indentation Rules in Python

```python
spam = ['apples',
  'oranges',
                     'bananas',
'cats']
print(spam)

print('Four score and seven ' + \
 'years ago...')
```

## List-like Types: Strings and Tuples

```batch
>>> name = 'Zophie'
>>> name[0]
'Z'
>>> name[-2]
'i'
>>> name[0:4]
'Zoph'
>>> 'Zo' in name
True
>>> 'z' in name
False
>>> 'p' not in name
False
>>> for i in name:
 print('* * * ' + i + ' * * *')
 ```

 ## Mutable and Immutable Data Types

```batch
>>> name = 'Zophie a cat'
>>> name[7] = 'the'
Traceback (most recent call last):
 File "<pyshell#50>", line 1, in <module>
 name[7] = 'the'
TypeError: 'str' object does not support item assignment

>>> name = 'Zophie a cat'
>>> newName = name[0:7] + 'the' + name[8:12]
>>> name
'Zophie a cat'
Lists 95
>>> newName
'Zophie the cat'
```

## The Tuple Data Type

```batch
>>> eggs = ('hello', 42, 0.5)
>>> eggs[0]
'hello'
>>> eggs[1:3]
(42, 0.5)
>>> len(eggs)
3

>>> eggs = ('hello', 42, 0.5)
>>> eggs[1] = 99
Traceback (most recent call last):
 File "<pyshell#5>", line 1, in <module>
 eggs[1] = 99
TypeError: 'tuple' object does not support item assignment

>>> type(('hello',))
<class 'tuple'>
>>> type(('hello'))
<class 'str'>
```

## Converting Types with the list() and tuple() Functions

```batch 
>>> tuple(['cat', 'dog', 5])
('cat', 'dog', 5)
>>> list(('cat', 'dog', 5))
['cat', 'dog', 5]
>>> list('hello')
['h', 'e', 'l', 'l', 'o']
```

## References

```batch
>>> spam = 42
>>> cheese = spam
>>> spam = 100
>>> spam
100
>>> cheese
42

>>> spam = [0, 1, 2, 3, 4, 5]
>>> cheese = spam
>>> cheese[1] = 'Hello!'
>>> spam
[0, 'Hello!', 2, 3, 4, 5]
>>> cheese
[0, 'Hello!', 2, 3, 4, 5]
```

### Passing References

```batch
def eggs(someParameter):
 someParameter.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam)
```

### The copy Module’s copy() and deepcopy() Functions

```batch
>>> import copy
>>> spam = ['A', 'B', 'C', 'D']
>>> cheese = copy.copy(spam)
>>> cheese[1] = 42
>>> spam
['A', 'B', 'C', 'D']
>>> cheese
['A', 42, 'C', 'D']
```