#! python3
#               Automate the Boring Stuff with Python 3
#     mcb.pyw - Saves and loads pieces of text to the clipboard.

#  Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#               py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#               py.exe mcb.pyw list - Loads all keywords to clipboard.

#  Scott Watson Revisions ->  #******************
# Goal: Add a delete <keyword> and delete all commands

'''
    The command line argument for the keyword is checked.
    If the argument is save, then the clipboard contents are saved to the keyword.
    If the argument is list, then all the keywords are copied to the clipboard.
    Otherwise, the text for the keyword is copied to the clipboard.

    Read the command line arguments from sys.argv.
    Read and write to the clipboard.
    Save and load to a shelf file.
'''

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

script, *command = sys.argv # *************

#Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete': # Deletes a specific keyword
    del mcbShelf[sys.argv[2]] # *************
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete': # Loops through all keys and deletes them
        for i in mcbShelf: # *************
            del mcbShelf[i] # *************

mcbShelf.close()
