#! python3
# mapIt.py - Lauches a map in the browder using an address
# from the command line or clipboard

import sys

import webbrowser, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ''.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

website = 'https://www.google.com/maps/place/' + address
webbrowser.open(website)
