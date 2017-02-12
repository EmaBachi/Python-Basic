list = [ 0, 0, 0, 0]

i = 0

while i < 4: 
	input = raw_input("Enter a value: ")
	list[i] = input
	i = i+1
	
max = 0

for numb in list :
	if numb > max :
		max = numb

print max
