# Section 5.4
# https://docs.python.org/3.11/tutorial/datastructures.html#sets

def sets():
	print(50 * '-')
	print('sets()')

	cities = {'Milan', 'Paris', 'Miami', 'Tokyo'}
	print(cities)
	print(type(cities))

	print(50 * '-')
	print('Demonstrating a set cannot contain duplicates')
	print('cities.add("Milan")')
	print(cities)

	print(50 * '-')
	print('Demonstrate set operations on unique letters from two words')
	a = set('abracadabra')
	b = set('alacazam')

	print('unique letters in "a"')
	print(f'{a = }')
	
	print(50 * '-')
	print('letters in "a" but not in "b"')
	print(f'{a - b = }')

	print(50 * '-')
	print('letters in "a" or in "b" or both')
	print(f'{a | b = }')

	print(50 * '-')
	print('letters in both "a" and "b"')
	print(f'{a & b = }')

	print(50 * '-')
	print('letters in "a" or in "b" but not both')
	print(f'{a ^ b = }')
	
if __name__ == '__main__':
	sets()
