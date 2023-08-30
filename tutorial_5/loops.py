# Section 5.6
# https://docs.python.org/3.11/tutorial/datastructures.html#looping-techniques

def dicts():
	print(50 * '-')
	print('dicts()')

	print('Creating a dict from list of tuples')
	lot = [(1, 'Hello'), (2, 'Ciao')]
	print(f'{lot = }')
	d1 = dict(lot)
	print(f'dict(lot) = < {d1} >')

	print(50 * '-')
	d2 = {x: x**2 for x in (2, 4, 6)}
	print('x: x**2 for x in (2, 4, 6)')
	print(f'{d2 = }')

	print(50 * '-')
	print('Demonstrate the items() function')
	for k, v in d1.items():
		print(k, v)

	print(50 * '-')
	print('Demonstrate the enumerate() function')
	for i, v in enumerate(['brave', 'courageous', 'fearless']):
		print(i, v)

	print(50 * '-')
	print('Demonstrate the zip() function')
	n = [1, 2, 3, 4]
	l = ['a', 'b', 'c', 'd']
	for num, letter in zip(n, l):
		print(num, letter)

	print(50 * '-')
	print('Demonstrate reversed() function')
	for i in reversed(range(1, 100, 13)):
		print(i)

	print(50 * '-')
	print('Demonstrate how to get a sorted(se())')
	basket = ['apples', 'carrotes', 'bananas', 'yogurts', 'bananas', 'bananas', 'apples', 'oranges']
	for item in sorted(set(basket)):
		print(item) 

if __name__ == "__main__":
	dicts()
