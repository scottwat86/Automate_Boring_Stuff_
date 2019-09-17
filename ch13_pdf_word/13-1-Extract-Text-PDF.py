#               Automate the Boring Stuff with Python 3
#               Ch 13 -  Working with PDF and Word Documents
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
