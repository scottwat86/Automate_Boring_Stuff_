#! python3
# 6_password_locker.py - An insecure password locker program.

#               Automate the Boring Stuff with Python 3
#               Ch 6

import sys # argv will store command line arguments
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
                            'blog':   'VmALvQyKAxiVH5G8c01if1MLZF3sdt',
                            'luggage': '12345' }

# Checks if used provdied correct number of comman line arguments
# If no then the program exits
if len(sys.argv) < 2:
    print('Usage: python password_locker.py [account] - copy acount password')
    sys.exit()

script, account = sys.argv # first command line argv is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
