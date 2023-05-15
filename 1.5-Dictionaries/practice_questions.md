# Practice Questions

1. What does the code for an empty dictionary look like?
_emptyDict = {}_  

2. What does a dictionary value with a key 'foo' and a value 42 look like?
_dict = {'foo': 42}_

3. What is the main difference between a dictionary and a list?
_dictionary has keys_

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
_Key error_

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
_cat in spam has key-values. In span.keys() has only the key name_

6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
_cat in spam has key-values. In span.values() has only the values_

7. What is a shortcut for the following code?
```python
if 'color' not in spam:
    spam['color'] = 'black'
```
_spam.setdefault('color', 'black')_

8. What module and function can be used to “pretty print” dictionary values?
_pprint_
