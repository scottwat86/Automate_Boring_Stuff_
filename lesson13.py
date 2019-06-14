#               Automate the Boring Stuff with Python 3
#               Lesson 13 - lists and slicing

# RECAP

#   List is a balue that contains multiple values
#   Values in a list are also called items
#   You can access items in a list with it's index
#   Indices start at 0   .... NOT 1
#   You can also use negative indices -> -1 is the last item
#   You can get multile items from the list using a slice

#   The slice has two indices. New list's items start at the first index
#   and go up tom but doesn't include, the second index

#   len() function concatenation and replication work the same way with
#  lists that they do with strings

#   you can convert a value into a list by passing into list()
#

spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] # bat
['cat', 'bat', 'rat', 'elephant'][1] # bat

print(f"The {spam[0]} in the {spam[2]}") #The cat in the rat

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]

spam[1][1] # 20
[['cat', 'bat'], [10, 20, 30, 40, 50]][1][1] # 20

spam[-1][-1]  # 50

spam[1][0:2] # [10, 20]

spam = "Hello"
spam * 2 # 'HelloHello'
spam[1] # e
spam[0:2] # He
spam[:2] # He
spam[1:] # ello
spam[-1] # o


spam = [1,2,3,4,5,6,7,8,9,10]
spam[1::2] #[2, 4, 6, 8, 10]

spam = [1,2,3,4,5,6]
spam[1:5] = 'Hello'
spam # [1, 'H', 'e', 'l', 'l', 'o', 6]
del spam[6] #[1, 'H', 'e', 'l', 'l', 'o']
len(spam)

int("42")
str(42)
spam = list("Hello")
spam #['H', 'e', 'l', 'l', 'o']

'howdy' in ['hello', 'hi', 'howdy', 'heyas'] # True
