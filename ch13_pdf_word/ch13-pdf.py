#               Automate the Boring Stuff with Python 3
#               Ch 13 -  Working with PDF and Word Documents

# PDF and Word documents are binary files, which makes them much more complex than
# plaintext files. In addition to text, they store lots of font, color, and layout information.
# If you want your programs to read or write to PDFs or Word documents, you’ll need to do
#  more than simply pass their filenames to open().

# PDF = Portable Document Format

# PyPDF2  module is case sensitive
'''
PyPDF2 might make mistakes when extracting text from a PDF and may even be unable to open
some PDFs at all

PyPDF2 does not have a way to extract images, charts, or other media from PDF documents, but
it can extract text and return it as a Python string.
'''

# Extracting Text from PDFs

import PyPDF2
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) #PyPDF2.pdf.PdfFileReader
# 0 = first page
pageObj = pdfReader.getPage(0) # PyPDF2.pdf.PageObject
pageObj.extractText()
'''
'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of \nMarch 7\n, 2014
\n        \n     The Board of Elementary and Secondary Education shall provide leadership and \n
create policies for education that expand opportunities for children, empower \nfamilies and
communities, and advance Louisiana in an increasingly \ncompetitive glob\nal market.\n BOARD
 \n of ELEMENTARY\n and \n SECONDARY\n EDUCATION\n  '
 '''
 pdfReader.numPages # 19 total pages

# To extract text from a page, you need to get a Page object, which represents a single page of a
#PDF, from a PdfFileReader object.

# Decrypting PDFs
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted # True
# pdfReader.getPage(0)
pdfReader.decrypt('rosebud') # 1
pageObj = pdfReader.getPage(0)


# Creating PDFs
'''
PyPDF2 cannot write arbitrary text to a PDF like Python can do with plaintext files. Instead,
PyPDF2’s PDF-writing capabilities are limited to copying pages from other PDFs, rotating pages,
 overlaying pages, and encrypting files.

General approach:
    1)Open one or more existing PDFs (the source PDFs) into PdfFileReader objects.
    2)Create a new PdfFileWriter object.
    3)Copy pages from the PdfFileReader objects into the PdfFileWriter object.
    4)Finally, use the PdfFileWriter object to write the output PDF.

Creating a PdfFileWriter object creates only a value that represents a PDF document in Python.
It doesn’t create the actual PDF file. For that, you must call the PdfFileWriter’s write() method.

The write() method takes a regular File object that has been opened in write-binary mode.
You can get such a File object by calling Python’s open() function with two arguments:
the string of what you want the PDF’s filename to be and 'wb' to indicate the file should be
opened in write-binary mode.
'''

# Copying Pages PDFs
'''PyPDF2 to copy pages from one PDF document to another. This allows you to combine multiple
PDF files, cut unwanted pages, or reorder pages.'''

import PyPDF2
pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf',  'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

# PyPDF2 cannot insert pages in the middle of a PdfFileWriter object; the addPage() method
# will only add pages to the end.

# Rotating Pages
'''
The pages of a PDF can also be rotated in 90-degree increments with the rotateClockwise() and
rotateCounterClockwise() methods.
'''

import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()


# Overlaying Pages

import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('watermarkCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()


import os
os.chdir('C:\\Users\\scott_watson\\Documents\\Python\\Automate_Boring_Stuff_\\ch13_pdf_word')
