# Section 4.3
# https://docs.python.org/3.11/tutorial/controlflow.html#the-range-function

def main():

	myrange = range(5, 13, 3)
	
	print(30 * '=')
	print(f'"myrange" type is "{type(myrange)}"')

	for n in myrange:
		print(f'number {n} found in "myrange"')

	print(30 * '=')
	print(f'sum of "myrange" is equal to {sum(myrange)}')

	# Use the range() function to iterate over a list
	print(30 * '=')
	values = ['a', 'b', 'c', 'd']
	for i in range(len(values)):
		print(f'index {i} found value = "{values[i]}"')

	# What happens if we try to print a range object?
	print(30 * '=')
	print(f'printing a "range" object gives "{myrange!r}"')
		
if __name__ == '__main__':
	main()
