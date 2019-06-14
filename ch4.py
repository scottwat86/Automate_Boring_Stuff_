#               Automate the Boring Stuff with Python 3
#               Ch 4 - Lists & Tuples
#               Lists can be used to arrange data into hierarchical structures
#               Contains multiple values in an ORDERED SEQUENCE

#
# [1, 2, 3]
# ['cat', 'bat', 'rat', 'elephant']
# ['hello', 3.1415, True, None, 42]
#
# #           ACCESSING INDICES
# spam = ['cat', 'bat', 'rat', 'elephant']
# #Index      0      1      2         3
# spam
# spam[0]  # 'cat'
#  ['cat', 'bat', 'rat', 'elephant'][3] #'elephant'
# 'Hello ' + spam[0] #'Hello cat'
# 'The ' + spam[1] + ' ate the ' + spam[0] #'The bat ate the cat'
#
# # IndexError will throw if you call an index beyond the range
# # spam[1000]
#
# # Indices can only be INTEGERS not floats
# spam[int(1.0)]
#
# spam = [['cat', 'bat'],[10, 20, 30, 40, 50]]
# #                0     1        0   1    2     3    4
# #                    0                       1
# sapm[0] # ['cat', 'bat']
# spam[0][1] # bat
# spam[1][4] # 50
#
# #           NEGATIVE INDICING
# spam[0][-1] # bat
# spam[1][-2] # 40
#
# #           SUBLIST & SLICER
# # spam[start:end:step]
# spam = ['cat', 'bat', 'rat', 'elephant']
# #               0       1    2          3
# spam[1:3] # ['bat', 'rat']
# #   Note 3 is NOT INCLUSIVE
# spam[::2]  # ['cat', 'rat']
# # Slices 2 by 2 starting at 0
# spam[:2] # ['cat', 'bat']
# spam[:] # ['cat', 'bat', 'rat', 'elephant']
#
# #           LENGTH
# spam = ['cat', 'dog', 'moose']
# len(spam) # 3
#
# #               CHANGING VALUES
# spam = ['cat', 'bat', 'rat', 'elephant']
# spam[1] = 'aardvark'
# spam[2] = spam[1]
# spam[-1] = 12345 # Last entry
# spam # ['cat', 'aardvark', 'aardvark', 12345]
# #               0         1                2               3
#
# #               CONCATENATION
# [1, 2, 3] + ['A', 'B', 'C'] #[1, 2, 3, 'A', 'B', 'C']
# ['X', 'Y'] *3 #['X', 'Y', 'X', 'Y', 'X', 'Y']
#
# spam += ['A']
# spam  #['cat', 'aardvark', 'aardvark', 12345, 'A']
#
#
# #               REMOVING VALUES -> DEL
# #   del is mostly used to delete elements from lists
# spam = [1, 2, 3, 4]
# del spam[2:4]
# spam # [1, 2]
# del spam[0] # [2]
#
# del spam # deletes variable name from memory
# # If you use spam you will now get a NameError
#
# #               IMPLEMENTING LISTS
# catName1 = 'Zophie'
# catName2 = 'Pooka'
# catName3 = 'Simon'
# # The above is dumb programming as it lead to duplicate code later
#
# print('Enter the name of cat 1:')
# canName1 = input()
# print('Enter the name of cat 2:')
# catName2 = input()
# # ...
#
# # Instead we should implement a list
# catNames = [] # creates an empty list
# while True: # creates an infinite loop
#     print('Enter the name of cat ' + str(len(catNames)+1) + '\n(Or enter nothing to stop.):')
#     name = input()
#     if name  == '':
#         break # breaks out of loop based on user input ''
#     catNames +=  [name] # list concatenation
#     # If you don't [] name it will take each char and added it seperately to the list
# print('The cat names are')
# for name in catNames:
#     print('  ' + name)
#
# # Data above is structured and more flexible to deal with
#
# #               LOOPS WITH LISTS
# # in this book list-like objects are really sequences
# spam = [2, 'hill', 3, 'billy']
# for i in spam:  # iterates through each element of the list.
#     print(i)
#     #    2   hill     3    billy
#
# spam = [2, 'hill', 3, 'billy']
# for i in range(len(spam)):  # Iterates through each index with in the list
#     print(i)
#     # 0   1   2   3
#
# supplies = ['pens', 'staplers', 'flame-throwers', 'binder']
# for i in range(len(supplies)):
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
# '''
# Index 0 in supplies is: pens
# Index 1 in supplies is: staplers-
# Index 3 in supplies is: binder
# '''
#
# #               IN / NOT IN     OPERATORS
# # are expression that connect two values together
#
# 'howdy' in ['hello', 'hi', 'howdy', 'heyas'] #True
# 'hello' in spam # False
# 'howdy' not in spam # True

