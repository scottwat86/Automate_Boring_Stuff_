#               Automate the Boring Stuff with Python 3
#               Lesson 11 - Functon & Error Handling

# RECAP
# Divide by zero error happens when Python divides a number by zero

# Errors cause the program to crash

# An error that happens inside a try block will cause code in the except
# block to execute. That code can handle the error or display a message to
# the user so that the program can keep going.

def div42by(divideBy):

    try:
        return 42 / divideBy

    except ZeroDivisionError:
        print("Error: You tried to divide by zero.") #Handles Zero Division


print(div42by(2))
print(div42by(12))
print(div42by(0))  # You cannot divide by 0
print(div42by(1))


print("How many cats do you have?")
numCats = input()

try:
    if int(numCats) >= 4:   # needs to convert str to int before boolean comparison
        print("That is a lot of cats!")
    else:
        print("That is not that many cats.")

except ValueError:  # Handles none int / float input
    print("You not enter a number.")
