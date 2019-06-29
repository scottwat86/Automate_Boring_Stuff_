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
os.path.split(os.path.sep) #('\\', '')

#                   FINDING FILES SIZE AND FOLDER CONTENTS
os.path.getsize(path) #40960  # size of file/directory in bytes

os.listdir(path)
r'''
['.git',
 '0_files',
 '1_Chapters',
 '2_video_lessons',
 '3_practice_projects',
 'README.md'] '''

os.path.getsize('README.md')  #376  bytes

# Attribute Error
# totalSize = 0
# for filename in os.listdir('C:\\Windows\\System32'):
#     totalSize = totalSize + os.path.getsize(os.path.joint('C:\\Windows\\System32', filename))
# print(totalSize)

#               CHECKING PATH VALIDITY
os.path.exists('.') #True -> checks if the current working directory exists
os.path.isfile(path) #False -> returns if arg exists and is a file
os.path.isdir(path) # True -> returns if path arg exists and is a folder
os.path.exists('C:\\Windows')
os.path.exists('C:\\some_made_up+folder') #False
os.path.isdir('C:\\Windows\\System32') # True
os.path.isfile('C:\\Windows\\System32') #False

os.path.exists('D:\\')

#               FILE READING / WRITING PROCESS
#               open() return a file object
#               read() or write() method on the file object
#               close() closes the file

#               OPENING FILES WITH THE OPEN() FUNCTION
helloFile = open('C:\\Users\\scott_watson\\Documents\\Python\\Automate_Boring_Stuff_\\1_Chapters\\hello_world.txt')
helloFile.read() #'Hello World!'
helloFile.close()

#               READING THE CONTENTS OF FILES
helloContent = helloFile.read()
helloContent

os.chdir('C:\\Users\\scott_watson\\Documents\\Python\\Automate_Boring_Stuff_\\1_Chapters\\')
sonnetFile = open('sonnet29.txt')
sonnetFile.readlines()
'''
["When, in disgrace with fortune and men's eyes,\n",
 'I all alone beweep my outcast state,\n',
 'And trouble deaf heaven with my bootless cries,\n',
 'And look upon myself and curse my fate,']
'''


#               WRITING TO FILES
baconFile = open('bacon.txt', 'w')
baconFile.write('Hellow world!\n')

baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

#               SAVING VARIABLES WITH THE SHELVE MODULE

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

type(shelfFile) #shelve.DbfilenameShelf
shelfFile['cats'] #['Zophie', 'Pooka', 'Simon']

shelfFile = shelve.open('mydata')
list(shelfFile.keys()) #['cats']
list(shelfFile.values())

#               SAVING VARIABLES WITH THE PPRINT.PFORMAT() FUNCTION

import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' +pprint.pformat(cats) + '\n')
fileObj.close()

import myCats
myCats.cats
myCats.cats[0] #{'desc': 'chubby', 'name': 'Zophie'}
myCats.cats[0]['name'] #'Zophie'

#               PROJECT: GENERATING RANDOM QUIZ FILES
