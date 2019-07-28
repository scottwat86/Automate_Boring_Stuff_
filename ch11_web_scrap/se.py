from selenium import webdriver
import os
browser = webdriver.Firefox(executable_path=os.environ['geckodriver'])
browser.get('http://inventwithpython.com')
try:
  elem = browser.find_element_by_class_name('bookcover')
  print('Found <%s> element with that class name!' % (elem.tag_name))
except:
  print('Was not able to find an element with that name.')

  # Was not able to find an element with that name.
