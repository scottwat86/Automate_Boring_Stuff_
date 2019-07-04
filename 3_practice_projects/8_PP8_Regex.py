#               Automate the Boring Stuff with Python 3
#               Ch 8 -  Practice Project - Regex Search

#               By Scott Watson

'''
Write a program that opens all .txt files in a folder and searches for any line that
matches a user-supplied regular expression. The results should be printed to the screen.
'''
import re, os, sys

script, filePath = sys.argv

try:
    os.chdir(filePath)
except:
    print('The file path was invalid')

files = [f for f in os.listdir('.') if os.path.isfile(f)] # produces a list of files in the CWD

pattern = input('Enter a regular expression to match\n\n>>') # Gets user supplied regex
check = re.compile(pattern) # Compiles regex and assigns to var pattern

matches = {}
# Loops through the files, open them, converts to a string for searching
for file in files:
    with open(file, 'r') as f:
        string = f.read()
        string
    lines = string.split('\n')
    for i in range(len(lines)):
        if check.search(lines[i], re.IGNORECASE) != None:
            # If a match is record to a dictionary with the file name as the key and (match, line number, starting index, ending index)
            matches[file] = (check.search(lines[i], re.IGNORECASE).group(0)+1, i, check.search(lines[i], re.IGNORECASE).start(), check.search(lines[i], re.IGNORECASE).end())
            print('File:' + file, '\nMatch:' + str(matches[file][0]) +'\nLine #:' + str(matches[file][1]) + '\nStart Index:' + str(matches[file][2]) +'\nEnd Index:' + str(matches[file][3]))
