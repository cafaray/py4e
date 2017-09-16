import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
#import ssl

#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = 'http://py4e-data.dr-chuck.net/comments_27267.html'
html = urllib.request.urlopen(url).read()  # , context=ctx
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
numbers = list()
for tag in tags:
    #print('TAG', tag)
    try:
        iNumber = int(tag.contents[0])
        numbers.append(iNumber)
    except:
        print('El tag no contiene un numero:',tag.contents[0])
        continue
    # print('Contents:',tag.contents[0])

print(sum(numbers))