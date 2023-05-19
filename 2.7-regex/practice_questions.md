# Practice Questions

1. What is the function that creates Regex objects?
_compile_

2. Why are raw strings often used when creating Regex objects?
_Because regex usually has a lot of chars thats would need to escape_

3. What does the search() method return?
_Find the first match on a string_

4. How do you get the actual strings that match the pattern from a Match object?
_group() method_ 

5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

- 0: (\d\d\d)-(\d\d\d-\d\d\d\d)
- 1: (\d\d\d)
- 2: (\d\d\d-\d\d\d\d)

6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?
using `'\('` and `'\.'`

7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?
_if the regex code has any group definition it will return a tuple. If not returns a simple string_

8. What does the | character signify in regular expressions?
_tha match can be anything before the pipe or after_

9. What two things does the ? character signify in regular expressions?
_char is present or not or not greedy search_

10. What is the difference between the + and * characters in regular expressions?
_+ just one char * one or multiple chars_

11. What is the difference between {3} and {3,5} in regular expressions?
_{3} length needs to be 3_
_{3,5} length needs to be between 3 and 5_

12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?
- \d - decimal char
- \w - alpha char
- \s - space or tab

13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?
- \D - not decimal char
- \W - not alpha char
- \S - not space or tab

14. How do you make a regular expression case-insensitive?
_re.IGNORECASE_

15. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?
_. will look at other lines too_

16. What is the difference between .* and .*?
_non greedy match_

17. What is the character class syntax to match all numbers and lowercase letters?
_[\da-z]_

18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?
_X drummers, X pipers, five rings, X hens_

19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?
_add comments and line breaks on the regex_

20. How would you write a regex that matches a number with commas for every three digits? It must match the following:
- '42'
- '1,234'
- '6,368,745'
but not the following:
- '12,34,567' (which has only two digits between the commas)
- '1234' (which lacks commas)

```python
re.compile(r'''^
    (
        (
            \d{1,3},
            (\d{3},)*
            \d{3}
        )
        |
        (\d{1,3})
    )
    $''', re.VERBOSE)
```


21. How would you write a regex that matches the full name of someone whose last name is Nakamoto? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
- 'Satoshi Nakamoto'
- 'Alice Nakamoto'
- 'RoboCop Nakamoto'
but not the following:
- 'satoshi Nakamoto' (where the first name is not capitalized)
- 'Mr. Nakamoto' (where the preceding word has a nonletter character)
- 'Nakamoto' (which has no first name)
- 'Satoshi nakamoto' (where Nakamoto is not capitalized)

```python
reg = re.compile(r'(Satoshi|Alice|RoboCop)\sNakamoto')
```

22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or 
throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the 
following:
- 'Alice eats apples.'
- 'Bob pets cats.'
- 'Carol throws baseballs.'
- 'Alice throws Apples.'
- 'BOB EATS CATS.'
but not the following:
- 'RoboCop eats apples.'
- 'ALICE THROWS FOOTBALLS.'
- 'Carol eats 7 cats.'

```python
re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|baseballs|cats)\.', re.IGNORECASE)
```