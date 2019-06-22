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
#            | or pipe in REGEX is ~ to OR
#            Matching | use \|
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()
mo2 = heroRegex.search('Tina Fey  and Batman')
mo2.group() # 'Tina Fey'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel.')
mo.group() #'Batmobile'
mo.group(1) #'mobile'

#            OPTIONAL MATCHING WITH THE QUESTION MARK
#             ?         character flags the group that precedes it as an optional part of the pattern
#              (wo)? is optional
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group() #'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group() #'Batwoman'  # (wo) is Optional

#                   MATCHING ZERO  OR MORE WITH THE STAR
#                   *  means match zero or more the group that precedes it
#                   \* for a literal *
batRegex =  re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()  #'Batman'   Zero instances of   (wo)

mo2 = batRegex .search('The Adventures of Batwoman')
mo2.group() # 'Batwoman'   One instance of (wo)

mo3 = batRegex.search('The Adventures of Batwowowoman')
mo3.group() #'Batwowowoman'   Multiple instances of  (wo)

#               MATCHING ONE OR MORE WITH THE PLUS
#               + matches one or more
#               MATCH MUST APPEAR ONCE. Its not optional

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group() #'Batwoman'

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group() #'Batwowowowoman'

mo3 = batRegex.search('The Adventures of Batman')
# mo3.group()    Returns an error b/c its a None Type
mo3 == None   #True

#                   MATCHING SPECIFIC REPETITIONS WITH CURLY BRACKETS
#                   (GROUP){n}  matches n repetitions of group, will not match if not n number of repeats
#                   (GROUP)(n,m)  matchs between   n     repetitions and    m      repetitions
#                   (Ha){3}   = HaHaHa
#                   (Ha){3,5}  = HaHaHa    or HaHaHaHa   or   HaHaHaHaHa
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group() #'HaHaHa'

mo2 = haRegex.search('Ha')
mo2 == None #False

haRegex = re.compile(r'(Ha){2,4}')
mo1 = haRegex.search('HaHaHa')
mo1.group() #'HaHaHa'

mo2 = haRegex.search('HaHaHaHa')
mo2.group() #'HaHaHaHa'


#                  GREEDY AND NONGREEDY MATCHING
#                   Regex are greedy by default meaning the longest possible match
#                   Nongreedy version which matches the shortest possible match     (){}?
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = nongreedyHaRegex.search('HaHaHaHaHa')
mo1.group()  #'HaHaHa'

#               FINDALL() METHOD
#               finds all the instances of the match
#               returns a list of strings as long there are NO GROUPS
#               returns a list of tuples if HAS GROUPS
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo =  phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # Note there are NO GROUPS ()
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# No group needed
# ['415-555-9999', '212-555-0000']

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #Has Groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# [('415', '555', '9999'), ('212', '555', '0000')]

#               CHARACTER CLASSES
#               SHORTHAND CODES FOR COMMON CHARACTER CLASSES

#               \d      Any numeric digit from 0-9
#               \D     Any character that is not a numeric digit from 0 - 9
#               \w     Any letter, numeric digit or the underscore char  THINK WORDS
#               \W    Any char that is not a letter nmeric digit or the underscore
#               \s      Any space, tab, or newline char  THINK SPACES
#               \S      Any char that is not a space tabe or newline

xmasRegex = re.compile(r'\d+\s\w+')  # \d+ one or more digits   \s one space   \w+ one or many words
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swan, 6 geese, 5 rings, 4 birds, 3 hens, 2 drove, 1 partridge')
'''
['12 drummers',
 '11 pipers',
 '10 lords',
 '9 ladies',
 '8 maids',
 '7 swan',
 '6 geese',
 '5 rings',
 '4 birds',
 '3 hens',
 '2 drove',
 '1 partridge']
'''

#                   MAKING YOUR OWN CHAR CLASSES
#                   [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers
#                   [a-z] The - is not literal but a range of char
#                   [.*?()+] no escaped needed for square brackets
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
#['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

