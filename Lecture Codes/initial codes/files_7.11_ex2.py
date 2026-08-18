fname = input("Enter file name: ")
fh = open(fname)
count=0
val=0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        b=line[20:]
        b=float(b)
        val=val+b
print("Average spam confidence:",val/count)
