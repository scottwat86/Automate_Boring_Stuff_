#               Automate the Boring Stuff with Python 3
#               Ch 3 - Functions
#               Functions are used for code that you want to repeat

##################### SIMPLE FUNCTION
#                   helloFunc.py
#####################

#            FUNCTIONS W/ PARAMETERS
def hello(name):  # name is a parameter to the function
    print("Hello " + name)

hello('Alice')
hello('Bob')

##################### FORTUNE FUNCTION
#                    magic8Ball.py
#####################


#             NONE
#              represents the absence of a value
#             All Functions return None if no other return statement
None
spam = print("Hello")
spam == None

#           KEYWORD ARG
print("hello", 'there', sep='-', end=' the end') # hello-there the end

#             LOCAL AND GLOBAL SCOPE
#              Local scope contain any variables/parameters assigned within a function
#             All variables/values within a scope are destroy with the scope (function returns)
#              The is only ONE Global Scope
#              Global scope cannot use any local variables
#              Local scope CAN access Global variables
#              Function local variables cannot use variable in other local scopes
#              Variables can have the same name as long as they are in different scopes
#              Scopes compartmentalize changes and impact due to sed changes

#              Local Variables Cannot Be Used in the Global Scope
def spam():
    eggs = 31_337
spam()
print(eggs) # NameError   -> Global scope can't see local variable

#              Local Scopes Cannot Use Variables in Other Local Scopes
def spam():
    eggs = 99 # This is still 99 at run b/c
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0 # this eggs is only seen here

spam()

#              Global Variables Can Be Read from a Local Scope
def spam():
    print(eggs)

eggs = 42
spam()
print(eggs)

#####################LOCAL AND GLOBAL VARIABLES W SAME NAME
#                   sameName.py
#####################

#          Global Statemnet
#          1) If a var is being used in global scop then it is alway global
#          2) If there is global statement for a var within a function, it is global
#          3) Otherwise, if the var is used in an assignment statement in the func it is local
#          4) BUT if the ar is not used in an assign, it is global

#####################GLOBAL STATEMENT
#                   sameName2.py
#####################

#####################GLOBAL STATEMENT
#                   sameName3.py
#####################

 #            EXCEPTION HANDLING

def spam(divideBy):
    return/divideBy

print(spam(2))
print(spam(12))
# print(spam(0)) # ZeroDivisionError

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(0))

#####################GUESS GAME
#                   guessTheNumber.py
#####################

#              QUESTIONS
#               1) Functions limit the impact of errors and simplify implementation by compartmentlizing the solution
#               2) Functions are executed when they are called
#               3) def statement
#               4) Function is definition of instructions. Funct call is an evaluation of sed instructions
#               5) One global scope, one local scope for every function
#               6) it is destroy/forgotten
#               7) return value is  information outputed by a function. Yes since a return value is a value it can be part of an expression.
#               8) All functions return None if no other return is provided
#               9) within a function def -> global the_variable
#               10) None represents a lack of a value or null
#               11) import areallyourpetsnamederic goes to the areallyourpetsnamederic module and retrieve the code for use
#               12) spam.bacon()   or   from spam import bacon  bacon()
#               13) use    try:            except Error:
#               14) try contain the code you want to evaluate      except catches the error if it hits in the try clause and contains code to execute after
