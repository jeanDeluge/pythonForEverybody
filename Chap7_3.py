#esteregg
fname = input('Enter the file name:')
try:
	if fname == 'na na boo boo':
		print('NA NA BOO BOO TO YOU! - you have been punkd!')
	
	else:
		fhand = open(fname)
		
except:
	print('File cannot be opened', fname)