# myPets.py
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

#           MULTIPLE ASSIGNMENT TRICK
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
disposition  # loud

'''
if the number of variables do not match the number of
elements to unpack, a ValueError is thrown
'''

a, b, = 'Alice', 'Bob'
a, b = b, a
a # Bob

#           AUGMENTED ASSIGNMENT OPERATORS
# This is faster to run then spam = spam + 1
spam = 42
spam += 1 # 43
spam -= 1 # 42
spam /= 7 # 6.0 # Converted to float b/c of division
spam *= 2 # 12.0

spam = 'Hello'
spam += ' World' # Hello World
bacon = ['Zophie']
bacon *= 3
bacon # ['Zophie', 'Zophie', 'Zophie']


#               METHODS
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello') # 0
spam.index('heyas') # 3

# If the value doesn't match literally then it throws a ValueError
# In this case there are no instances of howdy 3 times
# spam.index('howdy howdy howdy')

# index() returns first occurance of value
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
#                0               1           2              3
spam.index('Pooka') # 1

#           INSERT()    /    APPEND()
spam = ['cat', 'dog', 'bat']
spam.append('moose')  # addes moose to the end of list
spam.insert(1, 'chicken') # inserts chicken into index 1
spam # ['cat', 'chicken', 'dog', 'bat', 'moose']

# append()  and  insert()   return None. They modify the list instear
# Methods belong to a single data type.
# e.g. append() / insert() can only be used on list data types
# IF you use the wrong data type with a method it throws an AttrubuteError

#             REMOVE()
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
spam # ['cat', 'rat', 'elephant']

# removing values that do not exist result in a ValueError

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
spam # ['bat', 'rat', 'cat', 'hat', 'cat']

#           SORT()
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam #[-7, 1, 2, 3.14, 5]

spam = ['ants', 'cats', 'dogs', 'badgers', 'elepants']
spam.sort() # A->Z Sorting
spam  # ['ants', 'badgers', 'cats', 'dogs', 'elepants']
spam.sort(reverse=True) # Z -> A Sorting
spam  #['elepants', 'dogs', 'cats', 'badgers', 'ants']

# spam = [1, 3, 2, 4, 'Alice', 'Bob']
# spam.sort() # TypeError b/c mixed string and int

# Sort() uses ASCIIbetical ordering  A - Z  then a - z
spam = ['a', 'z', 'A', 'Z']
spam.sort()
spam # ['A', 'Z', 'a', 'z']
spam.sort(key=str.lower)
spam # ['A', 'a', 'Z', 'z']


#               magix8Ball2.py
import random

messages = [
'It is certain',
'It is decidedly so',
'Yes definitely',
'Reply haze try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']

print(messages[random.randint(0, len(messages)-1)])

#  TAB EXCEPTION
spam = ['apples',
        'oranges',
                                    'bananas'
    'cats']
spam    #['A', 'a', 'Z', 'z']

# alteratively
print('Four score and seven ' + \   # '\' line continuation
            'years ago...') #Four score and seven years ago...

# LIST LIKE -> STRINGS & TUPLES
name = 'Zophie'
name[0] # Z
name[-2] # i
name[0:4] #'Zoph'

'Zo' in name # True
'z' in name # False  -> Cases sensitve

for i in name:
    print('* * * ' + i + ' * * *')
'''
* * * Z * * *
* * * o * * *
* * * p * * *
* * * h * * *
* * * i * * *
* * * e * * *
'''

#               MUTABLE & IMMUTABLE
# TypeError thrown b/c strings are immutable
# name = 'Zophie a cat'
# name[7] = 'the'

name = 'Zophie a cat'
#           Z o p h  i  e     a     c   a  t
#           0 1 2 3 4  5 X 7 X  9 10 11
# The below doesn't throw an error b/c a new string is created
newName = name[0:7] + 'the' + name[8:12]
newName # 'Zophie the cat'

