import urllib.request, urllib.parse, urllib.error
import json
import ssl

dic=dict()
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum=0
url = input("Enter:-")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
js = json.loads(data)
print(js)
c = js["comments"]
for item in c:
    sum = sum + int(item ['count'])
#print(sum)
