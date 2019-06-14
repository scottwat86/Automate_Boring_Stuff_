#               Automate the Boring Stuff with Python 3
#               Ch 5 -  Dictionaries and Structuring Data
#               Are a flexible way to access and organize data
#               Collection of many values; but unlike lists
#               can uses many data types than just int for indexing
#               Dictionaries are constructed of key-value pairs

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud',}
myCat['size'] # 'fat'
'My cat has ' + myCat['color'] + ' fur.' # 'My cat has gray fur.'

spam = {12345: 'Luggage Combination', 42: 'The Answer'}

#               DICTIONARIES VS LISTS
# Dict are unordered  and lists are ordered -> there is not first in dict

# In lists order of sequence matters
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon # False

# In dict order of sequence DO NOT matter
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham # True

# As a result of being unorder dict CANNOT BE SLICED

# # Accessing keys that do not exist throws KeyError
# spam = {'name': 'Zophie', 'age': 7}
# spam['color']

# birthdays.py
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True: # Infinite loop
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break # breaks out of infinite loop

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthdays?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated!')


#                   KEYS()      VALUES()       ITEMS()    METODS
# Values returned by these methods are NOT mutable / true lists
# DATA TYPES   dict_keys, dict_values,  dict_items
spam = {'color': 'red', 'age': 42}

for v in spam.values():
    print(v, end =", ") # red, 42,

for k in spam.keys():
    print(k, end=', ') #color, age,

for i in spam.items():
    print(i, end=', ') # ('color', 'red'), ('age', 42), -> these are tuples of (key, value)

# Converting to list
spam = {'color': 'red', 'age': 42}
spam.keys()
list(spam.keys()) # ['color', 'age'] -> This is a list!

spam = {'color': 'red', 'age': 42}
for k, v, in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
# Key: color Value: red
# Key: age Value: 42

#               CHECKING IF KEYS / VALUES EXISTS
spam = {'name': 'Zophie', 'age': 7}

'name' in spam.keys() # True
'Zophie' in spam.values() # True
'color' in spam.keys() # False
'color' not in spam.keys() # True
'color' in spam # False -> shorter version of  spam.keys()

#               GET()
# get(lookup_key, default_value)
picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0 )) + ' eggs.' #'I am bringing 2 eggs.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.' #'I am bringing 0 eggs.'

# KeyError b/c eggs isn't a valid key
# picnicItems = {'apples': 5, 'cups': 2}
# 'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'

#                SETDEFAULT()
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

# Same as above
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')

spam.setdefault('color', 'white') # black -> default only applicable if no value assigned
spam #{'age': 5, 'color': 'black', 'name': 'Pooka'}

# characterCount.py
message = 'It was a bright cold day in April, and the colocks were striking thirteen'
count = {}

for character in message:
    count.setdefault(character, 0)
    # Above setdefault ensures key is in dict and value=0 before the below
    count[character] = count[character] + 1

print(count)
#{'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2, 'h': 3, 'c': 3, 'o': 3, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2}

#               PRETTY PRINTING
# prettyCharacterCount.py

import pprint
massage = ' It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] +1

pprint.pprint(count)
# This time the output looks much cleaner with keys sorted

# The next two statement are the equal
pprint.pprint(count)
print(pprint.pformat(count))

#               DATA STRUCTURES TO MODEL THE REAL WORLD

#  ticTacToe.py
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                    'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)
'''
 | |
-+-+-
 | |
-+-+-
 | |
'''

theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)

#                NESTED DICTIONARIES   AND
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                     'Bob':   {'ham sandwiches': 3, 'apple': 2},
                     'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apple                 ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups                   ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes                 ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwich   ' + str(totalBrought(allGuests, 'ham sanwiches')))
print(' - Apple Pies          ' + str(totalBrought(allGuests, 'apple pies')))
'''
Number of things being brought:
 - Apple                 5
 - Cups                   3
 - Cakes                 0
 - Ham Sandwich   0
 - Apple Pies          1
'''

#               QUESTIONS
#         1) {}
#         2) {'foo': 42}
#         3) dict are unordered have arbitrary keys while lists are ordered and have indexing instead of keys
#         4) KeyError is returned b/c 'foo' isn't a valid key
#         5) nothing they are equal
#         6)
#               'cat' in spam checks if 'cat' is in the dict key
#               'cat' in spam.values() checks if 'cat' is a value of dict
#         7)
spam.setdefault('color', 'black')

#         8) pprint
