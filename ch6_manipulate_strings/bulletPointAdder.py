#! python3
# bulletPointAdder.py.py - Adds Wikipedia bullet points to start
# of each line of text on the clipboard

#               Automate the Boring Stuff with Python 3
#               Ch 6

""" IN

Lists of animal
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""

import pyperclip

text = pyperclip.paste()
text_list = text.split("\n") # Splits up the text by \n

bullet_list = "" # This is techincally a string not a list as copy(string) is required later
for line in text_list:
    line = "* " + line
    bullet_list += line

pyperclip.copy(bullet_list)

''' OUT

* Lists of animal
* Lists of aquarium life
* Lists of biologists by author abbreviation
* Lists of cultivars
'''
