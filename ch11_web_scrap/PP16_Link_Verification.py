#! python3
#  Practice Project 16 - Link Verification

# By Scott Watson

from bs4 import BeautifulSoup
import requests, time, os, re, logging
# import os, re,

logging.basicConfig(level=logging.DEBUG,
                                  format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)  # Logg"ing disabled

def link_retriever(url):
    """
    Takes input url and retrieves all http links from the input website. Each link is tested for
    200 and 404 status codes and seperated in to two list. All other status code are saved to third list

    Returns a list of active 200 status code by default
    Set ReturnList to False to return a generator of same links
    """
    # Retrieving url html to parse
    website = requests.get(url)
    website.raise_for_status() # Checks for errors during the request
    logging.debug('HTML Request Successful')

    # Initiating some empty lists to hold links
    links = [] # All Links
    active_links = [] # 200 code links
    bad_links =[] # 404 code Links
    error = [] # All the other codes

    #Finding base url for relative path links
    base = re.compile(r"http\w?://\w*\.?\w+\.\w+")
    base_url = base.findall(url)[0]
    logging.debug('Extracting base url')

    # Parse the HTML for href
    soup = BeautifulSoup(website.text, "html.parser")
    for a in soup.find_all('a', href=True, text=True):
        # Stripping external urls
        if a['href'].find('https://') == 0 or  a["href"].find('http://') == 0:
            links.append(a['href'])
        # Stripping out relative path urls
        else:
            links.append(base_url+a['href'])
        logging.debug('Parseing links from HTML')

    # Tests if each link is active
    for i in range(len(links)):
        time.sleep(3)
        website = requests.get(links[i])
        website.raise_for_status()

        #Separates links by status code into lists
        if website.status_code == 404:
            bad_links.append(links[i])
        elif website.status_code == 200:
            active_links.append(links[i])
        else:
            other.append(links[i])

    yield active_links

    #
    # if ReturnList == True:
    #     return active_links
    # else:
    #     yield active_links
################# - END OF DEF - ##################

# try:
#     script, url = sys.argv
# except:
#     print("Script takes one argument which should be a url. Please try again")
# logging.debug('Initializing Argument Finished')

url = "https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/"

# File system path
env = os.environ.get('python_home')
path = env + '\\Automate_Boring_Stuff_\\ch11_web_scrap\\save_here'
os.chdir(path)
logging.debug('Changed the directory to the directory to save urls to.')

next(link_retriever(url))
