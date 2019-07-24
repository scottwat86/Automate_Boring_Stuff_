#! python3
# lucky.py - Opens several Google search results.
# Project: “I’m Feeling Lucky” Google Search

import requests, sys, webbrowser, bs4

sTerm = 'Beautiful Soup'
print('Googling...') # display text while downloading the Google page
res = requests.get('https://www.google.com/search?q=beautiful+soup')
res.raise_for_status()

# retrieve top search result links
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Open a browser tab for each result
linkElems = soup.select('.r a')
pass

numOpen = min(5, len(linkElems))
print(str(numOpen))################
for i in range(numOpen):
    print('opening' +str(i)) #################
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
