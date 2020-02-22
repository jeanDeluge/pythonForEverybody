fhand = open('romeo.txt')

newLine=[]
for line in fhand:
	newLine= newLine + (line.split(' '))

newLine.sort()
print(newLine)