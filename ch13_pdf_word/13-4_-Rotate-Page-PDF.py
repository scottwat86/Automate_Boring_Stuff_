#               Automate the Boring Stuff with Python 3
#               Ch 13 -  Working with PDF and Word Documents
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
