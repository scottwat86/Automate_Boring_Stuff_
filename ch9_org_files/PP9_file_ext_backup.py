#! python3
# Practice Project 9 - Program selective copies files with the same extension
# from a directory tree beginning at a given parent directory.

# By Scott Watson

import os, shutil, re

# TODO: Takes in arguments from user for parent directory, file extension, and destination
try:
    parent_path = input('Enter the root directory to begin backup from (e.g.  >> C\\origin  ):\n>>')
    while not os.path.isdir(parent_path): # Checks the origin is a valid directory
        parent_path = input('Parent directory does not exist please try again. (e.g.  >> C\\origin  ):\n>>')

    extension = input('Enter one file extension to search for and copy (e.g.  >> .pdf  )\n>>').lower()

    destination = input('Enter the destination directory to copy to (e.g.  >> C\\destination  ):\n>>')
    if not os.path.isdir(destination): # Makes the destination if it doesn't exist
        os.mkdir(destination)
        print('\n***********\n'
                    + 'Destination directory created!'
                    + '\n***********\n')
except: # handles error
        print("Something went terribility wrong. Please try again later. goodbye!")
        exit()

# TODO: Regex to identify file extension
match = re.compile(extension)

# TODO Walk through directories
for root, dirs, files in os.walk(parent_path):
    print('Searching...............' + str(root))


    # TODO: Loop through files in current directory and copy if the proper extension
    for filename in files:
        if match.search(filename):
            print('Match found...............' + filename)
            # os.chdir(destination)
            shutil.copyfile(root +'\\'+ filename, destination + '\\'+ filename)
            print('Copied...............' + filename)