# Lists are mutable but the below creates a new list that replaces the old lis
# in the container (variable)
eggs = [1, 2, 3]
eggs = [4, 5, 6]
eggs #[4, 5, 6]

# Changing the old list
eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]
eggs # []
eggs.append(4)
eggs.append(5)
eggs.append(6)
eggs # [4, 5, 6]

#               TUPLES
# Tuples are immutable
eggs = ('hello', 42, 0.5)
eggs[0] # hello
eggs[1:3] #(42, 0.5)
len(eggs) #3

# TypeError b/c tuples are immitable
# eggs = [1] = 99

type(('hello' ,)) # tuple
type(('hello')) # String

#                   LIST()   &    TUPLE()
tuple(['cat', 'dog', 5])
list(('cat', 'dog', 5))
list('hello') #['h', 'e', 'l', 'l', 'o']

#               REFERENCES
'''
Immutables such as strings, integers, and tuples, variables store the value.
For mutables such as lists and dictionaries they store the reference.
'''
spam = 42
cheese = spam
spam = 100
spam
cheese

#                   SHALLOW COPY
spam = [0, 1, 2, 3, 4, 5]
cheese = spam  # This is a shallow copy that is faster than copy()
cheese [1] = 'Hello'
# the value in spam as well b/c both point to the same memory location
spam # [0, 'Hello', 2, 3, 4, 5]
cheese # [0, 'Hello', 2, 3, 4, 5]
id(spam)    #3023613934408    Memory location equal
id(cheese) #3023613934408
# cheese = list(spam) # This is also a shallow copy
# cheese = copy(spam) # This is also a shallow copy

#                   PASSING REFERENCES
# Passing a list to a function copies it to a parameter
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam) #[1, 2, 3, 'Hello']
# The function changed the global variable value b/c the variable only is a ref and
# the shallow copy ref pointed to the same value in the memory when the parameter was created

#                   DEEP COPY
spam = [0, 1, 2, 3, 4, 5]
import copy
cheese = copy.deepcopy(spam) # This is faster than the item by item method
spam # [0, 'Hello', 2, 3, 4, 5]
cheese # [0, 'Hello', 2, 3, 4, 5]
id(spam)    #3023613934408
id(cheese) #3023615261256

# This is another way to deep copy
cheese=[]
for i in spam:
    cheese.append(i)
id(spam)    #3023615793032
id(cheese) #3023615793096

#                   SUMMARY
# lists are structured sequence and mutable (can be changed)
# variables that containt a list hold a ref not a Value
# Be mindful of copying lists and use deepcopy() where appropriate


#               QUESTIONS
#       1) [] defines a list in python
#       2) see below code

spam = [2, 4, 6, 8, 10]
spam.insert(2, 'hello')
spam #[2, 4, 'hello', 6, 8, 10]

spam = ['a', 'b', 'c', 'd',]
#       3) int('3'*2)-> 33  // 11 -> spam[3]
#           Ans = 'd'
spam[int(int('3' * 2) // 11)]

#       4) spam[-1] -> 'd'
#       5) spam[:2] -> ['a', 'b']

bacon = [3.14, 'cat', 11, 'cat', True]
#       6) bacon[1]
bacon.index('cat')
#       7) [3.14, 'cat', 11, 'cat', True, 99]
bacon.append(99)
#       8) [3.14, 11, 'cat', True, 99]
bacon.remove('cat')
#       9)
spam * 2 # replication
spam += ["Blah"]  # concatenation
# be careful to incl brackets otherwise each element of the string is used seperately

#       10) append() adds elements to the end of the list, insert adds item to a specific Index

#       11)  pop()  removes last item from list
#               remove() removes first instance of element from lists
#               del spam[1] # removes item from list
#       12) List and strings are iterable, can use len(), are ordered sequences,
#       13) lists are mutable and use []
#               tuples are immutable  and use ()
#       14)(42,)
type( (42,) )
#       15)
list((42,)) # [42]
tuple([42]) # (42,)
#       16) refereences to the values
#       17) copy() is a shallow copy that copies the reference
#              deepcopy() is a deep copy that copies the value not the reference
