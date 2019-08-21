#! python3
#               Automate the Boring Stuff with Python 3
#               Chapter 12 – Working with Excel Spreadsheets

#  readCensusExcel.py - Tabulates population and number of census tracts for
   #                                    each county.

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

# TODO - Counts the total population of each county


# TODO - Prints the results
