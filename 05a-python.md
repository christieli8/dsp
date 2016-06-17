# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both structures in Python. Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing. Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list. Tuples will work as keys in dictionaries because of their immutability. 

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are unordered collections of unqiue elements while lists are ordered collections of elements allowing duplicates. Sets allows you to do operations such as intersection, union, difference, and symmetric difference and sets are not indexed. List elements can be accessed by index while in order to find an element in a set, a hash lookup is used. This makes __contains__ (in operator) a lot more efficient for sets than lists.
Lists: 
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
Sets: 
from sets import Set
engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
programmers = Set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = Set(['Jane', 'Jack', 'Susan', 'Zack'])
employees = engineers | programmers | managers       
print employees 






---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called "lambda".Lambda forms can be used as the required function argument to other functions. 
```python 
student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.
The simplest form of a list comprehension is

[ expression-involving-loop-variable for loop-variable in sequence ]
This will step over every element of sequence, successively setting loop-variable equal to every element one at a time, and will then build up a list by evaluating expression-involving-loop-variable for each one. 

```python 
squares = [x**2 for x in range(10)]
squares = map(lambda x: x**2, range(10))
```
List comprehensions can be nested, in which case they take on the following form:

[ expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ]
results = []
for outer_loop_variable in outer_sequence:
    for inner_loop_variable in inner_sequence:
        results.append( expression_involving_loop_variables )
Filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence for which the function returned True.

```python 
squares = map(lambda x: x**2, range(10))
special_squares = filter(lambda x: x > 5 and x < 50, squares)
print special_squares
[9, 16, 25, 36, 49]
special_squares = [ x**2 for x in range(10) if x**2 > 5 and x**2 < 50 ]
```

set comprehension: 
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}

dictionary comprehension 
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





