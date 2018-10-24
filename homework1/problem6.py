import requests
import time
import sys
from bs4 import BeautifulSoup

out = ''
path = ''

# download the 1st page
url = 'https://www.kijiji.it/offerte-di-lavoro/offerta/informatica-e-web/'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

# get the total number of pages
last_page = int(soup.body.find('a','last-page').text)

# check if output file name was given as argument
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = 'output.tsv'

# function that parses a page of offers
def parse_offers(soup):
    global out
    offers = soup.find_all('li','result')
    for offer in offers:
        if 'treebay-ad' in offer['class']:
            continue
        out += offer.find('a','cta').text.strip() + '\t'
        out += offer.find('p','description').text.replace('\n',' ').strip() + '\t'
        out += offer.find('p','locale').text.strip() + '\t'
        out += offer.find('p','timestamp').text.strip() + '\t'
        out += offer.find('a','cta')['href']
        out += '\n'

# parse every page of offers
sys.stdout.write("Page 1 out of %s\r" % (last_page) )
sys.stdout.flush()
parse_offers(soup)
for page in range(2,last_page+1):
    time.sleep(0.5)    
    sys.stdout.write("Page %s out of %s\r" % (page,last_page) )
    sys.stdout.flush()
    html = requests.get(url+'?p='+str(page)).content
    soup = BeautifulSoup(html, 'html.parser')
    parse_offers(soup)

# write offers to .tsv file    
print '\nWritting to file ...'
text_file = open(path, "w")
text_file.write(out.encode('utf-8'))
text_file.close()

print 'Done!'