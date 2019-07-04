#               Automate the Boring Stuff with Python 3
#               Lesson 12 - This is a guess the number game.

import random

print("Hello, What is your name?")
name = input()
secretNumber = random.randint(1,20)
print("Well, " + name + ", I am thinking of a number between 1 and 20.")

# print("DEBUG: Secret number is" + str(secretNumber))  # Debugging

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print("Take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " guesses")
else:
    print("Nope. The number I was thinking of way " + str(secretNumber))

# #ROUND 2  I already typed this
# # This is a guess the number game.
# import random
#
# print("Hello. What is your name?")
# name = input()
#
# print("Well, " + name + ", I am thinking of a number between 1and 20.")
# secretNumber = random.randint(1, 20)
#
# for guessesTaken in range(1,7):
#     print("Take a guess.")
#     guess = int(input())
#
#     if guess < secretNumber:
#         print("Your guess is too low.")
#     elif guess > secretNumber:
#         print("Your guess is too high.")
#     else:
#         break #  This condition is for the correct guess!
#
# if guess == secretNumber:
#     print("Good job, " + name + "! You guess the number in " + str(guessesTaken) + " guesses.")
# else:
#     print("Nope, The number I was think of was " + str(secretNumber))
#
# print("You took " + str(guessesTaken) + " guesses.")
