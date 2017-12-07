import requests
from bs4 import BeautifulSoup
import os
url = 'https://en.wikipedia.org/wiki/Pakistan'
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')
h1 = soup.find_all('h1')
print(h1)
body = soup.find_all('body')
print(body)
#for div in result:
#    R1 = div.find(‘h1’)
#body = soup.find('div', {'class': 'mw-parser-output'})

#for link in soup.find_all('a'):
#    print(link.get('href'))
#print(soup.find_all('header'))