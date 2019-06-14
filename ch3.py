#               Automate the Boring Stuff with Python 3
#               Ch 3 - Functions
#               Functions are used for code that you want to repeat
#
# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there.')
#
# hello()
#
# #            FUNCTIONS W/ PARAMETERS
# def hello(name):  # name is a parameter to the function
#     print("Hello " + name)
# #
# # hello('Alice')
# # hello('Bob')
# #
# import random
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidely so'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubful'
#
# print(getAnswer(random.randint(1,9)))
# # r = random.randint(1,9)
# # fortune = getAnswer(r)
# # print(fortune)
#
# #             NONE
# #              represents the absence of a value
# #             All Functions return None if no other return statement
# None
# spam = print("Hello")
# spam == None
#
# #           KEYWORD ARG
# print("hello", 'there', sep='-', end=' the end') # hello-there the end
#
# #             LOCAL AND GLOBAL SCOPE
##              Local scope contain any variables/parameters assigned within a function
##             All variables/values within a scope are destroy with the scope (function returns)
##              The is only ONE Global Scope
##              Global scope cannot use any local variables
##              Local scope CAN access Global variables
##              Function local variables cannot use variable in other local scopes
##              Variables can have the same name as long as they are in different scopes
##              Scopes compartmentalize changes and impact due to sed changes
#
##              Local Variables Cannot Be Used in the Global Scope
# def spam():
#     eggs = 31_337
# spam()
# print(eggs) # NameError   -> Global scope can't see local variable
#
##              Local Scopes Cannot Use Variables in Other Local Scopes
# def spam():
#     eggs = 99 # This is still 99 at run b/c
#     bacon()
#     print(eggs)
#
# def bacon():
#     ham = 101
#     eggs = 0 # this eggs is only seen here
#
# spam()
#
##              Global Variables Can Be Read from a Local Scope
# def spam():
#     print(eggs)
#
# eggs = 42
# spam()
# print(eggs)
#
##              Local and Global Variables with the Same Name
# def spam():
#     eggs = 'spam local'
#     print(eggs) # prints 'spam local'
#
# def bacon():
#     eggs = 'bacon local'
#     print(eggs) # prints 'bacon local'
#     spam()
#     print(eggs) # prints 'bacon local'
#
# eggs = 'global'
# bacon()
# print(eggs) # prints 'Global'
#
##          Global Statemnet
##          1) If a var is veing used in global scop then it is alway global
##          2) If there is global statement for a var within a function, it is global
##          3) Otherwise, if the var is used in an assignment statement in the func it is local
##          4) BUT if the ar is not used in an assign, it is global
#
# def spam():
#     global eggs
#     eggs = 'spam'
#
# eggs = 'global'
# spam()
# print(eggs
#
# def spam():
#     global eggs
#     eggs = 'spam' # this is the global
#
# def bacon():
#     eggs ='bacon' # this is a local
#
# def ham():
#     print(eggs) # this is the global
#
# eggs = 42 # this is the globaland
# spam()
# print(eggs)
#
#  #            EXCEPTION HANDLING
#
# def spam(divideBy):
#     return/divideBy
#
# print(spam(2))
# print(spam(12))
# # print(spam(0)) # ZeroDivisionError
#
# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid argument.')
#
# print(spam(0))
#
##          Short Progam - Guess the Number
# from random import randint
# num = randint(1,20)
# print("I am thinking of a number between 1 and 20.")
# print(num)
#
# for i in range(1,7):
#     # while True: # Ensures appropriate input                                    -> FIX THIS
#     #     try:
#     #         guess = int(input("Take a guess. \n> "))
#     #         break
#     #     except ValueError:
#     #         guess = int(input("Invalid guess. Try again. \n> "))
#     #         continue
#     guess = int(input("Take a guess. \n> "))
#     if num > guess:
#         print('Your guess is too low.')
#     elif num < guess:
#         print('Your guess is too high.')
#     else:
#         break
#
# if num == guess:
#     print(f'Good job! You guessed my number in {i} guesses') # Could hav made this an else statement instead
# else:
#     print(f'Nope. The number I was thinking of was {num}\n')
# print('Good Bye')
#
##              QUESTIONS
##               1) Functions limit the impact of errors and simplify implementation by compartmentlizing the solution
##               2) Functions are executed when they are called
##               3) def statement
##               4) Function is definition of instructions. Funct call is an evaluation of sed instructions
##               5) One global scope, one local scope for every function
##               6) it is destroy/forgotten
##               7) return value is  information outputed by a function. Yes since a return value is a value it can be part of an expression.
##               8) All functions return None if no other return is provided
##               9) within a function def -> global the_variable
##               10) None represents a lack of a value or null
##               11) import areallyourpetsnamederic goes to the areallyourpetsnamederic module and retrieve the code for use
##               12) spam.bacon()   or   from spam import bacon  bacon()
##               13) use    try:            except Error:
##               14) try contain the code you want to evaluate      except catches the error if it hits in the try clause and contains code to execute after
