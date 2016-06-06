fname = raw_input('File name')
if len(fname) < 0:
	fname ='mbox-short.txt'


try: 
	fh = open(fname)
except:
	print" not a file bruh"

emails ={}
email_list = []
for line in fh:
	if not line.startswith('From'):
		continue
		words = line.split()
		email = words[1]
		email_list.append(email)

for address in email_list:
	emails[address] = emails.get(address, 0) + 1

	big_address = None
	big_count = None

	for address	, count in emails.items():
		if big_count is None or count > big_address:
		 big_count = count
		  big_address = address


print big_count, big_address
