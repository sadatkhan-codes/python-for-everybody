#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.

# opening file
fname=input('Enter the name of the file: ')
if len(fname)<1:
    fname="regex_sum_2440406.txt"
fhandle=open(fname)

l=list()
l_int=list()

import re
for line in fhandle:
    line=line.rstrip()
    l_string=re.findall('[0-9]+',line)
    if len(l_string)>0:
        for data in l_string:
            l.append(int(data))

print(sum(l))
