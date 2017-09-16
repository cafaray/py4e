import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Url de inicio: ')
strCount = input('Iteraciones: ')
strPosicion = input('Posicion:')
try:
    intCount = int(strCount)
    intPosicion = int(strPosicion)
except:
    print('invalid input')
    quit()

#url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

count = 1
while True:
    html = urllib.request.urlopen(url).read() 
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    position = 1
    for tag in tags:
        if position==intPosicion:
            url = tag.get('href', None)
            print(count, url)
        position = position + 1
    if count == intCount: break
    count = count + 1
initPosition = url.find('_by_') + 4
lastPosition = url.find('.htm')
print(url[initPosition:lastPosition])