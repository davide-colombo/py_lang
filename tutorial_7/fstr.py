# Section 7.1.1
# https://docs.python.org/3.11/tutorial/inputoutput.html#formatted-string-literals

def format():
	print(50 * '-')
	
	numf = 4.4683678
	print(f'{numf = }')
	print(f'numf up to third digit is {numf:.3f}')

	print(50 * '-')
	print('Demonstrate how to format a table')
	table = {'Galua': 4622, 'Robby': 5589, 'Mergh': 2101}
	for name, phone in table.items():
		print(f'{name:10} ==> {phone:10d}')

	print(50 * '-')
	print('Demonstrate the difference between "str()" and "repr()"')
	animal = "cow"
	print(f'str(animal) = {animal!s}')
	print(f'repr(animal) = {animal!r}')

	ten = 10
	print(f'str(ten) = {ten!s}')
	print(f'repr(ten) = {ten!r}')

	fruits = ['apple', 'orange', 'pear', 'banana', 'watermelon']
	print(f'str(fruits) = {str(fruits)}')
	print(f'repr(fruits) = {repr(fruits)}')
	
if __name__ == '__main__':
	format()
