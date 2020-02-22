# 입력 받은 문자의 최대 최소

enteredNumber=[]
total = 0
numberOf = 0;
while True:
	number = input('Enter a number:')
	try : 
		userInput = int(number)
		total += userInput
		numberOf += 1
		average = total/numberOf	
		enteredNumber+= number
	except:
		if number == 'done':
			print('Done','Total: ', total, 'NumberOF', numberOf, 'Avergae:' , average, 'Max', max(enteredNumber), 'Min', min(enteredNumber))
			break
			
			
def max(list):
	largest = None
	for number in list:
		if largest is None or largest < number:
			largest = number
	return largest
		
			
def min(list):
	smallist = None
	for number in list:
		if smallist is None or smallist > number:
			smallist = number
	return largest
		