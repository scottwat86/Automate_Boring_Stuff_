#               Automate the Boring Stuff with Python 3
#               Ch 6 -  Practice Project - Table Printer

#               By Scott Watson

def printTable(table):

    colWidth  = []
    numCol = len(table[0])
    numRow = len(table)

    for list in table:
         # Sorts each sublist by length and returns sorted last entry
        *_, max = sorted(list, key=len)
        # Assembles a colWidth length for each sublist
        colWidth.append(len(max))

    print('The column width is:', colWidth)

    # Swaps row with columns, prints, and justifies column text to colWidth
    for i in range(0,numCol):
        for j in range(0, numRow):
            print(table[j][i].rjust(colWidth[j]), end=" ")
        print("") # prints a new line

tableData = [  ['apples', 'oranges', 'cherries', 'banana'],
                        ['Alice', 'Bob', 'Carol', 'David'],
                        ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)

''' OUTPUT

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
'''
