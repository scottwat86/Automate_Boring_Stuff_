# Automate the Boring Stuff with Python 3
# Vid Lesson 5 - Flow Control

# name = 'Alice'
# name = 'Bob'
# if name ==  'Alice': # Starts the if block statement
#     print("Hi Alice") # Blocks are indented
# else:
#     print('Bob')
# print('Done!')
#
# password = 'swordfish'
# if password == 'swordfish':
#     print('Access granted!')
# else:
#     print('Access Denied!')


name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice!')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead immortal vampire.')
elif age > 100:
    print("You are not Alice granny.")
# you can have as many of the elif as you want but order of operation matter
else:
    print("Hello?") # executes if none of the elif or if statement are true

# Truethy -> "" = False any other string is True
print("Enter your name")
name = input()
if name: # It is better to be explicit with conditionals
    print('Thank you for entering a name.')
else:
    print('You did not enter a name')

    bool("t") # Evaluates truethy statements
