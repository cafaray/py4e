import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET 

url = input('Url de inicio:')
if len(url) <= 0:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
print('Enter location:', url)
pageXml = urllib.request.urlopen(url).read() 
print('Retrieving ', url)

stuff = ET.fromstring(pageXml)
lst = stuff.findall('.//count')
print('Count:', len(lst))
suma = 0
for elem in lst:  
    try:  
        suma = suma + int(elem.text)
    except:
        print('I can not recognize a number in this element:',elem.text)
print('Sum:', suma)