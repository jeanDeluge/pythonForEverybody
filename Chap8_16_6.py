
list=[]

keep = True

while(keep):
	inp = input('Enter the number')
	try:
		list.append(int(inp))
	
	except:
		if inp =='done':
			keep=False
		else :
			print('enter number')
	
def max(list):
	max = list[0]
	for number in list:
		if max <= number:
			max = number
	return max
	
def min(list):
	min = list[0]
	for number in list:
		if min >= number:
			min = number
	return min
print('Max: ', max(list), 'Min: ', min(list))