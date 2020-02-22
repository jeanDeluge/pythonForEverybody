import urllib.request, urllib.parse, urllib.error
try:
	url = input('Enter url : ')
	fhand = urllib.request.urlopen(url)
	
	count = 0
	for line in fhand:
		words = line.decode()
		
		if count < 3000:
			count+=len(words)
			print(words.strip())
	print(count)

except:
	print('Error url')