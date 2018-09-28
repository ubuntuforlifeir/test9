import requests
import json
import os
import regex
from bs4 import BeautifulSoup
url = requests.get('https://newahang.com')
soup = BeautifulSoup(url.content,'xml')
for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['herf'])