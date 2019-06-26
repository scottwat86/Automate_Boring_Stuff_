#               Automate the Boring Stuff with Python 3
#               Ch 7 -  Practice Project - Regex Version of strip

#               By Scott Watson

'''
Write a function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip, then whitespace characters
will be removed from the beginning and end of the string. Otherwise, the characters
 specified in the second argument to the function will be removed from the string.
'''
import re

def newStrip(string, pattern=None):
    '''
    Return a copy of the string with the leading and trailing
    characters removed. The chars argument is a string specifying
    the set of characters to be removed. If omitted or None, the
    chars argument defaults to removing whitespace. The chars
    argument is not a prefix or suffix; rather, all combinations
    of its values are stripped:
    '''
    if pattern == None: # Removes whitespaces by default
        pattern = r'\s'
    else:
        pattern = r'['+pattern+r']' # adds brackets to pattern for Regex matching
    # sub(pattern, replacing, string)
    # combines the pattern with some regex symbols in raw string format
    #                   ^  Matches pattern to the beginning of the string
    #                   * Pattern zero to many times
    #                   (.*?) nongreedy matching of zero to many char
    #                   * Pattern zero to many times
    #                   $ Matches to the end of the string

    #                   replaces the first g
    return re.sub(r'^' + pattern + r'*(.*?)' + pattern + r'*$', r'\1', string)

    #stripRegex = re.compile(r'\s*' + pattern + r'\s*') # sets up pattern to match
    # stripRegex.sub(pattern, string)  # Returns newString with pattern stripped


# Function Testing
# TRUE
# string = 'this is a test. THIS IS ONLY A TEST. TeSt. test test test'
string = '   Geeks for Geeks   '
pattern = ' Geeks'
newStrip(string, pattern)


#EX
# Python code to illustrate the working of strip()
string = '   Geeks for Geeks   '
  # Leading spaces are removed
print(string.strip())
# Geeks is removed
print(string.strip('   Geeks'))
# Not removed since the spaces do not match
print(string.strip('Geeks'))
