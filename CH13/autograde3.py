import urllib.request, urllib.parse, urllib.error
import json

serviceUrl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter address - ')

parameters = dict()
parameters['address'] = address
parameters['key'] = '42'
url = serviceUrl + urllib.parse.urlencode(parameters)

print('Retrieving', url)

urlHandle = urllib.request.urlopen(url)

data = urlHandle.read()
data = json.loads(data)

for result in data['results']:
    print('Place ID:', result['place_id'])