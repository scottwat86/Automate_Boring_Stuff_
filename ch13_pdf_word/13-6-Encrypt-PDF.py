#               Automate the Boring Stuff with Python 3
#               Ch 13 -  Working with PDF and Word Documents
# Encrypting PDFs

import PyPDF2
#Opens the input file
pdfFile = open('meetingminutes.pdf', 'rb')

#Creates pdfReader and pdfWriter objects
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

# Goes through every page pdfReader and adds it to the PdfFileWriter object
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

'''The user password and owner password are the first and second arguments to encrypt()'''
password = 'swordfish'
pdfWriter.encrypt(password) # encrypts the pdf object
resultPdf = open('encryptedminutes.pdf', 'wb') # Creates new file
pdfWriter.write(resultPdf) # Writes the encrypted file to resultPdf
resultPdf.close()
pdfFile.close()
