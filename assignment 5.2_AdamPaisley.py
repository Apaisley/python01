num_list = list()
while True:
	numbers = raw_input("enter a number:")
	If numbers == "done": break

	try:
		num_list.append(int(numbers))
	except:
		print"Please enter a number and not a word, try again"

print"the largest num is ",max(num_list), "& the smallest number is",min(num_list)