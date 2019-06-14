#               Python Cookbook
#               Chapter 8 - Libraries / Modules
import sys, os, math

import random
random.randint(1,101) # generates a random num 0-101

from random import * # imports all the code so functions can be called locally
randint(1,101) # this is less explicit than the prev example so should be avoided

import sys
print("Hello")
sys.exit()
print("Goodbye") # code will never execute b/c exit ends program

# third party modules
# Must be installed using the following in the command line
#           pip install the_module
import pyperclip # allows you to copy and paste from the windows clipboard

copy = pyperclip.copy("Hello") # Copies string to clipboard
paste = pyperclip.paste() # Pastes string from clipboard to paste var
print(paste)
