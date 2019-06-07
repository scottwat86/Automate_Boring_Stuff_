#               Python Cookbook
#               Chapter 9 - Functions

# Every function has a return statemnet
# if functions have no return the default is None
# Functions are like mini programs
# Functions are made to get rid of duplicate.repeating code
# def statement defines function
# Keyword arguments to functions are usually for optional arguments


# You should avoid duplicating code

# Defines a functions, The code below is not executed until the function is called
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

# Calls the function
hello()


def hello(name):  # name is a parameter of the function
    print("Hello " + name)

hello('Alice') # Hello Alice
hello('Bob') # Hello Bob


def plusOne(number):
    return number + 1 # returns number + 1

plusOne(4)

# Every print returns None as its return value but we don't see it

print("")
None # It is the only value of the None data type

# None represents a lack of a value and will not print by default in the shell


print("Hello ", end="") # Changes from default ending to empy string from newline
print("World") # this shows up on the same line as Hello
print("cat", "dog", "mouse", sep="_") # Chanes the default seperator of space to

from random import randint # Imports randint from random module

# Generates an answer based on input 1-9
def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidely so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"

print("Think of a yes/no question, and press enter to see the answer")
input()

print(getAnswer(randint(1,9)))
