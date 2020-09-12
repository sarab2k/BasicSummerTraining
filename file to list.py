fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
      b=line.split()
      for word in b:
          if not word in lst:
               lst.append(word)
lst.sort()
print(lst)
