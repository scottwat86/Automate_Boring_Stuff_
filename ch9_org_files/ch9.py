#               Automate the Boring Stuff with Python 3
#               Ch 9 -  Organizing Files
#

import shutil, os, sys

script, path = sys.argv

os.chdir(path) # Changes to the directory given as an argv

#                   COPYING FILES AND FOLDERS
shutil.copy('.\\spam.txt', '.\\delicious')
shutil.copy('.\\eggs.txt', '.\\delicious\\eggs2.txt')

# Creates a new folder with same content as original file
shutil.copytree('.\\bacon', '.\\bacon_backup')

#                   MOVING AND RENAMING FILES AND FOLDERS
# moves eggs.txt to bacon
shutil.move('.\\eggs.txt', '.\\bacon')

# shutil.move('spam.txt,' '.\\does_not_exist\\eggs\\ham')
# FileNotFoundError

#                   PERMANENTLY DELETING FILES AND ThisFolderDoesNotExist

#       os.unlink()  will delete the file at path
#       os.rmdir()  will delete the folder at path, folder must be empty
#        shutil.remtree() will remove the folder at path and all files and folders

# CAREFUL
# import os
for filename in os.listdir():
    if filename.endswith('.rxt'):
        # os.unline(filename)
        print(filename)

#                   SAFE DELETES WITH THE SEND2TRASH MODULE
import send2trash

with open('bacon.txt', 'a') as baconFile: # creates file and opens in append mode
    baconFile.write('Bacon is not a vegetable.')

os.listdir('.\\')

send2trash.send2trash('bacon.txt')   # send2trash() can only send files to the recycling bin
# To free up disk space and delete permanently use os and shutil functions for deleting files

#               WALKING A DIRECTORY TREE
# import os

# os.walk() walks through the directory tree
# Unlike range(), os.walk() returns three values on each iteration
for folderName, subfolders, filenames in os.walk('.delicious'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ':' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

    print('')

#               COMPRESSING FILES WITH THE ZIPFILE MODULE
import zipfile, os

# os.chdir(path) # move to the folder with example zip
os.listdir()
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()

spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size

'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
exampleZip.close()

# import zipfile, os
# os.chdir(path)
with zipfile.ZipFile('example.zip') as exampleZip:
     exampleZip.extractall('.\\extract')
     exampleZip.extract('spam.txt', '.\\extract2')
 # exampleZip.close() # Autocloses with the WITH

#           CREATING AND ADDING TO ZIP FILES
# import zipfile
with zipfile.ZipFile('new.zip', 'w') as newZip:
    newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# You can also pass the 'a' for append mode

#               PRACTICE PROBLEMS
#             1)    shutil.copy() copies just a file/directory into directory specified
#                   shutil.copytree() recursively copies the enire directory tree 
#             2)shutil.move() can be used to rename
#
#             3)  send2trash.send2trash() sends files to the recycling bin instead of permanently deleting
#                  shutil.rmtree(path) removes the entire directory tree permanently
#             4) zipfile.ZipFile('') opens a zip file similar to open()
