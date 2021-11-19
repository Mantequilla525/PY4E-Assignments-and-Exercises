import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

iURL = input("Enter URL:")

try:
    hostName = iURL.split("/")[2]
    mysock.connect((hostName, 80))
    cmd = ('GET ' + iURL + ' HTTP/1.0\r\n\r\n').encode()
    mysock.send(cmd)
except:
    print("Invalid URL")
    quit()


while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()