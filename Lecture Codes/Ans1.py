# This program is answer to a question which is in the format of an image in code3 with file name Q1(Ans1).png

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

reqcount=input('Enter count: ')
reqposition=input('Enter position: ')
reqposition=int(reqposition)
reqcount=int(reqcount)

count=-1

while (True):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print('Retrieving', url)
    tags = soup('a')

    position=0
    for tag in tags:
        position=position+1
        if position == reqposition:
            url = tag.get('href', None)
            break
    
    count=count+1
    if count == reqcount:
        break
