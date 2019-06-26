#               Automate the Boring Stuff with Python 3
#               Ch 8 -  Reading and Writing Files
#

# Windows
# Root Dir -> C:\
# DVD / USB Volumes -> D:\   or  E:\
#  BACKSLASH

# OSX and Linux
# Root Dir /
#  DVD / USB Volumes -> /Volume  OSX   /mnt Linux
# FORWARD SLASH

import os
os.path.join('usr', 'bin', 'spam') # 'usr\\bin\\spam' # Note the extra \ to escape the 2nd \

myFile = ['accounts.txt', 'deatils.csv', 'invite.docx']
for filename in myFile:
    print(os.path.join('C:\\Users\\scott_watson\\Documents\\Python', filename))
r'''
C:\Users\scott_watson\Documents\Python\accounts.txt
C:\Users\scott_watson\Documents\Python\deatils.csv
C:\Users\scott_watson\Documents\Python\invite.docx
'''

#               CURRENT WORKING DIRECTORY

import os

os.getcwd()
os.chdir('C:\\')
os.getcwd()

# os.chdir('C:\\ThisFolderDoesNotExist')
# The above would throw a FileNotFoundError

#               ABSOLUTE VS RELATIVE PATHS
# There are two ways to specify a file path
#       absolute -> relative to the roo directory
#        relative -> relative to the current working directory

#       . specifies this directory -> is optional when specifying a file
#      .. specifies one directory back (parent)

#              HANDLING ABSOLUTE AND RELATIVE PATHS
#       os.path.abspath(path) returns string of the absolute path of argument
#       os.path.istabs(path)  returns True if the arg is an absolute path
#       os.path.relpath(path, start) returns a string of a relative path from the start path to the path

os.path.abspath('.') # Absolute path of the cwd
os.path.abspath('.\\1_Chapters')
os.path.isabs('.')  # False
os.path.isabs(os.path.abspath('.')) #True

os.path.relpath('C:\\Windows', 'C:\\') #'Windows'
os.path.relpath('C:\\Windows', 'C:\\spam\\eggs') #'..\\..\\Windows'
os.getcwd()

#        os.path.dirname(path) returns a string of everthing that comes before the last slash in the path
#       os.path.basename(path) returns a string of everything that comes after the last slash
#           C:\Windows\System32  -> Dirname
#            calc.exe -> basename

path = 'C:\\Users\\scott_watson\\Documents\\Python\\Automate_Boring_Stuff_'
os.path.basename(path) #'Automate_Boring_Stuff_'
os.path.dirname(path) #'C:\\Users\\scott_watson\\Documents\\Python'

os.path.split(path) # returns dirname and basename as seperate strings in a tuple
