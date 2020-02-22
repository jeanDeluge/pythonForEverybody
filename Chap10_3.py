#문자의 빈도수를 내림차순으로 출력
#모든문자를 소문자로 변환
#a~z 사이의 문자만 카운트
# 공백, 숫자, 구두점 등은 카운트 안함
import string

fhand = open('romeo-full.txt')

counts = dict()#문자, 빈도수

for line in fhand:
	line = line.rstrip()
	line = line.translate(line.maketrans('','',string.punctuation))#구두점 제외
	line = line.translate(line.maketrans('','',string.digits))#숫자제외
	line = line.lower()#소문자로 변환
	
	words = line.split()#공백제외
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word]+=1
			
words = list()

for noun, number in list(counts.items()):
	words.append((number, noun))
	
words.sort(reverse=True) #빈도수내림차순으로 출력

print(words)

