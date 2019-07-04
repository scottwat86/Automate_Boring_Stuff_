#          Short Progam - Guess the Number
from random import randint
num = randint(1,20)
print("I am thinking of a number between 1 and 20.")
print(num)

for i in range(1,7):
    while True: # Ensures appropriate input                                    -> FIX THIS
        try:
            guess = int(input("Take a guess. \n> "))
            break
        except ValueError:
            guess = int(input("Invalid guess. Try again. \n> "))
            continue
    guess = int(input("Take a guess. \n> "))
    if num > guess:
        print('Your guess is too low.')
    elif num < guess:
        print('Your guess is too high.')
    else:
        break

if num == guess:
    print(f'Good job! You guessed my number in {i} guesses') # Could hav made this an else statement instead
else:
    print(f'Nope. The number I was thinking of was {num}\n')
print('Good Bye')
