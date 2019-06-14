#               Automate the Boring Stuff with Python 3
#               Ch 4 -  Practice Project - Comma Code & Grid Print
#               By Scott Watson

'''
PART 1
spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a string with all
the items separated by a comma and a space, with and inserted before the last item.
For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.
'''
print('''
Automate the Boring Stuff
CHAPTER 4 - PRACTIVE PROBLEM

Part 1: Comma Code Output:
''')
def list_to_string(list_in):
    string = ""
    for i in range(len(list_in)):

        # Block condition triggers for all but last index
        if i != (len(list_in) - 1):
            string += str(list_in[i])+", "

        else:
            string += 'and ' + str(list_in[i])

    return string

# spam =  [[1],(2,),{3},{1:2},5.0,5] # Testing to see if other data types work
spam = ['apples', 'bananas', 'tofu', 'cats']
string_list = list_to_string(spam)
print(string_list)

print('----------------------------------------------------------\n')
'''
PART 2 - Character Picture Grid
Given the input below generate the below output:

            ..OO.OO..
            .OOOOOOO.
            .OOOOOOO.
            ..OOOOO..
            ...OOO...
            ....O....
'''
# Reproducing grid[9][6]
#  9 column x 6 rows
# Note that the above is transposed matrix of the original grid

print('Part 2 - Character Picture Grid:')

#           GIVEN INPUT
grid = [
#            0  1  2  3   4  5
            ['.', '.', '.', '.', '.', '.'],             # 0
            ['.', 'O', 'O', '.', '.', '.'],         # 1
            ['O', 'O', 'O', 'O', '.', '.'],     # 2
            ['O', 'O', 'O', 'O', 'O', '.'],   # 3
            ['.', 'O', 'O', 'O', 'O', 'O'],   # 4
            ['O', 'O', 'O', 'O', 'O', '.'],   # 5
            ['O', 'O', 'O', 'O', '.', '.'],     # 6
            ['.', 'O', 'O', '.', '.', '.'],         # 7
            ['.', '.', '.', '.', '.', '.']              # 8
            ]
#prints input
print(grid)

# Assume all rows have same COL_NUM
col_num = len(grid[0])

# Prints transposed list of lists from grid input
for i in range(col_num):
    print('\n')
    for j in range(len(grid)):
        print(grid[j][i], end='')

"""
# MOST ELEGANT SOLUTION
# From overstack:
# https://stackoverflow.com/questions/35441305/automate-the-boring-stuff-with-python-chapter-4-practice-project-ii
#
#    0) Uses def statment to make this a method
#    1) Uses zip() to unpack the sublists within for loop
#    2) Then uses join() and the fact that lists are iterable
#    to iterate through a join on an empty string '' with the sublist

def fish():
    for line in zip(*grid):
        print(''.join(line))

fish()
"""
###################################
'''
FINDING COL_NUM
Was trying to make this generic for any length of list
but realized that realistic all rows must have the same
col_num. I revised my above solution to simply Enter
the col_num but the below will find the the max col_num

# Row num for indexing
row_num = len(grid)

# Find max number of columns for indexing
for i in range(row_num):
    col_num = 0
    if col_num >= len(grid[i]):
        continue
    else:
        col_num = len(grid[i])
'''
###################################

# SIMPLE BUT DUMB
#This works if you manual enter the grid below
# grid = [
# #            0   1   2     3    4    5    6    7   8
#             ['.', '.', 'O', 'O', '.', 'O', 'O', '.', '.'],              # 0
#             ['.', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '.'],         # 1
#             ['.', 'O', 'O', 'O', 'O', 'O', 'O', 'O', '.'],         # 2
#             ['.', '.', 'O', 'O', 'O', 'O', 'O', '.', '.'],            # 3
#             ['.', '.', '.', 'O', 'O', 'O', '.', '.', '.'],                # 4
#             ['.', '.', '.', '.', 'O', '.', '.', '.', '.'],                     # 5
#             ]
