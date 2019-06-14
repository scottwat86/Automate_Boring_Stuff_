#               Automate the Boring Stuff with Python 3
#               Ch 1 - Python Basics
#
#
# # EXPRESSION
#
# 2 + 2
# (2 + 2) / 4 # 1
# 10_000 # 10,000
#
# #  OPERATORS
# #   + Addition
# #   - Subtraction
# #   * Multiplication
# #   / Division
# #   % Modulus
# #   // Integer / Truncated Division
# #   ** Exponentia
# # Order of Operation  * / // %+ - (left to right)
#
# # Expressions are collapsed to a single ValueError
#
# # Integer, Float, and String Data Types
# #   INTEGERS
#
# 1
# -5
# int("2") # Converts string to int
# int('2.4') # This will throw a ValueError as it cannot convert to int directly
# int(2.4) # 2
#
# #   FLOAT
# 21.5
# 3.14
# float(1) # Converts int to float 1.0
#
# #   STRING
#
# "The"
# 'cat'
# """
# in the
# hat
# """
# str(4) # converts int to string
# 'the' + ' cat' # Concantenation
#  str(5) + ' cats' # If you don't have the str() its a TypeError
#  "Bye " * 2 # Bye Bye # This only works with int NOT floats
#
# # VARIABLES
# # Variables are boxes store values via evaluate expression
#
# spam = 42 # assignment operator '=' initializes spam
# eggs = 2
# bacon = 10_000
# spam / eggs * bacon # Note that / division returns a float
# spam = eggs # both 'boxes' point to the same value
# _   # This is the throwaway var, it holds info that you don't care about
#
# # Var Naming Rules
# #   Can only be one word
# #   Can use letters, numbers, and underscore _
# #   Cannot begin with a number
#
# #   This prgoram says hello and asks for user's name

print("Hello world!")
print('What is your name?')     # Ask for their name
myName = input()

print('It is good to mee you, ' + myName)

print('The length of your name is:')
print(len(myName))
#

print('What is your age?')
myAge = input() # Default input is string

print(f"You will be {int(myAge+1)} in a year")  # This achieves same as below
# print('You will be ' + str(int(myAge)+1) + ' in a year.')

# QUESTIONS

# 1)    VALUES = 'hello'  5 -88.8    OPERATORS= * - / +
# 2)    spam is a var       'spam' is a string
# 3)    Datatypes -> str, float, int, list, dictionary, set, tuple
# 4)    Expressions only contain operators, literals, identifies; they represent a single value
# 5)    Expressions are represent a values, and be combined/composed into larger expressions
#        Pure Expression, subexpre. do not have any order of execution/dependency
#         Statements do not return a value, are stand alone and do not return anything
 # 6)   20, ; the second line doesn not assign anything
 # 7)   spamspamspam    &      spamspamspam
 # 8)   variables must start with a letter
 # 9)   str() float() int()
 # 10)  TypeError, cannot combine a string with an int unless you convert the str(integer)
 # EXTRA    abs() absolute value    bool() converts to Boolean  type()  returns object type
 #                  round() by default rounds to int,
