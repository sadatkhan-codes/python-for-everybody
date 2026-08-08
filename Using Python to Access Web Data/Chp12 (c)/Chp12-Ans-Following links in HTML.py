# To run this, download the BeautifulSoup zip file and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defauts to certicate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
reqcount=input('Enter count: ')
reqposition=input('Enter position: ')

reqposition=int(reqposition)
reqcount=int(reqcount)

count=-1

while True:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print('Retrieving', url)

    position=0
    tags = soup('a')
    for tag in tags:
        position=position+1
        if position == reqposition:
            url=tag.get('href', None)
            break

    count=count+1
    if count == reqcount:
        break