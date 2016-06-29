text ="X-DSPAM-Confindence:     0.8475"

num_strt = text.find('0')
print num_strt
num = text[num_strt:]

flt = float(num)

print flt