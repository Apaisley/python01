fname = raw_input('File name')
if len(fname) < 0:
	fname ='mbox-short.txt'


try: 
	fh = open(fname)
except:
	print" not a file bruh"

for line in fh:
	if not line.startswith('From'):
		continue
	words_list = line.split()
	email = words_list[1]
	count += 1
	print email