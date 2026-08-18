fh=open('mbox-short.txt')

for line in fh:
    lx=line.rstrip()
    print(lx.upper())