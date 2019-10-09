import requests
from bs4 import BeautifulSoup, NavigableString, Tag 
import re

url = 'https://access.redhat.com/articles/3078'
rhelpage = requests.get(url)

#print(response)
soup = BeautifulSoup(rhelpage.content, 'html.parser')

#find the element header "Red Hat Enterprise Linux 7" and then extract the table right after it
for header in soup.find_all('h1', text=re.compile('Red Hat Enterprise Linux 7')):
    nextNode = header
    while True:
        nextNode = nextNode.nextSibling
        if nextNode is None:
            break
        if isinstance(nextNode, Tag):
            if nextNode.name == "h1":
                break
            print(nextNode)

