#10.2 Write a program to read through the mbox-short.txt and 
#figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then 
#splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname=input('Enter the file name: ')
if len(fname) < 1:
    fname = "mbox-short.txt"
fhandle = open(fname)
d=dict()
l=list()
for line in fhandle:
    if line.startswith('From '):
        words=line.split()
        time=words[5]
        hour=time[0:2]
        l.append(hour)
for h in l:
    d[h]=d.get(h,0)+1

lst=list(d.items())
lst.sort()

for key,val in lst:
    print (key,val)