#               Automate the Boring Stuff with Python 3
#               Ch 13 -  Working with PDF and Word Documents
# Decrypting PDFs

import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted # True
# pdfReader.getPage(0)
pdfReader.decrypt('rosebud') # 1
pageObj = pdfReader.getPage(0)
