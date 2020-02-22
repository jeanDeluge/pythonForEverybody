fhand = open('mbox.txt')

counts = dict()
for line in fhand:
	if not line.startswith('From:'):
		continue
	else:
		words= line.split()
		for word in words:
			if word not in counts:
				counts[word] =1
			else:
				counts[word] += 1


lst = list()
for key, val in list(counts.items()):
	lst.append((val, key))
	
del lst[0] #From을 튜플에서 지움

#가장 적은 메일을 받은 사람을 출력 => sort() 사용

lst.sort()
print('min', lst[0])


#가장 많은 메일을 보낸 사람 출력 =>sort(revers=True) 사용


lst.sort(reverse=True)
print('max', lst[0])