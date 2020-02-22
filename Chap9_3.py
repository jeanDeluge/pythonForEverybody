#3, #4 번문제
#3
fhand = open('mbox.txt')

mailAdress = dict()
for line in fhand:
	line.rstrip()
	if not line.startswith('From'):
		continue
	words = line.split()
	if not words[1] in mailAdress:
		mailAdress[words[1]] = 1
	else:
		mailAdress[words[1]] += 1
print(mailAdress)	

#4
min = 100
max = 0
for key in mailAdress :
	if mailAdress[key] >= max:
		max = mailAdress[key]
	if mailAdress[key] <= min:
		min = mailAdress[key]


for key in mailAdress :
	if mailAdress[key] == max:
		print('max', key, mailAdress[key])
	elif mailAdress[key] == min:
		print('min', key, mailAdress[key])
	else : continue	
