list = [2, 5, 3, 6, 9]

smallest = None

#do not overuser "is"; use "is" only with special value such as True, False, None
for numb in list : 
	if smallest is None:
		smallest = numb
	elif numb < smallest:
		smallest = numb
		
print smallest