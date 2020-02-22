strings = input('문자를 입력하시오:')
length = len(strings)
index = length
while index > 0:
	letter = strings[index-1]
	print(letter)
	index -=1
	