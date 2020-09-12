name = input("Enter file:")
handle = open(name)
d=dict()
ls=list()
for line in handle:
    a=line.split()
    if len(a) == 0: continue
    if a[0] != "From:": continue
    ls.append(a[1])

for email in ls:
    if email not in d:
         d[email]=1
    else:
         d[email] = d[email] +1

bigcount = None
bigword=None
for word , count in d.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count

print (bigword, bigcount)