#           [^] negative char class excludes matchs with the [chars]
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('Robocop eats baby food. BABY FOOD') # Returns only constanants
'''
['R',
 'b',
 'c',
 'p',
 ' ',
 't',
 's',
 ' ',
 'b',
 'b',
 'y',
 ' ',
 'f',
 'd',
 '.',
 ' ',
 'B',
 'B',
 'Y',
 ' ',
 'F',
 'D']
'''

#               CARET AND DOLLAR SIGN CHAR
beginsWithHello = re.compile(r'^Hello') #  Matches strings beginnning with Hello
beginsWithHello.search('Hello World!') # returns Hello
beginsWithHello.search('He said hello.')  == None # True

endsWithNumber = re.compile(r'\d$') # Matches the end with a 0-9 char
endsWithNumber.search('Your number is 42') # returns 2
endsWithNumber.search('Your number is forty two.') == None

wholeStringIsNum = re.compile(r'^\d+$') # Matches the beginning and end with numeric chars
wholeStringIsNum.search('1234567890') # Returns 1234567890
wholeStringIsNum.search('12345xyz67890') == None #True
wholeStringIsNum.search('12 34567890') == None #True

#               WILDCARD CHAR
#               . char is a wildcard that will match any char except for a newline
atRegex = re.compile(r'.at') # any char followed by 'at'
atRegex.findall('The cat in the hat say on the flat mat.') #['cat', 'hat', 'lat', 'mat']

#               MATCHING EVERYTHING WITH DOT-STAR
#               .* is a stand in for ANYTHING
#               .* uses greedy mode
#               like
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group() #'First Name: Al Last Name: Sweigart'

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner>')
mo.group() #'<To serve man>'

greedyRegex = re.compile(r'<.*>')
mo1 = greedyRegex.search('<To serve man> for dinner.>')
mo1.group() #'<To serve man> for dinner.>'


#                   MATCHING NEWLINES WITH THE DOT CHARACTER

noNewLineRegex = re.compile('.*')
noNewLineRegex.search('Serve the public trust.\nProtext the innocent.\nUphold the law.').group()
# 'Serve the public trust.'

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
#'Serve the public trust.\nProtect the innocent.\nUphold the law.'

#                  REVIEW OF REGEX SYMBOLS

#                  ?  matches zero or one of the preceding group
#                  *  matches zero or more ...
#                  +  match one or more ... THERE MUST BE ONE
#                  {n} matches exacyly n ...
#                  {n,}  matches n or more ...
#                  {,m}  matches 0 to m ...
#                  {n,m}  matches at least   n   and at more    m
#                  {n,m}?  OR *?  OR +?   performs NONGREEDY matches
#                  ^spam  means the string must begin with spam
#                  .  matches any character except a new line
#                  \d    \w  \s   matches    numeric digits   OR  words  OR spaces
#                  \D  \W  \S  matches anything but  numeric digits   OR  words  OR spaces
#                  [abc]  matches any char between the brackets such as a, b, or c
#                  [^abc]  matches any char that isn't between the brackets

