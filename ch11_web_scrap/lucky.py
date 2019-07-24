#! python3
# lucky.py - Opens several Google search results.
# Project: “I’m Feeling Lucky” Google Search
# This code is bugging out
# https://www.reddit.com/r/learnpython/comments/46cdor/automate_the_boring_stuff_chapter_11_feeling_lucky/d045xt5/?context=8&depth=9

import sys, requests, webbrowser, bs4

print('Googling......') # display text while downloading the Google pages
res = requests.get('https://www.google.cz/search?q=Beautiful+Soup' )
res.raise_for_status()

# 'http://google.com/search?q=' + ' '.join(sys.argv[1:])

#  Retrieve top search reult links
soup = bs4.BeautifulSoup(res.text, "lxml")

# # Open a brower tab for each result.
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
print(str(numOpen))################ EMPTY FOR SOME REASON
for i in range(numOpen):
    print('opening' +str(i)) #################
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
