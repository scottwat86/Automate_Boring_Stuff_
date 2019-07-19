#! python3
#  Practice Project 12 - Debugging Coin Toss

# By Scott Watson

import random
guess = ''
while guess.lower() not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.choice(['heads', 'tails']) # tails or heads
if toss == guess.lower():
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess.lower():
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
