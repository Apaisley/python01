fname = raw_input('enter file')

if len(fname) < 0:
	fname ='romeo.txt'

try:
	fh = open(fname)
except:
	print " not a file"

	words =[]

	for line in fh:
		line_words = line.split()
		for word in list_words:
			if word in words:
				continue
				words.append(word)

print sorted (words)