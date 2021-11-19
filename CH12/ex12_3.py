import socket
import urllib.request, urllib.parse, urllib.error

iURL = input("Enter URL:")

fh = urllib.request.urlopen(iURL)

charCount = 0
for line in fh:
    line = line.decode().strip()
    for char in line:
        charCount += 1
        if charCount < 3000:
            print(char)

print(charCount)