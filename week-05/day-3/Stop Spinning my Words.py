def spin_words(sentence):
	new = sentence.split()
	print(new)
	rev = ""
	for n in range(len(new)):
		if len(new[n]) >= 5:
			new2 = new[n][::-1]
			for i in new2:
				rev += i
		else:
			rev += new[n]
		if n < len(new)-1:
			rev += " "
	return rev
    
    
print (spin_words("Malakala ha valakala"))