import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL - ")
count = int(input("Enter count - "))
pos = int(input("Enter position - "))

for i in range(0, count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    cont = 0

    for tag in tags:
        cont += 1

        if cont > pos:
            break
        url = tag.get('href', None)
        name = tag.contents[0]

print(name)