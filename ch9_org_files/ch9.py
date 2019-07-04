#               Automate the Boring Stuff with Python 3
#               Ch 9 -  Organizing Files
#

import shutil, os

os.chdir('C:\\Users\\scott_watson\\Documents\\Python\\Automate_Boring_Stuff_')

#                   COPYING FILES AND FOLDERS
shutil.copy('C:\\spam.txt', 'C:\\delicious')
shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')

# Creates a new folder with same content as original file
shutil.copytree('C:\\bacon', 'C:\\bacon_backup')

#                   MOVING AND RENAMING FILES AND FOLDERS

# moves eggs.txt to bacon
shutil.move('C:\\eggs.txt', 'C:\\bacon')

# shutil.move('spam.txt,' 'C:\\does_not_exist\\eggs\\ham')
#FileNotFoundError


#                   PERMANENTLY DELETING FILES AND ThisFolderDoesNotExist

# os.unlinl(path)
# os.rmdir(path)
# shutil.remtree(path)

# CAREFUL
# import os
# for filename in os.listdir():
#     if filename.endwith('.rxt'):
#         os.unline(filename)


#                   SAFE DELETES WITH THE SEND2TRASH MODULE
# import send2trash
#
# baconFile = open('bacon.txt', 'a') # creates file
# baconFile.write('Bacon is not a vegetable.')
# baconFile.close()

# send2trash.send2trash('bacon.txt')   # send2trash() can only send files to the recycling bin
# To free up disk space and delete permanently use os and shutil functions for deleting files

#               WALKING A DIRECTORY TREE
os.getcwd()
os.chdir('C:\\Users\\scott_watson\\Documents\\Python\\Automate_Boring_Stuff_')
os.walk()
