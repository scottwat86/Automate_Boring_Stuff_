#   This prgoram says hello and asks for user's name

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
print('You will be ' + str(int(myAge)+1) + ' in a year.')
