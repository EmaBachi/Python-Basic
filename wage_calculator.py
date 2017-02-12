treshold = 40
normalWage = 10
overtimeWage = 5
error = False

input = raw_input("Enter number of hours: ")

#don't put too many lines of code inside try block otherwise your program is not able to detect the proper error
try:
	hours = int(input)
except:
	error = True
	print "Error, please enter numeric input"
	
if error == False :
	if hours <= treshold :
		print "wage ", hours*normalWage
	else :
		print "wage ", treshold*normalWage + (hours-treshold)*overtimeWage