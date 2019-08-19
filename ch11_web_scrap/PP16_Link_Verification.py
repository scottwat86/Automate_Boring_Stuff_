#! python3
#  Practice Project 16 - Link Verification

# By Scott Watson

import requests, sys, re, logging
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

logging.basicConfig(level=logging.DEBUG,
                                  format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)  # Logg"ing disabled

def link_retriever(url):
    """
    Takes input url and retrieves all http(s) links from the input website. Each link is tested for
    200 and 404 status codes and seperated in to two list. All other status code are saved to third list

    Returns a list of of lists
    """

    # Stackoverflow solution for max retries exceeded error
    #https://stackoverflow.com/questions/23013220/max-retries-exceeded-with-url-in-requests?rq=1
        # This will GET the URL and retry 3 times in case of requests.exceptions.ConnectionError.
        # backoff_factor will help to apply delays between attempts to avoid to fail again in case of
        # periodic request quota.
    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # Retrieving url html to parse
    website = session.get(url)
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
        print(".", end='')
        website = session.get(links[i])
        website.raise_for_status()

        #Separates links by status code into lists
        if website.status_code == 404:
            bad_links.append(links[i])
        elif website.status_code == 200:
            active_links.append(links[i])
        else:
            error.append(links[i])

    return active_links, bad_links, error

################# - END OF DEF - ##################

# Retrieves URL from command line

try:
    script, url = sys.argv
    logging.debug('Initializing Argument Finished')
except:
    print("\n*************\n\nScript takes one url as an argument!\n\n*************\n")
    print("Please try again later.")
    quit()

# Seperates the three lists for printing
all_links = link_retriever(url)
good = all_links[0]
bad = all_links[1]
evil = all_links[2]

# Prints the results
print("\n\nGood Links:")
for i in good:
    print(i)
print("*****************\n")

print("Bad Links:")
for i in bad:
    print(i)
print("*****************\n")

print("Evil  Links:")
for i in evil:
    print(i)
print("*****************\n")


"""
INPUT ARGV
url = https://www.datacamp.com

OUTPUT:

Good Links:
https://www.datacamp.com/pricing
https://www.datacamp.com/groups/business
https://www.datacamp.com/groups/education
https://www.datacamp.com/users/sign_up
https://www.datacamp.com/users/sign_in
https://www.datacamp.com/onboarding/learn?from=home
https://www.datacamp.com/terms-of-use
https://www.datacamp.com/privacy-policy
https://www.datacamp.com/users/sign_in
https://www.datacamp.com/users/sign_up
*****************

Bad Links:
*****************

Evil  Links:
*****************
"""
