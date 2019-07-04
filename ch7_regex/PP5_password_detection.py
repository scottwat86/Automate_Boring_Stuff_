#               Automate the Boring Stuff with Python 3
#               Ch 7 -  Practice Project - Strong Password Detection

#               By Scott Watson

'''
Write a function that uses regular expressions to make sure the password string it is passed is strong.
You may need to test the string against multiple regex patterns to validate its strength.
'''
import re

def str_pw(password):
    '''
    Determines if a password is strong if it contains the following criteria:
        * At least eight characters long
        * Uses both uppercase and lowercase characters
        * At least one digit
    '''
       # Rev 2
    # Sorts password NUMERIC-UPPERCASE-LOWERCASE
    sorted_pass = ''.join(sorted(password))
    # Pattern to check is [one or more numeric] [symbols if any][one or more uppercase][symbols if any][one or more lowercase]
    pwRegex = re.compile(r'\d+[^0-9a-zA-Z]*[A-Z]+[^0-9a-zA-Z]*[a-z]+')
    # Returns True      if  password is 8 char or longer
    #                              AND  boolean converts the regex to True which corresponds a matched object rn
    return len(password) >=8 and bool(pwRegex.search(sorted_pass))


# ################Straight forward but verbose approach
    #
    # uppercase  = False
    # if upperRegex.findall(password) != []:
    #     uppercase = True
    #
    # lowercase  = False
    # if lowerRegex.findall(password) != []:
    #     lowercase = True
    #
    # num  = False
    # if numRegex.findall(password) != []:
    #     num = True
    #
    # length = False
    # if len(password) >=8:
    #     length = True
    #
    # return [length, num, uppercase, lowercase]

# Function Testing
# TRUE
str_pw('asdsgasGASDGSD334234##%$^&()') # UPPER  LOWER NUMERIC  len() = 8
str_pw('!1234ABCd') # NUMERIC UPPER LOWER len() = 8
str_pw('!abcdEFG1') # LOWER UPPER NUMERIC len() = 8
str_pw('abcd1EFG') # LOWER NUMERIC UPPER len() = 8

# FALSE
str_pw('123456') # len() = 6
str_pw('12345678') # All NUMERIC
str_pw('Abcdef1') # len() = 7  Otherwise would be True
str_pw('!Abcdefgh') # Missing NUMERIC
str_pw('#ABCDEFGH') # All UPPER
str_pw('abcdefg1') # Missing UPPER
str_pw('ABCDEFG1') # Missing LOWER
