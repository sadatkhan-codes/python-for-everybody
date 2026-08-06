# 10.2 Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then 
# splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname=input('Enter file name:')
if len(fname)<1:
    fname='mbox-short.txt'
fhand=open(fname)

ls=list()
dic=dict()

for line in fhand:
    if line.startswith('From '):
        data=line.split()
        time=data[5]
        hour=time[:2]
        ls.append(hour)
for word in ls:
    dic[word]=dic.get(word,0)+1

for hr in sorted(dic):
    print(hr,dic[hr])