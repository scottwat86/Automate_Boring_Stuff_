#               Automate the Boring Stuff with Python 3
#               Ch 2 - Flow Control / Booleans / Conditions / Loops

##          BOOLEAN VALUES
# True
# False
#
# spam = True # This is case sensitive
# spam
#
# #         if you use 'true' then its a SyntaxError
#
# #         COMPARISON OPERATORS
# #         Evaluate to two values and evaluate to single boolean value
# #         Can be used on any Data Type
# #         Floats/int will never be equal to a string
#
# #         == equat to
# #         != not equal to
# #         < less than
#
# #         Only work for int / floats   NOT Strings
# #         >  greater than
# #         <= less than or equal to
# #         >= greater than or equal to
#
# 42 < 42  # False ... its equal to
# 24 < 42 # True
# 42.0 == 42 # True
# 2 !=3 # True
#
# 'hello' == 'hello'  # True
# 'hello' == 'Hello' # False b/c its case sensitive
# 'dog' != ' cat' # True
#
#
#  #        BINARY OPERATORS
# #         take in boolean values/expressions
#  #        See Truth tables
#
# 42 and True # True
# False or "string"   # True
# 4<5 and True
#
# #         NOT OPERATOR
# #         only evaluates One Boolean
# #         Returns the opposite boolean value
#
# not True
# not "" # True
# not not False # False
#
# #         Computer will evaluate left side first then work right
# (1==2) or (2==2) # True
# 2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2 # Truw True True -> TRUE

# #         ELEMENTS OF FLOW CONTROL
# #         CONDITIONS
# #         Conditions always eval to a single Boolean value
# #         Every flow statement uses a conditions
# #         Cond. Statement always end with :
# #         if / elif / else
#
# #         BLOCK OF CODE
# #         1) Begin when the indentation increases
# #         2) Contain other blocks
# #         3) End with the decrease in indentation
#
# name = 'Mary'
# password = 'swordfish'
# if name == 'Mary':
#     print('Hello Mary')
#     if password == 'swordfish':
#         print('Access granted.')
#     else:
#         print('Wrong password.')

# #         IF / ELSE
#
# name = 'Bob'
# if name == 'Alice':
#     print('Hello Alice')
# else:
#     print('Hello, stranger.')
#
# #         ELIF  -> Else if
#
# name = 'Bob'
# age = 5
# if name == 'Alice':
#     print('Hello Alice!')
# elif age < 12:
#     print('Your not Alice kiddo.')
#
# name = 'Dracula'
# age = 4_000
# if name == 'Alice':
#     print('Hello Alice ')
# elif age <12:
#     print('You are not Alice, kiddo')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead, immortal')
# elif age > 100:
#     print('You are not Alice, grannie.')
#
# #         Alternative
# name = 'Dracula'
# age = 4_000
# if name == 'Alice':
#     print('Hello Alice ')
# elif age <12:
#     print('You are not Alice, kiddo')
# else:
#     print('You are neither Alice nor a little kid.')
#
# #          WHILE LOOP
# #          repeats code for an unknown length until condition is met
# #         Avoid infinite loops they are bugs!
# spam = 0
# while spam < 5:
#     print('Hello world.')
#     spam += 1
#
# #         Annoying Loop
# name = ''
# while name != 'your name':
#     print('Please type your name.')
#     name = input()
# print('Thank you!')
#
# #         BREAK - breaks out of loops
# while True: # Creates an inifite loop
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#         break
# print('Thank you!')
#
# #           CONTINUE - bypasses remaining loop to start another iteration
# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')
#
# #         Truethy and Falsely Values
# #         Are consider equivalent to True / False
# 0.0 and 0 and "" and False # False
# 0.5 and 10 and "sdfdsafsd" and True # True
#
##          Another Loop
# name = ''
# while not name:
#     print("Enter your name:")
#     name = input()
# print('How many guests will you have?')
# numOfGuests = int(input())
# if numOfGuests:
#     print('Be sure to have enough room for all your guests.')
# print('Done')
#
# #         FOR LOOP
# #         Used for looping a certain number of timers
# print('My name is')
# for i in range(5):
#     print('Jimmy Five Times (' + str(i) + ')')
#
##          Another Loop
# total = 0
# for num in range(101):
#     total = total + num
# print(total)
#
##          RANGE and Stepping
# for i in range(0,10,2):
#     print(i)
#
# for i in range(5, -1, -1):
#     print(i)
#
##          IMPORT MODULES
# import random, sys, os, math
# for i in range(5):
#     print(random.randint(1, 10))
#
# from random import * # imports functions/methods to be local
# randint(1, 10)
#
# sys.exit() # Temrinates the program
#
# #         QUESTIONS
##          1) True   False  -> they are case sensitive
##          2) and or not
##          3) AND always False unless everything is True
##              OR  always True unless all statement are False
##          4) False, False, False, False, True
##          5) ==   !=  >   <   <=  >=
##          6) = assigns value to memory   == compares
##          7) Condition checks to see if something is True or False.
##              Used in a flow control statement to make decisions
##          8) block 1 -> lines 2 - 8      block 2 -> lines 4-5     block 3  -> lines 6-7
##          9)
# spam = int(input())
# if spam == 1:
#     print('Hello')
# elif spam == 2:
#     print("Howdy")
# else:
#     print("Greetings!")
#
##          10) CLTRL C
##          11) BREAK ends the loop, CONTINUE stops current iteration and begins a new iteration
##          12) range(10) and range(0,10) are the same. range(0,10,2) counts by step 2
##          13)
# for i in range(1,11):
#     print(i)
#
# i =0
# while i<10:
#     i +=1
#     print(i)
##          14) from spam impot bacon
##          EXTRA) round() rounds to the nearest int by default
##                         abs() returns absolute value
