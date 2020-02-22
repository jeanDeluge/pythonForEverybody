fhand = open('mbox-short.txt')

FromWhose = []
numberofline=0
for line in fhand:
	line.rstrip()
	if line.startswith('From'):
		numberofline +=1
		newLine = line.split(' ')
		FromWhose.append(newLine[1:2])
		
		

print(FromWhose)
print('There is ', numberofline, 'in the file with From as the fisrt word')