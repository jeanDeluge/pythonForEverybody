fhand = open('words.txt')

newList =[]
number =0
for lines in fhand:
	stripped = lines.strip()
	newList+=stripped.split(' ') 

dicList = dict()

for words in newList:
	number+=1
	dicList[number] = words
print(dicList)

print( 'we' in dicList.values())