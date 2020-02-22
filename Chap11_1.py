import re
fhand = open('mbox.txt')

regularEX = input('Enter a regular expression')

numberOfline = 0

for line in fhand:
	line = line.rstrip()
	if re.search(regularEX, line):
		numberOfline+=1

print(numberOfline)