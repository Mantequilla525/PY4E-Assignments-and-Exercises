import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location:")

print('Retrieving', url)
urlHandle = urllib.request.urlopen(url)

data = urlHandle.read()
print('Retrieved', len(data), 'characters')

data = json.loads(data)

comments = data['comments']

list = list()
for comment in comments:
    list.append(comment['count'])

print('Sum of counts in URL:', sum(list))