#basic program in order to compute the average. The average will be compute when user writes 'done'.

count = 0
sum = 0

while True:
	input = raw_input("Enter a value or done: ")
	
	if input == 'done': 
		break
	if len(input) < 1:  #this line clean a little bit the input
		break
		
	try:
		numb = float(input)
	except:
		print 'Invalid input'
		continue
	
	count = count + 1
	sum = sum + numb

		
print "average: ", float(sum/count)