#! python3
# PP10 - Deleting Unneeded files
#Write a program that walks through a folder tree and searches for exceptionally large files/folders
#   say, ones that have a file size of more than 100MB.
# Print these files with their absolute path to the screen.

import os

max_size = 104_857_600 # bytes = 100MB

try:
    parent_path = input('Enter the root directory to search for files =< 100MB(e.g. >> C\\origin  ):\n>>')
    while not os.path.isdir(parent_path): # Checks the origin is a valid directory
        parent_path = input('Parent directory does not exist please try again. (e.g.  >> C\\origin  ):\n>>')
except: # handles error
  print("Something went terribility wrong. Please try again later. goodbye!")
  exit()

  # TODO: Walk through directories starting at parent_path
  # and search for files greater than or equal to max_size
matches = {}
for root, dirs, filenames in os.walk(parent_path):
    for filename in filenames:
        file_path = os.path.join(root + '\\' + filename)
        if os.path.getsize(file_path) >= max_size:
            print(f'{file_path} ....................... {int(os.path.getsize(file_path) / 1048576)} MB')
            matches[file_path] = int(os.path.getsize(file_path) / 1048576)
