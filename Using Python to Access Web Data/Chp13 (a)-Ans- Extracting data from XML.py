import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 :
   url = 'http://py4e-data.dr-chuck.net/comments_2440410.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
cou=0
sum=0
for result in counts:
   result=int(result.text)
   sum=sum + result
   cou = cou + 1
print('Count:', cou)
print('Sum:', sum)