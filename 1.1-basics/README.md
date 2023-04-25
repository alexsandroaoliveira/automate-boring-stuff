# Python Basics

## Expressions
Expressions consist of `values` and `operators` and they can `evaluate` (reduce)

## Operator List:
| Operator | Operation | Example | Evaluates to... |
|---|---|---|---|
| ** | Exponent | `2 ** 3` | `8` |
| % | Modulus/remainder | `22 % 8` | `6` | 
| // | Integer division/floored quotient | `22 // 8`, `2` |
| / | Division | `22/8` | `2.75` |
| * | Multiplication | `3 * 5` | `15` |
| * | Multiplication | `'Alice' * 5` | `'AliceAliceAliceAliceAlice'` |
| - | Subtration | `5 - 2` | `3` |
| + | Addition | `2 + 2` | `4` |

## Variables

Variable names are case-sensitive
hyphens (-) are not allowed
PEP 8 - Official Python code style

## Questions

1. Which of the following are operators, and which are values? 
- [x] `*`
- [ ] `'hello'`
- [ ] `-88.8`
- [x] `-`
- [x] `/`
- [x] `+`
- [ ] `5`

2. Which of the following is a variable, and which is a string?
- `spam`: _Variable_
- `'spam'`: _String_

3. Name three data types
- String
- Float
- Int

4. What is an expression made up of? What do all expressions do?
- _Expressions consist of `values` and `operators` and they can `evaluate` (reduce)_

5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?
- _An expression reduce to a single value_ 
- _An assignment statement assign a value to a variable_

6. What does the variable bacon contain after the following code runs?
```python
bacon = 20
bacon + 1
```
- bacon == `21`

7. What should the following two expressions evaluate to?
```python
'spam' + 'spamspam' 
'spam' * 3
```
- `'spamspamspam'`

8. Why is eggs a valid variable name while 100 is invalid?
- It can't begin with a number

9. What three functions can be used to get the integer, floating-point number, or string version of a value?
- `int()`
- `float()`
- `str()`

10. Why does this expression cause an error? How can you fix it?
```python
'I have eaten ' + 99 + ' burritos.'
```
- Because the add operator don't work with string + number. To fix:
`'I have eaten ' + str(99) + ' burritos.'`
