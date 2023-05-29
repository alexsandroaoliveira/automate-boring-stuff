# Debugging

### Raising Exceptions

```python
>>> raise Exception('This is the error message.')
Traceback (most recent call last):
 File "<pyshell#191>", line 1, in <module>
 raise Exception('This is the error message.')
Exception: This is the error message.
```

```python
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
    raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))

# ****
# * *
# * *
# ****
# OOOOOOOOOOOOOOOOOOOO
# O O
# O O
# O O
# OOOOOOOOOOOOOOOOOOOO
# An exception happened: Width must be greater than 2.
# An exception happened: Symbol must be a single character string.
```

### Getting the Traceback as a String

```python
def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')
spam()

# Traceback (most recent call last):
#  File "errorExample.py", line 7, in <module>
#  spam()
#  File "errorExample.py", line 2, in spam
#  bacon()
#  File "errorExample.py", line 5, in bacon
#  raise Exception('This is the error message.')
# Exception: This is the error message.


>>> import traceback
>>> try:
 raise Exception('This is the error message.')
except:
 errorFile = open('errorInfo.txt', 'w')
 errorFile.write(traceback.format_exc())
 errorFile.close()
 print('The traceback info was written to errorInfo.txt.')

# Traceback (most recent call last):
#  File "<pyshell#28>", line 2, in <module>
# Exception: This is the error message 
```

### Assertions

```python
>>> podBayDoorStatus = 'open'
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
>>> podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can't do that.''
>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
Traceback (most recent call last):
 File "<pyshell#10>", line 1, in <module>
 assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
AssertionError: The pod bay doors need to be "open".
```

### Using an Assertion in a Traffic Light Simulation

```python
market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
 for key in stoplight.keys():
 if stoplight[key] == 'green':
 stoplight[key] = 'yellow'
 elif stoplight[key] == 'yellow':
 stoplight[key] = 'red'
 elif stoplight[key] == 'red':
 stoplight[key] = 'green'
switchLights(market_2nd)

assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

Traceback (most recent call last):
 File "carSim.py", line 14, in <module>
 switchLights(market_2nd)
 File "carSim.py", line 13, in switchLights
 assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
AssertionError: Neither light is red! {'ns': 'yellow', 'ew': 'green'}
```

### Disabling Assertions

Assertions can be disabled by passing the -O option when running Python. 

## Logging

### Using the logging Module

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s 
- %(message)s')

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s 
- %(message)s')
logging.debug('Start of program')
def factorial(n):
 logging.debug('Start of factorial(%s%%)' % (n))
 total = 1
 for i in range(n + 1):
 total *= i
 logging.debug('i is ' + str(i) + ', total is ' + str(total))
 logging.debug('End of factorial(%s%%)' % (n))
 return total
print(factorial(5))
logging.debug('End of program')

# 2015-05-23 16:20:12,664 - DEBUG - Start of program
# 2015-05-23 16:20:12,664 - DEBUG - Start of factorial(5)
# 2015-05-23 16:20:12,665 - DEBUG - i is 0, total is 0
# 2015-05-23 16:20:12,668 - DEBUG - i is 1, total is 0
# 2015-05-23 16:20:12,670 - DEBUG - i is 2, total is 0
# 2015-05-23 16:20:12,673 - DEBUG - i is 3, total is 0
# 2015-05-23 16:20:12,675 - DEBUG - i is 4, total is 0
# 2015-05-23 16:20:12,678 - DEBUG - i is 5, total is 0
# 2015-05-23 16:20:12,680 - DEBUG - End of factorial(5)
# 0
# 2015-05-23 16:20:12,684 - DEBUG - End of program
```

### Don’t Debug with print()

### Logging Levels

| Level | Logging Function | Description |
|---|---|---|
| DEBUG | logging.debug() | The lowest level. Used for small details. Usually you care about these messages  only when diagnosing problems. |
| INFO | logging.info() | Used to record information on general events in your program or confirm that things are working at their point in the program. |
| WARNING | logging.warning() | Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future. |
| ERROR | logging.error() | Used to record an error that caused the program to fail to do something. |
| CRITICAL | logging.critical() | The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely |

```python
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - 
%(levelname)s - %(message)s')
>>> logging.debug('Some debugging details.')
2015-05-18 19:04:26,901 - DEBUG - Some debugging details.
>>> logging.info('The logging module is working.')
2015-05-18 19:04:35,569 - INFO - The logging module is working.
>>> logging.warning('An error message is about to be logged.')
2015-05-18 19:04:56,843 - WARNING - An error message is about to be logged.
>>> logging.error('An error has occurred.')
2015-05-18 19:05:07,737 - ERROR - An error has occurred.
>>> logging.critical('The program is unable to recover!')
2015-05-18 19:05:45,794 - CRITICAL - The program is unable to recover!
```

### Disabling Loggin

```python
>>> import logging
>>> logging.basicConfig(level=logging.INFO, format=' %(asctime)s - 
%(levelname)s - %(message)s')
Debugging 225
>>> logging.critical('Critical error! Critical error!')
2015-05-22 11:10:48,054 - CRITICAL - Critical error! Critical error!
>>> logging.disable(logging.CRITICAL)
>>> logging.critical('Critical error! Critical error!')
>>> logging.error('Error! Error!')
```

### Logging to a File

```python
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' 
%(asctime)s - %(levelname)s - %(message)s')
```

## IDLE’s Debugger


