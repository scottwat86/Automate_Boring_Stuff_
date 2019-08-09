#! python3
#  Practice Project 13 - Command Line Emailer

# By Scott Watson

from selenium import webdriver
import sys, time, logging

logging.basicConfig(level=logging.DEBUG,
                                  format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)  # Logging disabled

script, username, password, *body = sys.argv
wait = 0.1  # Wait period in seconds to slow the HTTP requests
url = 'https://login.yahoo.com/' # Defining URL
logging.debug('Assigning Username, Password, and Body arguments to variables')

browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.get(url) # Opens url
time.sleep(wait) #slows the program to prevent web server blocking selenium
logging.debug('URL opened in browser')

# USERNAME AND NEXT PAGE
userElem = browser.find_element_by_id('login-username').send_keys(username)
buttonElem = browser.find_element_by_id('login-signin').click() # submit user name
time.sleep(wait)
logging.debug('Username box selected and email entered and submit')

# PASSWORD AND LOGIN
# Submit was working but now this needs a selection then click()
passElem = browser.find_element_by_id('login-passwd').send_keys(password)
buttonElem = browser.find_element_by_id('login-signin').click()
time.sleep(wait)
logging.debug('Password select box, password enter, and submit')


# NAVIGATING PAGE
mailLink = browser.find_element_by_id('uh-mail-link').click()
time.sleep(wait) #slows the program to prevent web server blocking selenium
composeLink = browser.find_element_by_link_text('Compose').click()
time.sleep(wait)
logging.debug('Navigated to the compose email page')


# COMPOSING EMAIL AND SENDING
# There was some diffiuclty selecting the text boxes for subject and body
# See https://selenium-python.readthedocs.io/waits.html for solution

# Filling out the Email to box
email_to = browser.find_element_by_id('message-to-field').send_keys(username)
# Filling out Subject Line
subject_text = browser.find_element_by_css_selector('input.q_T:nth-child(1)').send_keys('test')
# Filling out Body Line
body_text = browser.find_element_by_css_selector('.rte').send_keys('This is only a test')
# Send the email
browser.find_element_by_css_selector(".q_Z2aVTcY").click()
logging.debug('Email prepared and sent')

# CLEAN UP
browser.quit()
