# Section 5.1
# https://docs.python.org/3.11/tutorial/datastructures.html#more-on-lists

def lists():
	print(50 * '-')

	fruits = ['apple', 'orange', 'banana', 'pear', 'apricot']
	print(f'hex(id(fruits)) = {hex(id(fruits))}')
	print(fruits)

	print(50 * '-')
	print(f'len(fruits) = {len(fruits)}')
	print(f"fruits.count('pear') = {fruits.count('pear')}")
	print(f"fruits.index('banana') = {fruits.index('banana')}")

	print(50 * '-')
	fruits.extend(['blueberries', 'raspberries', 'blackberries'])
	print(fruits)
	print(f'len(fruits) = {len(fruits)}')

	print(50 * '-')
	print('insert at index 0')

	fruits.insert(0, 'banana')
	print(fruits)
	print(f'hex(id(fruits)) = {hex(id(fruits))}')

	print(50 * '-')
	print(f"fruits.index('banana') = {fruits.index('banana')}")

	print(50 * '-')
	fruits.remove('banana')			# this just removes the first instance
	print(fruits)
	print(f'hex(id(fruits)) = {hex(id(fruits))}')

	print(50 * '-')
	print('fruits.pop()')			# this removes the last item in the list
	item = fruits.pop()
	print(fruits)
	print(f'item removed: "{item}"')
	
	print(50 * '-')
	print('fruits.pop(1)')
	item = fruits.pop(1)
	print(fruits)
	print(f'item removed: "{item}"')

	print(50 * '-')
	print('fruits.reverse()')
	fruits.reverse()
	print(fruits)
	print(f'hex(id(fruits)) = {hex(id(fruits))}')

if __name__ == '__main__':
	lists()
