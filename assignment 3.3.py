score = float(raw_input("Enter score: "))

try: 
	score >= 0.0 and score <= 1.0	
	print "Your score is: ", score

except:
	print "Your score is not valid!"
	
if score >= 0.9:
	print "A"
elif score >= 0.8:
	print "B"
elif score >= 0.7:
	print "C"
elif score >= 0.6:
	print "D"
elif score < 0.6:
	print "F"
	