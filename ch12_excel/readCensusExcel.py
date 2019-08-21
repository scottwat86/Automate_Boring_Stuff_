#! python3
#               Automate the Boring Stuff with Python 3
#               Chapter 12 – Working with Excel Spreadsheets

#  readCensusExcel.py - Tabulates population and number of census tracts for
   #                                    each county.

   # The readCensusExcel.py program was throwaway code: Once you have its results saved to
   # census2010.py, you won’t need to run the program again.

import openpyxl, pprint, os
print('Opening workbook...')

# Defines local variable path for Ch12
path = os.environ['python_home'] + '\\Automate_Boring_Stuff_\\ch12_excel'
os.chdir(path)

# TODO - Read the data from Excel
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

# TODO - Counts the number of census tracts in each county
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state    = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop      = sheet['D' + str(row)].value

    # Two lines create keys for state, tract, and pop, to avoid errors in the next two lines
    # setdefault() does nothing if a key exists
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'tracts' : 0, 'pop': 0})

    countyData[state][county]['tracts'] += 1 # Each row represemts one census tract, so increment by 1
    countyData[state][county]['pop'] += int(pop) # Increase the county pop by the pop in this census tract

# TODO - Counts the total population of each county
print('Writing results........')
resultFile = open('_census2010.py', 'w')
# pprint.pformat() produces a string that itself is formatteed as Python code.
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')

# TODO - Prints the results
