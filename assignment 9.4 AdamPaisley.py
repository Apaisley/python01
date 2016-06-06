fname = raw_input("/n Enter File name:") #enter file name an saves to varibable to fname
if fname < 1:
	fname = 'mailbox-short.txt'


try:
		fhand = open(fname, 'r') # line means open file in read mode


except: 
	"Could not find File"

emailDict = {}
emaillist = []

for line in fhand:
	if not line.startswith('From'):continue

	words = line.split()
	email = emaillist.append(words[1])
for email in emaillist:
	emailDict[email] = emailDict.get(email,0)+1
print emailDict	
swap_list = []
for k,v in list_kv:
	swap_list.append((v,k))

print sorted(swap_list, reverse= True)