# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
sum=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    bob=line.find("0")
    n=line[bob:]
    s=float(n)
    sum=sum+s
average=sum/count
print('Average spam confidence:',average)
