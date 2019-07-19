#! python3
#  Practice Project 11 - Filling in the Gaps

# By Scott Watson
"""
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt,
and so on, in a single folder and locates  any gaps in the numbering
"""

# By Scott Watson

import os, re, shutil

# TODO Define Function to intake directory, search files for numbering pattern,
# and created missing number files
def gap_filler(path):

    print(os.listdir(path)) #################

    file_num = 1 # starts the count of file sequence

    pattern = re.compile(r''' (.*?)               # group 1 match text
                                          (\d{3})           # group 2 match 3 numbers
                                          (\.\w*)$         # group 3 match file extension ''', re.VERBOSE)

    for filename in os.listdir(path):
        # Regex matches organized into 3 groups
        mo = pattern.search(filename)
        text = mo.group(1)
        num  = mo.group(2)
        file_ext  = mo.group(3)
        source = os.path.join(path, filename)

        if int(num) == file_num:
            file_num += 1
            print(filename + ' exists. Skipping to the next file.')
            continue
        else:
            # Creates a new file name within the sequence to test
            new_filename = f'{text}{file_num:03}{file_ext}'

        while new_filename in os.listdir(path):
            file_num += 1
            new_filename = f'{text}{file_num:03}{file_ext}'
        else:
            destination  = os.path.join(path, new_filename)
            shutil.move(source, destination)
            print(filename +' >> ' + new_filename+' has been created') ###############


# Call function
file_folder = input("Enter a directory:\n>>")
gap_filler(file_folder)
