#               Automate the Boring Stuff with Python 3
#               Chapter 11 – Web Scraping

#   WEB SCRAPING is the term for using a program to download and process content from the Web
#   webbrowser - opens a browser to a specific page
# Requests - Downloads files and web pages from the Internet
# Beautiful Soup - Parses HTML for webpages
# Selenium - Lauches and controls a web browser. Is able to fill in forms and simulate mouse clicks

#           WEBBROWSER MODULUE
#           SEE Project: mapit.py

#           REQUEST MODULE
# Downloading Files from the Web
# Always call raise_for_status() after calling requests.get().

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res) # requests.models.Response

res.status_code == requests.codes.ok # True
len(res.text) # 178,978 char long

print(res.text[:250])
'''
The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Projec
'''
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status() # HTTP ERROR raised
except Exception as exc:
    print('There was a problem: %s' % (exc))
    # There was a problem: 404 Client Error: Not Found for url: http://inventwithpython.com/page_that_does_not_exist

# Saving Downloaded Files to the Hard Drive

import requests, os

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status() # Checks if get was sucessful
playFile = open('RomeoAndJuliet.txt', 'wb') # wb = write binary

for chunk in res.iter_content(100_000): # 100_000 byte chunks to iterate
        playFile.write(chunk)
playFile.close()

#           HTML
# Web Dev Tools Firefox->  CTRL SHIFT C
# DON'T use REGEX for locating HTML CODE

#               BEAUTIFULSOUP OBJECTS
import requests, bs4
path = '.\\example.html'
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup) # bs4.BeautifulSoup
os.chdir(./A)
exampleFile = open(path) ######### Definie path
exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")
type(exampleSoup)


#               CSS SELECTORS
# Cascading Style Sheet (MIME) is a plain text file format used for formatting content on web pages.
#  The below selector patterns can be combined to form complex matching
#   select() returns a TAG object which is how bs4 represents HTML. TAG obj can be passed to str
# Tag obj also have attrs which contains HTML attrs

#       soup.select('div')                All elements named 'div'
#       soup.select('#author')        Element with an id attribute of author
#       soup.select('.notice')          All elements that use CSS class attr named notice
#       soup.select('div span')        All elements names <span> that are within an element <div>
#       soup.select('div > span')    All elements named <span> that are directly within an ele <div>.
#                                                   with no other elements in between

#     soup.select('input[name]')    All elements named <input> that have a name attr with any value

#     soup.select('input[type="button"]')   All elements named <input> that have an attr named type
#                                                                  with value button

import bs4

examplefile = open(path) ######### Definie path
myfile=examplefile.read()
examplesoup = bs4.BeautifulSoup(myfile, 'html.parser')
elems = examplesoup.select('#author')
type(elems) #list
len(elems) # 1
type(elems[0]) #bs4.element.Tag
elems[0].getText() #'Al Sweigart' #returns the element’s text, or inner HTML.
str(elems[0]) #'<span id="author">Al Sweigart</span>'
elems[0].attrs #{'id': 'author'}

pElems = examplesoup.select('p')
str(pElems[0])
#'<p>Download my <strong>Python</strong> book from
#<a href="http://\ninventwithpython.com">my website</a>.</p>'
pElems[0].getText()
# 'Download my Python book from my website.'
str(pElems[1])
#'<p class="slogan">Learn Python the easy way!</p>'
pElems[1].getText()
#'Learn Python the easy way!'
str(pElems[2])
'''
[<p>Download my <strong>Python</strong> book from <a href="http://
 inventwithpython.com">my website</a>.</p>,
 <p class="slogan">Learn Python the easy way!</p>,
 <p>By <span id="author">Al Sweigart</span></p>]
'''
pElems[2].getText()
#'By Al Sweigart'

#       Getting Data from an Element’s Attributes
import bs4
soup = bs4.BeautifulSoup(open(path), 'xml') ######### Definie path
spanElem = soup.select('span')[0]
str(spanElem) #'<span id="author">Al Sweigart</span>'
spanElem.get('id') # 'author'
spanElem.get('some_nonexistent_addr') == None # True
spanElem.attrs #{'id': 'author'}


# ###############
'''Project: “I’m Feeling Lucky” Google Search
 See ------>lucky.py'''
################


# ###############
'''Project: Downloading All XKCD Comics
 See ------>downloadXkcd.py'''
################

#                       Controlling the Browser with the SELENIUM MODULE



path = 'C:\\Users\\scott_watson\\Documents\\Python\\Automate_Boring_Stuff_\\ch11_web_scrap\\example.html'
