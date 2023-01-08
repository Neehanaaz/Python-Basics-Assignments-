# -*- coding: utf-8 -*-
"""Python Basics Assignment - 5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eGmHNPxV6ByEyRYeJ2Vf7qJ2fABt6_Fr

1. What does an empty dictionary's code look like?

Ans: The empty dictionary's code looks like { }

2. What is the value of a dictionary value with the key 'foo' and the value 42?

Ans: dict={'foo': 42}

3. What is the most significant distinction between a dictionary and a list?

Ans: The dictionary is represented by { } which are unordered and list is represented by [ ] which is ordered.

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
"""

spam = {'bar': 100}
spam['foo']

"""We will get a key error.

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

Ans: There is no difference. The in operator checks whether the values exists as key in dictionary.

6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

Ans: The 'cat' in spam checks whether there is a cat key in the dictionary whereas the 'cat' in spam.values() checks whether there is a value of cat for one of the keys in spam.

7. What is a shortcut for the following code?

if 'color' not in spam:

spam['color'] = 'black'
"""

spam.setdefault('color','black')
spam

"""8. How do you "pretty print" dictionary values using which module and function?

Ans: By using pprint.pprint() 
"""