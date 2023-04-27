# Functions

## The None Value
In Python there is a value called None, which represents the absence of a value. None is the only value of the NoneType data type.

## Local and Global Scope
- Local scope: Parameters and variables that are assigned in a called function
- Global scop: Variables that are assigned outside all functions.
- Only one Global scope
- Local Variables Cannot Be Used in the Global Scope
- Local Scopes Cannot Use Variables in Other Local Scopes
- Global Variables Can Be used from a Local Scope
- Local and Global Variables Can have the Same Name (bad pratice)

## The global Statement
If you need to modify a global variable from within a function, use the global statement

## Exception Handling
Errors can be handled with try and except statements. The code that could potentially have an error is put in a try clause. The program execution moves to the start of a following except clause if an error happens

## Practice Questions
1. **Why are functions advantageous to have in your programs?**
_They are reusable / organize the code_

2. **When does the code in a function execute: when the function is defined or when the function is called?**
_When defined the function gets available to use_
_When is caled, the code inside the funciont is executed_

3. **What statement creates a function?**
`def`

4. **What is the difference between a function and a function call?**
Function is a definition. Function call is a function execution

5. **How many global scopes are there in a Python program? How many local scopes?**
1 Global
N Locals

6. **What happens to variables in a local scope when the function call returns?**
Are destroyed

7. **What is a return value? Can a return value be part of an expression?**
Is the value returned by a function after its execution.
Yes

8. **If a function does not have a return statement, what is the return value of a call to that function?**
`None`

9. **How can you force a variable in a function to refer to the global variable?**
`global` statement
 
10. **What is the data type of None?**
`NoneType`

11. **What does the import areallyourpetsnamederic statement do?**
Import the module `areallyourpetsnamederic`

12. **If you had a function named bacon() in a module named spam, how would you call it after importing spam?**
`bacon()`

13. **How can you prevent a program from crashing when it gets an error?**
use `try` `catch` statements

14. **What goes in the try clause? What goes in the except clause?**
In a try, nothing
In a catch, a variable to receive the exception data
