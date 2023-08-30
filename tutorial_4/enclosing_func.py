# Section 4.7
# Try to assign a value to a variable defined in an
# enclosing function

def main():

	print(30 * "=")
	print('main()')
	enclosing()

def enclosing():
	print(30 * "=")
	print('enclosing()')

	n = 100
	c = 'a'

	print(f'{n = }')
	print(f'{c = }')
	
	def inner():
		print(30 * "=")
		print('inner()')

		n = 200
		ic = 'b'
		
		print(f'{ic = }')
		print(f'{n = }')
		print(f'{c = }')

	inner()


if __name__ == "__main__":
	main()
