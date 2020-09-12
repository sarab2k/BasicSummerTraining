fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    n=line.strip()
    h=n.upper()
    print(h)
