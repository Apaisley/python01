fname = raw_input('File name')
if len(fname) < 0:
	fname ='mbox-short.txt'


try: 
	fh = open(fname)
except:
	print" not a file bruh"

for line in fh:
	if not line.startswith('X-DSPAM-Confidence:'):
		continue
		
	else:
		num_start = line.find('0')
		num = line[ num_start:]
		flt = float(num)
		count += flt

print count