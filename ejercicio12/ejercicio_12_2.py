import urllib.request, urllib.parse, urllib.error
import json 

url = input('Url de inicio:')
if len(url) <= 0:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'
print('Enter location:', url)
pageJson = urllib.request.urlopen(url).read() 
print('Retrieving ', url)
print('Reading', len(pageJson),'characters')

js = json.loads(pageJson)
#print(json.dumps(js, indent=4))

lst = list()
lst = js['comments']
suma = 0
for item in lst:
    #print(item['count'])
    suma = suma + int(item['count'])

print('elementos:', len(lst))
print('suma:', suma)
