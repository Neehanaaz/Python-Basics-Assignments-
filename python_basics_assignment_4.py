# -*- coding: utf-8 -*-
"""Python Basics Assignment - 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bv6VPuL0AIh14N29iVaRkOXQZ_HhMW-f

1. What exactly is [ ]?

Ans: This refers to the empty list as it does not contains any values. This is even similar to ' ' in a string.

2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
"""



spam=[2,4,8,10]
spam[2]='hello'
print(spam)

"""Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

3. What is the value of spam[int(int('3' * 2) / 11)]?
"""

spam=['a','b','c','d']
 spam[int(int('3' * 2) / 11)]

"""4. What is the value of spam[-1]?"""

spam=['a','b','c','d']
spam[-1]

"""5. What is the value of spam[:2]?"""

spam=['a','b','c','d']
spam[:2]

"""Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.

6. What is the value of bacon.index('cat')?
"""

bacon = [3.14,'cat',11,'cat',True]
bacon.index ('cat')

"""7. How does bacon.append(99) change the look of the list value in bacon?"""

bacon = [3.14,'cat',11,'cat',True]
bacon.append(99)
print(bacon)

"""8. How does bacon.remove('cat') change the look of the list in bacon?"""

bacon = [3.14,'cat',11,'cat',True]
bacon.remove('cat')
print(bacon)

"""9. What are the list concatenation and list replication operators?

Ans: The list concatenation operator is + and the list replication oprator is *.

10. What is difference between the list methods append() and insert()?

Ans: append() will add the value at the end of the list whereas insert() will add the value anywhere we want.
"""

#example for append
list=[1,2,3,4]
list.append(5)
list

#example for insert
list=[1,2,3,4]
list.insert(2,23)
list

"""11. What are the two methods for removing items from a list?

Ans: The two methods for removing items from a list are del() and remove().

12. Describe how list values and string values are identical.

Ans: Lists values and string values are identical as both can have indexes, slicing, knowing the length the string or list, both can be replicated and concatenated.

13. What's the difference between tuples and lists?

Ans: Lists are mutable - they can add,remove or change trhe values whereas the tuples are inmmutable they cannot be changed. Lists are represented in [ ]  and tuples are in ( )

14. How do you type a tuple value that only contains the integer 42?

Ans: (42)
"""

tuple=(42)

type(tuple)

"""15. How do you get a list value's tuple form? How do you get a tuple value's list form?

Ans: By using tuple() and list() functions.

16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?

Ans: They contain references to list values.

17. How do you distinguish between copy.copy() and copy.deepcopy()?

Ans: copy.copy() function will copy yje list. Whereas the copy.deepcopy() will do  a deep copy of a list.
"""