#                   CASE-INSENSITIVE MATCHING
# The below matches different strings because they are case-sensitive
regex1 = re.compile('Robocop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('RobOcop')
regex4 = re.compile('RobocOp')

# re.IGNORECASE    OR   re.I
robocop = re.compile(r'robocop', re.I) # re.I makes it case insensitive
robocop.search('Robocop is part man, part machine, all cop.').group() #'Robocop'
robocop.search('ROBOCOP protexts the innocent.').group() #'ROBOCOP'

#           SUBSTITUTING STRINGS WITH THE SUB() METHOD
namesRegex = re.compile(r'Agent \w+') # Agent (word)
nameRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'Agent Alice gave the secret documents to Agent Bob.'

#
agentNamesRegex = re.compile(r'Agent (\w)\w*') # Agent  (First Letter)Remaining Letters  -> First Letter
agentNamesRegex.sub(r'\1***', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# 'A**** told C**** that E**** knew B**** was a double agent.'

agentNamesRegex = re.compile(r'Agent (\w)(\w)\w*') # Agent  (1st Letter)(2nd Letter)Remaining Letters  -> First Letter
agentNamesRegex.sub(r'\1\2*******', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
#'Al******* told Ca******* that Ev******* knew Bo******* was a double agent.'
# Note that *** are the literal substitution and \1 \2 \3 specify the number of char to show


#               MANAGING COMPLEX REGEXES
#               OVER MULTIPLE LINES

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                    # Area Code  555  OR  (555)   One or None
    (\s|-|\.)?                                    # Seperator  Space  OR  -  OR  .
    \d{3}                                       # First 3 digits   555
    (\s|-|\.)                                      # Seperators  ....
    \d{4}                                       # last 4 digist
    (\s*(ext|x|ext.)\s*\d{2,5})?     # Extensions    Space (0 to many) [ext OR x  OR ext.]Space (0 to many)  numerics 2-5
)''', re.VERBOSE)

phoneRegex.findall('555.555.5555 ext. 1234 Bob will call you later Phone: (206)-515-3854')

#               COMBINING RE.IGNORECASE     RE.DOTALL       AND     RE.VERBOSE
#               re.compiles only takes a single argument
#               you can get around this limitation by using | the bitwise operator

# Matching case-insensitive and including newlines in the match
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)

# ALL THREE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

|#              BOOK PROJECT
# See phoneAndEmail.py


#           IDEAS FOR SIMILAR PROGRAMS
#           Finding website URLS that begin with http://
#           Clean up dates in different date format by replacing them with dates in a single standard
#           Remove sensitve information such as Social Security or credit card numbers
#           Find common typos such as multiple spaces betweens words, accidentally repeated words or multiple excamations

#           SUMMARY
#           Regular Expression provide a precise method for searching for patterns in strings


#           PRACTICE PROBLEMS
#           1) Using re.compile() creates a Regex object that stores the pattern you are looking for
#           2) Raw strings are passed to re.compile() because Regex sometimes use \ to delineate patterns and raw strings take all characters literally
#           3) search() returns a match object.
#           4) To access the match you need to use a group() call on the object the is returned and saved to memory from the search() call
#           5) GRP0  (\d\d\d)   GRP1 -    GRP2  (\d\d\d-\d\d\d\d)
#           6) \(  \)  \.   ADD A BACKSLASH
#           7)  finall() returns list of strings for all matches as long as there aren't grouping with (), it returns tuples when there are groups
#           8)  | essentially matches this OR that
#           9)  ? matches OPTIONAL 0 or 1 occurances . ? can also change from greedy to nongreedy selections when multiple selections are possible
#           10)  + match one to many    *  matches zero to many
#           11)  {3} matches 3 instances of the preceding pattern    {3,5}  matches 3 to 5 instances ....
#           12) \d are for numerics   \words/chars      \s whitespace
#           13) \D matches anything but numerics   \W matches anything but words
#           14)  re.compile('/w/w/w/w', re.IGNORECASE )
#           15)  wildcard . matches anything char except newline.  re.DOTALL matches all chars inclu newlines
#           16) .* matches zero to many of any char but a newline.  .*? matches the same but is NONGREEDY meaning it takes the first instance not the last
#           17) [a-zA-Z0-9]
#           18) 'XX drummers, XX pipers, five rings, X hens'  RETURNED
#           19) re.VERBOSE allows for a multiline string to be inputed and then you can use # marks to comment out the multiple patterns for documentation
#           20)  42     ->   \d\d           1,234  ->   \d,\d\d\d       6,368,745 ->  \d,\d\d\d,\d\d\d  ^(\d\d,\d\d,\d\d\d) ^(\d\d\d\d)
#           21) [A-Z][a-z]*\sNakamoto
#           22) re.compile(r'(Alice|Bob|Carol|BOB)\s(eats|pets|throws|EATS)\s(apples|cats|baseballs|Apples|CATS)', re.IGNORECASE)
