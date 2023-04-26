# Flow Control

## Boolean
True or False

## Comparison Operators
| Operator | Meaning |
| --- | --- |
| `==` | Equal to |
| `!=` | Not equal to |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |

## The not Operator
|Expression|Evaluates to…|
|---|---|
|`not True`|`False`|
|`not False`|`True`|

## Blocks of Code
1. Blocks begin when the indentation increases.
2. Blocks can contain other blocks.
3. Blocks end when the indentation decreases to zero or to a containing block’s indentation

## Flow Control Statements
- `if` Statements:
    - The if keyword
    - A condition (that is, an expression that evaluates to True or False)
    - A colon
    - Starting on the next line, an indented block of code (called the if clause)
- `else` Statements:
    - The else keyword
    - A colon
    - Starting on the next line, an indented block of code (called the else clause)
- `elif` Statements:
    - The elif keyword
    - A condition (that is, an expression that evaluates to True or False)
    - A colon
    - Starting on the next line, an indented block of code (called the elif clause)
- `while` Loop Statements:
    - The while keyword
    - A condition (that is, an expression that evaluates to True or False)
    - A colon
    - Starting on the next line, an indented block of code (called the while clause)
- `break` Statements:
    - If the execution reaches a break statement, it immediately exits the while loop’s clause
- `continue` Statements:
    - continue statements are used inside loops. When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop’s condition.
- `for` Loops and the `range()` Function
    - The for keyword
    - A variable name
    - The in keyword
    - A call to the range() method with up to three integers passed to it
    - A colon
    - Starting on the next line, an indented block of code (called the for clause)

## Importing Modules
    - The import keyword
    - The name of the module
    - Optionally, more module names, as long as they are separated by commas

## Ending a Program Early with sys.exit()

## Practice Questions
1. What are the two values of the Boolean data type? How do you write them?
- `True`
- `False`

2. What are the three Boolean operators?
- `and`
- `or`
- `not`

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
- `True and True == True`
- `True and False == False`
- `False and True == False`
- `False and False == False`

4. What do the following expressions evaluate to?
|Expression|Evaluate to...|
|---|---|
|`(5 > 4) and (3 == 5)`|`False`|
|`not (5 > 4) `|`False`|
|`(5 > 4) or (3 == 5)`|`True`|
|`not ((5 > 4) or (3 == 5))`|`False`|
|`(True and True) and (True == False)`|`False`|
|`(not False) or (not True)`|`True`|

5. What are the six comparison operators?
- `==`
- `!=`
- `<`
- `>`
- `<=`
- `>= `

6. What is the difference between the equal to operator and the assignment operator?
- Equal operator `==` Compare too values 
- Assignment operator `=` Atribute a value to a variable

7. Explain what a condition is and where you would use one.
_A condition is and Bolean expression that should be used to control the execution flow_

8. Identify the three blocks in this code:
```python
spam = 0                # block 1
if spam == 10:          # block 1
    print('eggs')       # block 2
    if spam > 5:        # block 2
        print('bacon')  # block 3
    else:               # block 2
        print('ham')    # block 4
    print('spam')       # block 2
print('spam')           # block 1
```

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
```python
spam = 0                
if spam == 1:          
    print('Hello')       
elif spam = 2:        
    print('Howdy')  
else:               
    print('Greetings!')    
```

10. What can you press if your program is stuck in an infinite loop?
`ctrl+c`

11. What is the difference between break and continue?
- `break` exists the loop
- `continue` jump to the next loop item

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
_None_

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
```python
# Using for
for i in range(1, 10):
    print(i)
```

```python
# Using while
i=1
while i <= 10:
    print(i)
    i += 1
```
14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
```bacon()```

15. Extra credit: Look up the round() and abs() functions on the Internet, and find out what they do. Experiment with them in the interactive shell.
- __abs(x)__
    Return the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing __abs__(). If the argument is a complex number, its magnitude is returned.
- __round(number, ndigits=None)__
    Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.
