#1 파일을 읽고 그 내용을 한 줄씩 대문자로 변환해 출력하는 프로그램을 만들어보자.
fname = input('Enter the file name:')
try:
	fhand = open(fname)
	for line in fhand:
		upperWord = line.upper()
		print(upperWord)
	
	
except:
	print('try again')
	exit()
	