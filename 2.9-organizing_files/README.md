# Organizing Files

## Copying Files and Folders

```python
>> import shutil, os
>>> os.chdir('C:\\')
>>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
'C:\\delicious\\spam.txt'
>>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
'C:\\delicious\\eggs2.txt'

>>> import shutil, os
>>> os.chdir('C:\\')
>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
'C:\\bacon_backup'
``` 

## Moving and Renaming Files and Folders

```python
>>> import shutil
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs\\bacon.txt'

>>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
'C:\\eggs\\new_bacon.txt'

# WARNING: this renames the file bacon.txt to eggs
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
'C:\\eggs'

# Not exists
>>> shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')
Traceback (most recent call last):
 File "C:\Python34\lib\shutil.py", line 521, in move
 os.rename(src, real_dst)
FileNotFoundError: [WinError 3] The system cannot find the path specified: 
'spam.txt' -> 'c:\\does_not_exist\\eggs\\ham'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
 File "<pyshell#29>", line 1, in <module>
 shutil.move('spam.txt', 'c:\\does_not_exist\\eggs\\ham')
 File "C:\Python34\lib\shutil.py", line 533, in move
 copy2(src, real_dst)
 File "C:\Python34\lib\shutil.py", line 244, in copy2
 copyfile(src, dst, follow_symlinks=follow_symlinks)
 File "C:\Python34\lib\shutil.py", line 108, in copyfile
 with open(dst, 'wb') as fdst:
FileNotFoundError: [Errno 2] No such file or directory: 'c:\\does_not_exist\\
eggs\\ham'
```

## Permanently Deleting Files and Folders

- Calling os.unlink(path) will delete the file at path.
- Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
- Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

```python
import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        os.unlink(filename)

import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        #os.unlink(filename)
    print(filename)
```

## Safe Deletes with the send2trash Module

```python
>>> import send2trash
>>> baconFile = open('bacon.txt', 'a') # creates the file
>>> baconFile.write('Bacon is not a vegetable.')
>>> baconFile.close()
>>> send2trash.send2trash('bacon.txt')
```

## Walking a Directory Tree

```python
import os
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
 
    print('')

# The current folder is C:\delicious
# SUBFOLDER OF C:\delicious: cats 
# SUBFOLDER OF C:\delicious: walnut
# FILE INSIDE C:\delicious: spam.txt
# The current folder is C:\delicious\cats
# FILE INSIDE C:\delicious\cats: catnames.txt
# FILE INSIDE C:\delicious\cats: zophie.jpg
# The current folder is C:\delicious\walnut
# SUBFOLDER OF C:\delicious\walnut: waffles
# The current folder is C:\delicious\walnut\waffles
# FILE INSIDE C:\delicious\walnut\waffles: butter.txt.
```

## Compressing Files with the zipfile Module

### Reading ZIP Files

```python
>>> import zipfile, os
>>> os.chdir('C:\\') # move to the folder with example.zip
>>> exampleZip = zipfile.ZipFile('example.zip')
>>> exampleZip.namelist()
['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
>>> spamInfo = exampleZip.getinfo('spam.txt')
>>> spamInfo.file_size
13908
>>> spamInfo.compress_size
3828
>>> 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
.compress_size, 2))
'Compressed file is 3.63x smaller!'
>>> exampleZip.close()
```

### Extracting from ZIP Files

```python
>>> import zipfile, os
>>> os.chdir('C:\\') # move to the folder with example.zip
>>> exampleZip = zipfile.ZipFile('example.zip')
>>> exampleZip.extractall()
>>> exampleZip.close()

>>> exampleZip.extract('spam.txt')
'C:\\spam.txt'
>>> exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
'C:\\some\\new\\folders\\spam.txt'
>>> exampleZip.close()
```

### Creating and Adding to ZIP Files

```python
>>> import zipfile
>>> newZip = zipfile.ZipFile('new.zip', 'w')
>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
>>> newZip.close()
```

