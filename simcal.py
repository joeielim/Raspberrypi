operation = int((raw_input('Please type in the math operation you would like to complete\n 1 for Addition\n 2 for Subtraction\n 3 for Mulitplication\n 4 for Division\n')))

n1 = float(input('Please enter the first number: \n'))
n2 = float(input('Please enter the secound number: \n'))

if operation == 1:
	print('{} + {} = '.format(n1, n2))
	print(n1 + n2)
elif operation == 2:
	print('{} - {} = '.format(n1, n2))
	print(n1 - n2)
elif operation == 3:
	print('{} * {} = '.format(n1, n2))
	print(n1 * n2)
elif operation == 4:
	print('{} / {} = '.format(n1, n2))
	print(n1 / n2)
