#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers. 
#You will extract all the numbers in the file and compute the sum of the numbers.

import re

fname=input('Enter file name:')
if len(fname)<1:
    fname='regex_sum_2440406.txt'
fhand=open(fname)

l_string=list()
l=list()
for line in fhand:
    l_string=re.findall('[0-9]+',line)
    if len(l_string)>0:
        for data in l_string:
            data=int(data)
            l.append(data)
print(sum(l))