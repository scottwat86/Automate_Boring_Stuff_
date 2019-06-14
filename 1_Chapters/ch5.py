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

# CHECKING IF KEYS / VALUES EXISTS
spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys() # True

'Zophie' in spam.values() # True
