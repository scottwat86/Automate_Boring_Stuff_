#! python3
#               Automate the Boring Stuff with Python 3
#               Ch 13 -  Working with PDF and Word Documents
# 13-P-Combine-Pages-PDFs.py - Project: Combining Select Pages from Many PDFs

import os
import PyPDF2

# Get all PDFs files in CWD
pdfFiles = []
for file in os.listdir('.'):
    if file.endswith('.pdf'):
        pdfFiles.append(file)

# Sort the PDF filenames
pdfFiles.sort(key=str.lower)

# Write each page, excluding the first page, of each PDF to the ouput file
pdfWriter = PyPDF2.PdfFileWriter()

# Loop over each PDF file to creat PdfFileReader object
for file in pdfFiles:
    pdfFileObj = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
