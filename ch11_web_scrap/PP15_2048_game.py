#! python3
#  Practice Project 1 - 2048 Game

# By Scott Watson

# IMPORTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

#OPEN BROWSER
url = 'https://gabrielecirulli.github.io/2048/'
browser = webdriver.Firefox()
browser.get(url)

# Selecting the html to interact with using the keyboard
game_element = browser.find_element_by_tag_name('html')

# LIST GAME OPTIONS
controls = [r'Keys.UP', r'Keys.RIGHT', r'Keys.DOWN', r'Keys.LEFT']

# LOOP TO ENTER GAME MOVES

# Originally had a double for loop but the game was reseting the score after RIGHT
# I found the below on stackoverflow and tweaked
while True:
    game_element.send_keys(Keys.UP)
    game_element.send_keys(Keys.RIGHT)
    game_element.send_keys(Keys.DOWN)
    game_element.send_keys(Keys.LEFT)
    time.sleep(0.1)

# SHUT DOWN RESOURCES
browser.close()
