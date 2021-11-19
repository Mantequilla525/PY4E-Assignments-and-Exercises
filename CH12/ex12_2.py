import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

countedChars = 0
while True:
    data = mysock.recv(512)
    countedChars += len(data)
    if countedChars < 3000:
        print(data.decode())
    if len(data) < 1:
        break

mysock.close()
print("Counted characters:", countedChars)