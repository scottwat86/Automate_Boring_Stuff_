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

import requests, os

# Defines local variable path for Ch11
path = os.environ['python_home'] + '\\Automate_Boring_Stuff_\\ch11_web_scrap\\'

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
playFile = open(path+'RomeoAndJuliet.txt', 'wb') # wb = write binary

for chunk in res.iter_content(100_000): # 100_000 byte chunks to iterate
        playFile.write(chunk)
playFile.close()

#           HTML
# Web Dev Tools Firefox->  CTRL SHIFT C
# DON'T use REGEX for locating HTML CODE

#               BEAUTIFULSOUP OBJECTS
import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup) # bs4.BeautifulSoup
exampleFile = open(path+'example.html') ######### Definie path
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

examplefile = open(path+'example.html')
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
soup = bs4.BeautifulSoup(open(path+'example.html''), 'xml') ######### Definie path
spanElem = soup.select('span')[0]
str(spanElem) #'<span id="author">Al Sweigart</span>'
spanElem.get('id') # 'author'
spanElem.get('some_nonexistent_addr') == None # True
spanElem.attrs #{'id': 'author'}


################
"""
Project: I m Feeling Lucky Google Search
 See ------>lucky.py
 """


################
'''Project: Downloading All XKCD Comics
 See ------>downloadXkcd.py'''

#                       Controlling the Browser with the SELENIUM MODULE

from selenium import webdriver
import os
###########
'''
Tried to debug the env variable problem but wouldn't work. the below is a work around.
'''
browser = webdriver.Firefox(executable_path=os.environ['geckodriver'])
# Alternatively to specifying the executable_path you can copy geckodriver to the python dir
type(browser)
browser.get('http://inventwithpython.com')


#               Finding Elements on the Page
#          METHOD                                                            WEBELEMENT OBJECT / LIST RETURN

#           browser.find_element_by_class_name(name)     Elements that use the class
#           browser.find_elements_by_class_name(name)   class name

#           browser.find_element_by_css_selector(selector)  Elements that match the CSS selector

#           browser.find_element_by_id(id)                             Element with a matching id attribute value

#           browser.find_by_link_text(text)                             <a> elements that completely match the text provided

#           browser.find_element_by_partial_link_text(text)     <a> elements that contain the text provided

#           browser.find_element_by_name(name)                      Elements with a matching name attribute value

#           browser.find_element_by_tag_name(name)              Element with matching tag name
#                                                                                               (case insensitive; an <a> element is
#                                                                                                 matched by 'a' and 'A')

#               Except for the *_by_tag_name() methods, the arguments to all
#               these methods are case sensitvie

#               NoSuchElement exception is raised if nothing is found


#           WEBELEMENT ATTRIBUTES / METHODS
#       ATTRIBUTE / METHOD       DESCRIPTION

#       tag_name                                tag name, such as 'a' for an <a> element
#       get_attribute(name)                value for the element's name attribute
#       text                                          text within the element, such as 'hello' in <span>hello</span>
#       clear()                                     text field or text area elements, clears the text typed into it
#       is_displayed()                         Returns True if the elements is visible; otherwise returns False
#       is_enabled()                            for input elements, return True if the element is enabled; otherwise returns False
#       is_selected()                           for checkbox or radio button elements, returns True if the element is selected; otherwise return False
#       location                                  Dictionary w keys 'x' and 'y' for the position of the element in the page

from selenium import webdriver
browser = webdriver.Firefox(executable_path=os.environ['geckodriver'])
browser.get('http://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Automate the Boring Stuff with Python')
type(linkElem) # selenium.webdriver.firefox.webelement.FirefoxWebElement
linkElem.click() # follows the "Read it online link"
browser.quit()

#                   Filling Out and Submitting Forms
from selenium import webdriver
browser = webdriver.Firefox(executable_path=os.environ['geckodriver'])
url = 'https://login.yahoo.com/?.src=ym&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd'
browser.get(url)
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('email@yahoo.com')
emailElem.submit()
buttonElem = browser.find_element_by_id('login-signin')
buttonElem.submit()
passwordElem = browser.find_element_by_id('login-passwd')
passwordElem.send_keys('password')
buttonElem = browser.find_element_by_id('login-signin')
buttonElem.click()
browser.quit()

# The above was revised as the old code from the book didnt work as is
# as yahoo has moved to a two page login


#                       Sending Special Keys
#           Keys.Down, Keys.LEFT, Keys.RIGHT                               keyboard arrow Keys
#           Keys.ENTER, Keys.RETURN                                            Enter and Return Keys
#           Keys.HOME, Keys.END, Keys.PAGE_DOWN                 Home, end, pagedown, and pageup keys
#           Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE       ESC, BACKSPACE, and DELETE
#           Keys.F1, Keys.F2, ... Keys.F12                                        F1 - F12
#           Keys.TAB                                                                         Tab Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)        # scolls to bottom
htmlElem.send_keys(Keys.HOME)     # scolls to top


#               Clicking Browser Buttons
#           browser.back()             click the back button
#           browser.forward()       click the forward button
#           browser.refresh()         click the refresh / reload button
#           browser.quit()              clic the close window button

#               PRACTICE QUESTIONS
#           1)  webbrowser - has open() method that can lauch firefox to a URL
#               requests - can download files from the web
#               BeautifulSoup - parses HTML
#               selenium - can launch and control the browser
#           2)
import requests
response = requests.get(url)
type(response)  #requests.models.Response
response.text
#           3)
response.status_code # 200 -> successful
#           4)
response.status_code #200
#           5)
file = open(new_file, 'wb') # write binary
for chunk in response.iter_content(100_000): #100_000 bytes
    file.write(chunk)
file.close()
#           6)  CTRL-SHIFT-C
#           7) Right click and inspect element
#           8)
soup.select('#main')
#           9)
 soup.select('.highlight')
#           10)
soup.select('div div')
#           11)
soup.select('input[type="favorite"]')
#           12)
spam.getText()
#           13)
linkElem.attrs
#           14)
from selenium import webdriver
#           15)
#find_element_*    returns first match as WebElement object
#find_element_*   returns a list of all element as WebElement object
#           16)
inkElem = browser.find_element_by_link_text('Automate the Boring Stuff with Python')
linkElem.click()

#           17)
emailElem = browser.find_element_by_id('login-username')
emailElem.send_keys('email@yahoo.com')
emailElem.submit()
#           18)
browser.back()
browser.forward()
browser.refresh()
