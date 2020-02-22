fhand = open('mbox-short.txt')

hourClock = dict()
hourSave=list()
for line in fhand:
	if not line.startswith('From'):
		continue
	else:
		words = line.split()
		try:
			timer_ex = words[5].split(':')
			hourSave.append(timer_ex[0])
		except:
			continue

numberOfhour = list()

for hour in hourSave:
	if hour not in hourClock:
		hourClock[hour] = 1 
	else :
		hourClock[hour]+=1
	
for key , val in list(hourClock.items()):
	numberOfhour.append((key, val))


numberOfhour.sort()

for hour, number in numberOfhour:
	print(hour,number)