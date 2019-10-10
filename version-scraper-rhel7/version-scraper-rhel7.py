import requests
from bs4 import BeautifulSoup, NavigableString, Tag 
import re

url = 'https://access.redhat.com/articles/3078'
rhelpage = requests.get(url)

soup = BeautifulSoup(rhelpage.content, 'html.parser')

table = soup.find_all('table')[1]

rhel7version = table.find_all('td')[3].get_text()

print(rhel7version)
