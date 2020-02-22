import socket

try:
	url = input('Enter- ') #http://data.pr4e.org/romeo.txt
	urllist = url.split('/')
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect((urllist[2], 80))
	
except:
	print(url, ' 이 잘못되었습니다.')
	mysock.close()
	

cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
	data = mysock.recv(512)
	if len(data) < 1:
		break
	print(data.decode(),end='')
mysock.close()
