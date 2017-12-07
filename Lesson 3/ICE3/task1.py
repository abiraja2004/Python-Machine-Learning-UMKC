import requests
from bs4 import BeautifulSoup
import os
url = 'https://en.wikipedia.org/wiki/Pakistan'
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, 'html.parser')
result = soup.findAll('div')
print(soup.h1.string)
#for div in result:
#    R1 = div.find('h1')
print(soup.body.text)