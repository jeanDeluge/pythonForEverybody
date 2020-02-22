
#c출력 문자가 3000개에 이르면 중단시키도록 함
import socket

try:
	url = input('Enter- ') #http://data.pr4e.org/romeo.txt
	urllist = url.split('/')
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect((urllist[2], 80))
	
	count = 0
	doc= ''

	cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
	mysock.send(cmd)

	while True:
		data = mysock.recv(3000)
		if len(data) < 1:
			break
		count = count + len(data)
		doc = doc + data
		mysock.close()		
		print(data.decode(),end='')
except:
	print(url, ' 이 잘못되었습니다.')
	mysock.close()
	
