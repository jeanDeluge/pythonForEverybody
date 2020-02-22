fname = input('Enter the file name:')

try:
	fhand = open(fname)
		
except:
	print('try again')
	exit()

total =0
average =0
count = 0
for line in fhand:
	wantedline = line.startswith('X-DSPAM-Confidence')
	if wantedline == False:
		continue
	else:
		count += 1
		first =line.find(' ')
		last = line.find("'",first)
		total += float(line[first+1:last])

average = total/count
print('Average spam confidence', average)