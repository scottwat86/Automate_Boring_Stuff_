#               Automate the Boring Stuff with Python 3
#               Lesson 15 - list functions



# RECAP
#  Methods are functions that are called on values
# index()         list method returns the index of an item in the List
# append()      list method adds a value to the end of a list
# insert()         list method adds a value anywhere inside a list
# remove()      list mtheod removes an item, specified by the value from a List
# sort()            list method sorts the items in a list
#                      reverse=True     keyword arg reverse order
#                       Sorting per ASCII betical order -> A Z a z
#                       key=str.lower       -> a A z Z
# These list methods operate on the list in place, rather than returning a new list value

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello') # 0
spam.index('heyas') # 3
spam.index("asfdasd")  # ValueError not in lists

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']

# Adds mouse to the end of list
spam.append('mouse')
spam # ['Zophie', 'Pooka', 'Fat-tail', 'Pooka', 'mouse']

# Inserts chicken to #1 Index
spam.insert(1, 'chicken')
spam #['Zophie', 'chicken', 'Pooka', 'Fat-tail', 'Pooka', 'mouse']

eggs = 'Hello'
eggs.append('world') # AttributeError -> append can't mod string

spam = ['cat', 'bat', 'rat', 'elephant']

# Removing first instance
spam.remove('bat')
spam #['cat', 'rat', 'elephant']

# Delete
del spam[0]
spam # ['rat', 'elephant']

spam = ['cat', 'bat', 'at', 'cat', 'bat']
spam.remove('cat') # removes the first instance of cat
spam #['bat', 'at', 'cat', 'bat']

spam.sort()
spam # ['at', 'bat', 'bat', 'cat']

spam = [2, 5, 3.14, 1, -2]
spam.sort()
spam # [-2, 1, 2, 3.14, 5]

spam.sort(reverse=True)
spam #[5, 3.14, 2, 1, -2]

spam = [1, 2, 3, 'the', 'at']
spam.sort() # TypeError b/c mixed types

spam = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']
spam.sort()
spam # ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
spam =  ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam #['a', 'A', 'z', 'Z']
