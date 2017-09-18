#import socket

#mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysocket.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()
#mysocket.send(cmd)

#while True:
#    data = mysocket.recv(512)
#    if(len(data)<1):
#        break
#    print(data.decode())
#mysocket.close()

import urllib.request, urllib.parse, urllib.error

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhandle:
    print(line.decode().strip())