import xml.etree.ElementTree as ET
import urllib.request, urllib.error, urllib.parse

url = input("Enter URL - ")
if len(url) < 1:
    print("Invalid URL")
    quit()

print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)

counts = tree.findall('.//count')

countList = list()
for count in counts:
    countInt = int(count.text)
    countList.append(countInt)

print("Count:", len(countList))
print("Sum:", sum(countList))