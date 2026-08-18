# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
try:
    fhand=open(name)
except:
    print('The file',name, 'is not found')
    exit()
    
dic=dict()
lis=list()

for line in fhand:
    line.rstrip()
    if line.startswith('From '):
        data=line.split()
        lis.append(data[1])
        
for word in lis:
    dic[word]=dic.get(word,0)+1
    
bigword=None
bigcount=None
for w,c in dic.items():
    if bigcount is None or c>bigcount:
        bigcount=c
        bigword=w
print(bigword,bigcount)
