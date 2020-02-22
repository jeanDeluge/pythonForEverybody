fhand = open('mbox-short.txt')

newLine = []
dayList = { 'Mon' : 0 , 'Tue': 0, 'Wed' : 0, 'Thu' : 0, 'Fri':0, 'Sat' : 0, 'Sun' : 0 }
for line in fhand:
	line.rstrip()
	if line.find('From') ==-1: 
		continue
	else:
		newLine.append(line.split(' '))


for line in newLine:
	for word in line:
		for key in dayList.keys():
			if word == key:
				dayList[key] += 1
print(dayList)