#               Automate the Boring Stuff with Python 3
#               Ch 5 -  Practice Project -  Collatz Sequence
#               By Scott Watson

import sys

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

try:
    userNum = int(input("Select a number to enter into a Collatz Function\n> "))
except ValueError:
    print('You didn\'t enter  a valid number')
    print('Good bye!')
    sys.exit()

while userNum != 1:
    userNum = collatz(userNum)
