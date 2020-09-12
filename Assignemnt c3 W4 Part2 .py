url = input("Enter URL:")
count = int(input("Enter Count:"))
pos = int(input("Enter Position:"))
lst = list()
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#RUNNING THE FIRST html

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
for i in range(count):
    lst.append(tags[pos].get('href', None))
#REPEATED ITERATIONS OF ABOVE code3

#while count != 0 :
#    html = urllib.request.urlopen(lst[pos], context=ctx).read()
#    soup = BeautifulSoup(html, 'html.parser')
#    tags = soup('a')
#    for tag in tags:
#        lst.append(tag.get('href', None))
