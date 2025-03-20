# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
    
# mysock.close()

# import urllib.request, urllib.parse, urllib.error

# file_handler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in file_handler:
#     print(line.decode().strip())
    
    
# import urllib.request, urllib.parse, urllib.error
# file_handler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# often_words = dict()
# for line in file_handler:
#     words = line.decode().split()
#     for word in words:
#         often_words[word] = often_words.get(word, 0) + 1
        
# print(often_words)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
