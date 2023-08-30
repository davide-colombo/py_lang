# Section 5.3
# https://docs.python.org/3.11/tutorial/datastructures.html#tuples-and-sequences

def tup():
	print(50 * '-')
	print('tup()')

	t = 1234, 5678, "Hello"
	print(f't = <1234, 5678, "Hello"> gives: <{t}>')

	print(50 * '-')
	print('Demonstrate tuples are IMMUTABLE')
	try:
		t[0] = 8888
	except TypeError as te:
		print(f'Invalid operation: {te}')

	print(50 * '-')
	print('A tuple of mutable objects')
	mut = ([1, 2, 3, 4], [5, 6, 7, 8])
	print(f'mut = <[1, 2, 3, 4], [5, 6, 7, 8]> = <{mut}>')

	print(50 * '-')
	print('Demonstrate tuple unpacking')
	x, y, cheer = t
	print('x, y, cheer = t')
	print(f'{x = }, {y = }, {cheer = }')

if __name__ == '__main__':
	tup()
