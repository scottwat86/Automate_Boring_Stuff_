#! python3
# 6_phoneAndEmail.py - FInds phone number and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                         # area code      (OPTIONAL)
    (\s|-|\.)?                                          # seperator      (OPTIONAL)
    (\d{3})                                         # first 3 digits
    (\s|-|\.)                                          # seperator
    (\d{4})                                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?       # extension      (OPTIONAL)
)''', re.VERBOSE)

# TODO : Create email regex.
emailRegex = re.compile(r'''(
                [a-zA-z0-9._%+-]+            # username     lowercase upper case numeric OR .-%+-
                @                                       # @ symbol
                [a-zA-Z0-9.-]+                  # domain name
                (\.[a-zA-Z]{2,4})              # dot-something
    )''', re.VERBOSE)

# TODO: Find Matches in Clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + group[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])  # Matches the entire regex

# TODO: Copy results to the Clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')


''' OUTPUT AFTER COPYING TO CLIPBOARD THEN RUNNING
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com
'''
