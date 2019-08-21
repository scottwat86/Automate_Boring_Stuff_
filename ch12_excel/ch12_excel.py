#               Automate the Boring Stuff with Python 3
#               Chapter 12 – Working with Excel Spreadsheets

# OpenPyXL is a package for reading and writing Excel files. OpenPyXL covers  advanced
# features of Excel such as charts, styles, number formatting and conditional formatting.
# It even includes a tokeniser for parsing Excel formulas and isupports Pandas as well

# Can be quite slow for handling large files -> If you have to write reports with thousands of rows
# and your application is time-sensitive then XlsxWriter or PyExcelerate may be better choices

# More Info for Excel modules
# https://www.pyxll.com/blog/tools-for-working-with-excel-and-python/

'''
I recognize that I will be repeating some import statments and other code but in the interest of
learning I will follow the book literally and retype the code to better remember in the future
'''


import openpyxl, os

# Defines local variable path for Ch12
path = os.environ['python_home'] + '\\Automate_Boring_Stuff_\\ch12_excel'
os.chdir(path)

# Opening workbook examples.xlsx
wb = openpyxl.load_workbook('example.xlsx')
type(wb) # openpyxl.workbook.workbook.Workbook

# GETTOMG SHEETS FROM THE WORKBOOK
import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
wb.get_sheet_names()
# ...['Sheet1', 'Sheet2', 'Sheet3']

sheet = wb.get_sheet_by_name('Sheet3')
sheet # <Worksheet "Sheet3">
type(sheet) #openpyxl.worksheet.worksheet.Worksheet
sheet.title # 'Sheet3'

anotherSheet = wb.active # Sheet1 is the active sheet
anotherSheet #<Worksheet "Sheet1">

# GETTING CELLS FROM THE SHEETS

import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
sheet['A1'] #<Cell 'Sheet3'.A1>
sheet['A1'].value #datetime.datetime(2015, 4, 5, 13, 34, 2)
# openpyxl interprets the datetime data instead of a string

 c = sheet['B1'] # Initlize variable with openpyxl.cell.cell.Cell object
 c.value # 'Apples'

'Row ' + str(c.row) + '. Column ' + c.column_letter + ' is ' + c.value #'Row 1. Column B is Apples'
# cell.column revised to cell.column_letter as column is only the int index not the letter

'Cell ' + c.coordinate + ' is ' + c.value # 'Cell B1 is Apples'
sheet['C1'].value # 73

# First row / column starts at 1 NOT 0
sheet.cell(row=1, column=2) #<Cell 'Sheet1'.B1>
sheet.cell(row=1, column=2).value # 'Apples'

for i in range(1, 8, 2):
    print(i, sheet.cell(row=i, column=2).value)
'''
1 Apples
3 Pears
5 Apples
7 Strawberries
'''

import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
sheet.max_row # 7
sheet.max_column # 3 -> C

# CONVERTING BETWEEN COLUMN LETTERS AND NUMBERS
import openpyxl

# This code is out of date  openpyxl.cell became -> openpyxl.util
from openpyxl.utils import get_column_letter, column_index_from_string

# now its just get_column
get_column_letter(1) # 'A'
get_column_letter(2) # 'B'
get_column_letter(27) # 'AA'
get_column_letter(900) # 'AHP'

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
get_column_letter(sheet.max_column) # 'C' is the largest column with a value in it

column_index_from_string('A') # 1
column_index_from_string('AA') # 27

# GETTING ROWS AND COLUMNS FROM THE SHEETS
import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
tuple(sheet['A1' : 'C3'])
'''
((<Cell 'Sheet1'.A1>, <Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>),
 (<Cell 'Sheet1'.A2>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>),
 (<Cell 'Sheet1'.A3>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>))
'''

for rowOfCellObjects in sheet['A1' : 'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')

'''
A1 2015-04-05 13:34:02
B1 Apples
C1 73
--- END OF ROW ---
A2 2015-04-05 03:41:23
B2 Cherries
C2 85
--- END OF ROW ---
A3 2015-04-06 12:46:51
B3 Pears
C3 14
--- END OF ROW ---

'''
# sheet['A1' : 'C3']   -> provies a geneterator object of the cells included in the range

import openpyxl
wb = openpyxl.load_workbook('example.xlsx')

# Revise sheet.columns[1] -> sheet['B'] now
sheet['B']
'''
(<Cell 'Sheet1'.B1>,
 <Cell 'Sheet1'.B2>,
 <Cell 'Sheet1'.B3>,
 <Cell 'Sheet1'.B4>,
 <Cell 'Sheet1'.B5>,
 <Cell 'Sheet1'.B6>,
 <Cell 'Sheet1'.B7>)
'''

for cellObj in sheet['B']:
    print(cellObj.value)
'''
Apples
Cherries
Pears
Oranges
Apples
Bananas
Strawberries
'''

# WORKBOOKS, SHEETS, CELLS
import openpyxl # Import module
wb = openpyxl.load_workbook('example.xlsx') # Get Workbook object
active_sheet = wb.active # Read Active Sheet Variable
active_sheet.title # 'Sheet1'
sheet = wb.get_sheet_by_name('Sheet1') # Retreive Sheet object

sheet.cell(row=1, column=2) # <Cell 'Sheet1'.B1>  cell()
sheet['B1'] # <Cell 'Sheet1'.B1>  indexing
