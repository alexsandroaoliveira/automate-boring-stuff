# Practice Questions

1. What is []?
_An empty list_

2. How would you assign the value 'hello' as the third value in a list stored 
in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
_spam[2]_

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

3. What does spam[int('3' * 2) / 11] evaluate to?
_list indices must be integers or slices, not float_

4. What does spam[-1] evaluate to?
_d_

5. What does spam[:2] evaluate to?
_['a', 'b']_

For the following three questions, let’s say bacon contains the list 
[3.14, 'cat', 11, 'cat', True].
6. What does bacon.index('cat') evaluate to?
_1_

7. What does bacon.append(99) make the list value in bacon look like?
_[3.14, 'cat', 11, 'cat', True, 99]_

8. What does bacon.remove('cat') make the list value in bacon look like?
_[3.14, 'cat', 11, True]_

9. What are the operators for list concatenation and list replication?
_+ for concatenation and * for replication_ 

10. What is the difference between the append() and insert() list methods?
_append adds to the end, insert to an especific index_

11. What are two ways to remove values from a list?
_del operator or remove method_

12. Name a few ways that list values are similar to string values.
_both are list but string is immutable_

13. What is the difference between lists and tuples?
_tuples are immutable_

14. How do you type the tuple value that has just the integer value 42 in it?
_(42,)_

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
- _list((1, 2))_
- _tuple([', 2])_

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
_Reference_

17. What is the difference between copy.copy() and copy.deepcopy()?
_copy() copies the list references into a new list_
_deepcopy() copies the list values into a new list_ 
