#continue 로 반복종료하기

while True:
	line=input('>')
	if line[0] =='#':
		continue
	if line == 'done':
		break
	print(line)
print('done!')