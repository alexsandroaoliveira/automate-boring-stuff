# Reading and Writing Files

```python
import os
os.path.join('usr', 'bin', 'spam')
# 'usr\\bin\\spam'

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

# C:\Users\asweigart\accounts.txt
# C:\Users\asweigart\details.csv
# C:\Users\asweigart\invite.docx
```

## The Current Working Director

```python
>>> import os
>>> os.getcwd()
'C:\\Python34'
>>> os.chdir('C:\\Windows\\System32')
>>> os.getcwd()
'C:\\Windows\\System32'


>>> os.chdir('C:\\ThisFolderDoesNotExist')
Traceback (most recent call last):
 File "<pyshell#18>", line 1, in <module>
 os.chdir('C:\\ThisFolderDoesNotExist')
FileNotFoundError: [WinError 2] The system cannot find the file specified: 
'C:\\ThisFolderDoesNotExist'
```

## Absolute vs. Relative Paths

- An absolute path, which always begins with the root folder
- A relative path, which is relative to the program’s current working directory

C:\bacon

| Relative Paths | Absolute Paths |
|---|---|
| .\ | C:\bacon |
| ..\ | C:\ |
| .\fizz | C:\bacon\fizz |
| .\fizz\spam.txt | C:\bacon\fizz\spam.txt |
| .\spam.txt | C:\bacon\spam.txt |
| ..\eggs | C:\eggs |
| ..\eggs\spam.txt | C:\eggs\spam.txt |
| ..\spam.txt | C:\spam.txt |

## Creating New Folders with os.makedirs()

```python
>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')
```

## The os.path Module

### Handling Absolute and Relative Paths

- Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.
- Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.
- Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path

```python
>>> os.path.abspath('.')
'C:\\Python34'
>>> os.path.abspath('.\\Scripts')
'C:\\Python34\\Scripts'
>>> os.path.isabs('.')
False
>>> os.path.isabs(os.path.abspath('.'))
True


>>> os.path.relpath('C:\\Windows', 'C:\\')
'Windows'
>>> os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
'..\\..\\Windows'
>>> os.getcwd()
'C:\\Python34


>>> path = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.basename(path)
'calc.exe'
>>> os.path.dirname(path)
'C:\\Windows\\System32'


>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
>>> os.path.split(calcFilePath)
('C:\\Windows\\System32', 'calc.exe')


>>> (os.path.dirname(calcFilePath), os.path.basename(calcFilePath))
('C:\\Windows\\System32', 'calc.exe')


>>> calcFilePath.split(os.path.sep)
['C:', 'Windows', 'System32', 'calc.exe']


>>> '/usr/bin'.split(os.path.sep)
['', 'usr', 'bin']
```



### Finding File Sizes and Folder Contents

```python
>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
776192
>>> os.listdir('C:\\Windows\\System32')
['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
--snip--
'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']

>>> totalSize = 0
>>> for filename in os.listdir('C:\\Windows\\System32'):
 totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
>>> print(totalSize)
1117846456

```

### Checking Path Validity

- Calling os.path.exists(path) will return True if the file or folder referred to in the argument exists and will return False if it does not exist.
- Calling os.path.isfile(path) will return True if the path argument exists and is a file and will return False otherwise.
- Calling os.path.isdir(path) will return True if the path argument exists and is a folder and will return False otherwise.

```python
>>> os.path.exists('C:\\Windows')
True
>>> os.path.exists('C:\\some_made_up_folder')
False
>>> os.path.isdir('C:\\Windows\\System32')
True
>>> os.path.isfile('C:\\Windows\\System32')
False
>>> os.path.isdir('C:\\Windows\\System32\\calc.exe')
False
>>> os.path.isfile('C:\\Windows\\System32\\calc.exe')
True

>>> os.path.exists('D:\\')
False
```

## The File Reading/Writing Process

### Opening Files with the open() Function

```python
>>> helloFile = open('C:\\Users\\your_home_folder\\hello.txt')

>>> helloFile = open('/Users/your_home_folder/hello.txt')
```

### Reading the Contents of Files

```python
>>> helloContent = helloFile.read()
>>> helloContent
'Hello world!'


>>> sonnetFile = open('sonnet29.txt')
>>> sonnetFile.readlines()
[When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my 
outcast state,\n', And trouble deaf heaven with my bootless cries,\n', And 
look upon myself and curse my fate,']
```

### Writing to Files

```python
>>> baconFile = open('bacon.txt', 'w') 
>>> baconFile.write('Hello world!\n')
13
>>> baconFile.close()
>>> baconFile = open('bacon.txt', 'a') 
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> baconFile = open('bacon.txt')
>>> content = baconFile.read()
>>> baconFile.close()
>>> print(content)
Hello world!
Bacon is not a vegetable.
```

### Saving Variables with the shelve Module

```python
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> shelfFile['cats'] = cats
>>> shelfFile.close()


>>> shelfFile = shelve.open('mydata')
>>> type(shelfFile) 
<class 'shelve.DbfilenameShelf'>
>>> shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
>>> shelfFile.close()


>>> shelfFile = shelve.open('mydata')
>>> list(shelfFile.keys())
['cats']
>>> list(shelfFile.values())
[['Zophie', 'Pooka', 'Simon']]
>>> shelfFile.close()
```

### Saving Variables with the pprint.pformat() Function

```python
>>> import pprint
>>> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
>>> fileObj = open('myCats.py', 'w')
>>> fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
83
>>> fileObj.close()


>>> import myCats
>>> myCats.cats
[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> myCats.cats[0]
{'name': 'Zophie', 'desc': 'chubby'}
>>> myCats.cats[0]['name']
'Zophie'

```