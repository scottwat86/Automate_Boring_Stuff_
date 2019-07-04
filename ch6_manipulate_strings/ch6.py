#               Automate the Boring Stuff with Python 3
#               Ch 6 -  Manipulating Strings

#                LITERALS

# 'That is Alice's cat.'   Alice's is a problem b/c of the '
"That is Alice's cat."

#               ESCAPE CHARACTER   \
#               distinguishes text with special character as literal
spam = 'Say hi to Bob\'s mother.'

'\''            # Single quote
"\""         # Double quote
'\t'            # Tab
'\n'           # Newline (line break)
'\\'            # Backslash

#               RAW STRING
#               Ignore all escape char and print litrally  \
#               Handy when the text has a lot of \
print(r"That is Carol\'s cat.s")     #That is Carol\'s cat.s

#               MULTILINE STRING
# Note that no escape is needed
# catnapping.py
print(''' Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
'''
#           MULTILINE COMMENTS
""" This is a test python program.
Written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""

def spam():
    """ This is a multiline comment to help
    explain what the spam() function does."""
    print("Hello!")

#               INDEXING  &  SLICING
   'H e  l  l  o  W o r  l  d   !'
# 0  1 2 3 4 5 6 7 8 9 10 11
spam = 'Hello world!'
spam[0] # H
spam[4] # o
spam[-1] # !
spam[0:5] #'Hello' # 5 is none inclusive
spam[6:] #'world!'

#               IN / OUT OPERATORS
'Hello' in 'Hello World' # True
'HELLO' in 'Hello' # False
'' in "spam" # True
'cats' not in 'cats and dogs' # False

#               UPPER()         LOWER()
# These methods do not change the original string but make new strings
# Return a string
spam = 'Hello World'
spam = spam.upper() #'HELLO WORLD'
spam = spam.lower() #'hello world'

print('How are you?')
feeling = input()
if feeling.lower() == 'great': # Ensures the input is all lower case
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

#               ISUPPER()      ISLOWER()
# Returns TRUE iff ALL letters are upper / lower case
spam = 'Hello World!'
spam.islower() #False
spam.isupper() # False
'HELLO'.isupper() #TRUE
'abc1234'.islower() # True
'12345'.islower() #False

#               IS X Method
'abc'.isalpha()         # Returns True if a string consists of only letters and IS NOT BLANK
'abc124'.isalnum()        # If string consists of only letters and numbers and IS NOT BLANK
'1234'.isdecimal()     # if the string consists of only numeric char and IS NOT BLANK
' \n\t'.isspace()         # if string is only spaces / tabs / newlines and IS NOT BLANK
'The End'.istitle()            # if the string is only of words that begin with an uppercase letter followed by lowercase

#       validateInput.py
while True: # Infinite Loop
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

#           STARTSWITH      ENDSWTH()
# Returns true if the string begins or ends with the string passed
'Hello World'.startswith('Hello') #True
'Hello World'.endswith('World') # True
'abc123'.startswith('abcdef') # False
'abc123'.endswith('12') # Flase


#           JOIN()      SPLIT()
# Called on a string
# Passed a list of strings as input
# Returns String
'-'.join(['cats', 'rats', 'bats']) # 'cats-rats-bats'
' '.join(['My', 'name', 'is', 'Simon']) #'My name is Simon'

# Default to split by ' ' \t or \n   white space which is stripped out
# Returns LIST
'My name is Simon'.split() #['My', 'name', 'is', 'Simon']

# Passing split a string will change what is stripped out
'MyABCnameABCisABCSimon'.split('ABC') #['My', 'name', 'is', 'Simon']

spam = '''Dear Alice,
How have you been? I am fine.
There us a container in the frige
that is labeled "Milk Experiment"

Please do not drink it.
Sincerely,
Bob'''
spam.split('\n')

#               RJUST()         LJUST()    CENTER()
# Return padded version of the string with spaces to justify text
# Optional 2nd argv which will specify a fill char other than ' '
# Usefull for tabular data
"Hello".rjust(10) #'     Hello'
'Hello'.rjust(20) #'               Hello'

'Hello World'.ljust(20, '*') #'Hello World*********'
'Hello'.ljust(20, '-') #'Hello---------------'

#                          CENTER()
'Hello'.center(20) #'       Hello        '
'Hello'.center(20, '=') #'=======Hello========'

# picnicTable.py
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth+rightWidth))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwich': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
#printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 5)
"""
       PICNIC ITEMS
sandwich............    4
apples..............   12
cups................    4
cookies............. 8000
"""

#               STRIP()         RSTRIP()            LSTRIP()
#   Removing whitespace from strings

spam = '    Hello World     '
spam.strip() # 'Hello World'
spam.lstrip() #'Hello World     '
spam.rstrip() #'    Hello World'

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS') #'BaconSpamEggs'
spam.strip('Spam') #'BaconSpamEggs'
spam.strip('SpamEggs') #'Bacon'
# strips occurences of a, m, p, and S from the ends of the string
# Stops once a differenct character is hit on either side

#               PYPERCLIP MODULE
#               COPY()          PASTE()
# For sending and receiving text from the computers clipboard

import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste() #'Hello world!'

#                   PROJECT PASSWORD LOCKER
# see 6_password_locker.py
# see 6_password_locker.py

#           QUESTIONS
#       1) \ char alters the way python interprets special string modifiers withi ""
#       2)  \n makes a new line  and \ makes a tab within the string
#       3) \\ is how a backslash is entered into a ""
#       4) ' ' quotes will confuse python as it can't distinguish between the literal ' and the programming '
#       5)
"""
by using multiline string
"""
#       6)
'e'
'Hell'
'Hell'
'lo world!'
#       7)
'HELLO'
True
'hello'
#       8)
['Remember,', 'remember,', 'the', ' fifth', 'of', 'November.']
#       9)
"|".rjust(20)
"|".ljust(20)
"|".center(20)
#       10)
'.......The, whitespace.......'.strip(".")
'.......The, whitespace.......'.lstrip(".")
'.......The, whitespace.......'.rstrip(".")
