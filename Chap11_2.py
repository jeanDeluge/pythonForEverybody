import re
fname = input('Enter file: ')


try:
	fhand = open(fname)
except:
	print('try again', fname , 'is not exist')

sum=0
numberOfLine=0
for line in fhand:
	line.rstrip()
	number = re.findall('^New\sR.*:\s([0-9]+)', line)
	if len(number)>0:
		numberOfLine+=1
		for n in number:
			sum += float(n)
			

print(sum/numberOfLine)