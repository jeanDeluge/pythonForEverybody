# 문제 1 사용자가 'done'을 입력할 때까지 반복해서 숫자를 읽는 프로그램 작성

total = 0
numberOf = 0;
while True:
	number = input('Enter a number:')
	try : 
		userInput = int(number)
		total += userInput
		numberOf += 1
		average = total/numberOf	
		
	except:
		if number == 'done':
			print('Done','Total: ', total, 'NumberOF', numberOf, 'Avergae:' , average)
			break