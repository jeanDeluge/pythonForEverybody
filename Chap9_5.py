fhand = open('mbox-short.txt')


counts= dict()
for line in fhand:
	line.rstrip()
	if line.startswith('From:'):
		words = line.split()
		domain = words[1].split('@')
		if domain[1] not in counts:
			counts[domain[1]] = 1
		else : 
			counts[domain[1]] += 1
	else: continue
	
print(counts)