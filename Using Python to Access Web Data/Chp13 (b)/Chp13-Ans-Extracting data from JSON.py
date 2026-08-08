import json
import urllib.request

url = input('Enter - ')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/comments_2440411.json'

uh = urllib.request.urlopen(url)
print('Retrieving URL', url)

data = uh.read()
print(len(data))

info = json.loads(data)

print(info)   # Just to check what kind of data is there in info

cou=0
sum=0

comments=info['comments']

for comment in comments:
    num=int(comment['count'])
    cou=cou+1
    sum=sum+num
print('Count is',cou)
print('Sum is', sum)