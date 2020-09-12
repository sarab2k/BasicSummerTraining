import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import urllib

sum=0
url = input('Enter url:')
uh = urllib.request.urlopen(url)
xmldata = uh.read()
pydata = ET.fromstring(xmldata)
lst = pydata.findall('./comments/comment')
for item in lst:
    count= item.find('count').text
    intcount=int(count)
    sum=sum+intcount
print(sum)
