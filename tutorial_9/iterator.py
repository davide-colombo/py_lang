# Section 9.8
# https://docs.python.org/3.11/tutorial/classes.html#iterators

def main():

	print(50 * '-')
	print('main()')

	s = 'superstring'
	print(f'Target of the iterator is: {s!r}')

	# This binds 'it' to an object of type 'class iterator'
	it = iter(s)
	print(f'{type(it) = }')

	try:
		while True:
			next_char = next(it)
			print(f'{next_char = }')
	except StopIteration as e:
		print('End of iterable object')

if __name__ == '__main__':
	main()
