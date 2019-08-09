#! python3
#  Practice Project 14 - IMAGE SITE DOWNLOADER

# By Scott Watson

from bs4 import BeautifulSoup
import time, sys, os, re, requests, logging

# Set up logging
logging.basicConfig(level=logging.DEBUG,
                                  format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)  # Logging disabled

# Initiate variables
#scrrpt, *find_this = sys.argv
find_this = 'cats'
url_search = 'https://www.flickr.com/search/?text='

environment = os.environ.get('python_home') # Anaconda is having trouble locating env variables!
dir_path = environment + '\\Automate_Boring_Stuff_\\ch11_web_scrap\\save_here'

os.chdir(dir_path)
logging.debug('Variables Initilized')

# Conduct request to search for find_this
search = requests.get(url_search + find_this)
search.raise_for_status() # Checks for errors during the request
logging.debug('HTML Request Successful')

# Builds bs4 object to parse HTML
soup = BeautifulSoup(search.text, 'html.parser')
image_HTML = soup.find_all('div',  class_=
                                                         "view photo-list-photo-view requiredToShowOnServer awake")
logging.debug('Soup Object Successful')

# Regex to get link from style='...url()'
"""The parsering of the links probably could be done better then this hard coding!"""
regex_URL = re.compile(r'(/\w*)(\.\w*\.\w*/\d*/\d*_.*_.*\.jpg)')
image_links = regex_URL.findall(str(image_HTML))
logging.debug('Parsing HTML Successful')
# /live.staticflickr.com/3064/2434899664_cf1ccc308f_m.jpg

# Flickr tags explained
#https://www.flickr.com/services/api/misc.urls.html
#

# Tag
# https://farm1.staticflickr.com/2/1418878_1e92283336_m.jpg
#farm-id: 1
#server-id: 2
#photo-id: 1418878
#secret: 1e92283336
#size: m

logging.debug('For Loop to request files, number, and save')
for i in range(len(image_links)):

    image_id = image_links[i][1]
    file_name = find_this + str(i+1) + '.jpg'
    image_url = 'https://farm1' + image_id
    print(image_url)
    image = requests.get(image_url)
    time.sleep(0.25)

    with open(file_name, 'wb') as f:
        for chunk in image.iter_content(100_000):
            f.write(chunk)
        print('file saved')

print('Done\n\n',f'Total of {i+1} files saved' )
