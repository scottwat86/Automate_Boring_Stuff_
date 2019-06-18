#               Automate the Boring Stuff with Python 3
#               Ch 7 -  PATTERN MATCHING WITH REGULAR EXPRESSIONS
#               Regular Expressions allow you to specify a pattern of text to search for

#            Finding patterns of text w/o Regular Expressions
#    This function has several checks to determine if the string is a phone num
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))

print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

# isPhoneNumber.py
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

#           Finding Patterns of Text with Regular Expression
#           Regular Expressions = regexes
#           \d  -> Digit Character

# Creating Regex Objects

import re
# REGEX OBJECT -> compile was pass raw string r''
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # Creates a REGEX object

mo = phoneNumRegex.search('My number is 415-555-4242.') # search()   Returns a match
type(mo)  #_sre.SRE_Match
print('Phone number found: ' + mo.group())
# mo is just a generic variable name here

#               GROUPING W/ PARENTHESES
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My number is 415-555-4242.")
mo.group(1) #'415'
mo.group(2) # '555-4242'
mo.group(0) #'415-555-4242'

mo.groups() #('415', '555-4242') # Returns a tuples of multiple values
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# () Groups patterns but to use literal () you need \( \)
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)

#           MATCHING MULTIPLE GROUPS WITH THE PIPE
# | or pipe in REGEX is ~ to OR
# Matching | use \|
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()
mo2 = heroRegex.search('Tina Fey  and Batman')
mo2.group() # 'Tina Fey'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel.')
mo.group() #'Batmobile'
mo.group(1) #'mobile'

# Optional matching with the question mark
