# Automate the Boring Stuff with Python 3
# Vid Lesson 3 - printing / input / functions

# This program says hello and asks for my name

# Calls the print function
# Funtions are like mini programs
# Input passed to function are call arguments
print("Hello World!") # Function that prints to std output


print("What is you name?") # ask for their name -> Passes string to print
myName = input() # Calls input() function to retrieve user string from std in
print(" It is good to meet you, " + myName)
print("The length of your is :")
print(len(myName)) # Calls len() to return the length of the string that is passed into the print()

print("What is your age?") # ask for their age
myAge = input() # Input() returns string via std in
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
# myAge is initially a string that is converted to int to ADD 1 then back to a str to concat the other strs

# Converting values between data types
str(26) # returns a string
int("1234") # returns an integer
float("3.14") # returns a float
