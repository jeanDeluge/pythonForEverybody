import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo-full.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
data = ''
while True :
	data = mysock.recv(512)
	if len(data) < 1: break
	print(data.decode())
mysock.close()


#헤더의 끝을 찾기
pos = data.decode().find('\r\n\r\n')+4 
print('Header length', pos)
