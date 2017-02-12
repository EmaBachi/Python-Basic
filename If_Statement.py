
input = raw_input("Enter one value: ")
#Pay attention: raw input gives back a string so I have to convert the string into an integer. 
const = 10

#I put a try/except block in order to check the client input. I don't want my program to blow up for a wrong input.
try:
	x = int(input)
	if x < const :
		print "smaller"
	else :
		print "bigger"
except:
	print "Number Format Exception"

