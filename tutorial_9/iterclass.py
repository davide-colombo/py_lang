# Section 9.8
# Define an iterable class by implementing the iterator interface

class ReverseIterator:

	def __init__(self, items):
		self.items = items
		self.index = len(items)

	def __iter__(self):
		print(50 * '-')
		print('ReverseIterator.__iter__()')

		return self

	def __next__(self):
		print(50 * '-')
		print('ReverseIterator.__next__()')

		if self.index == 0:
			raise StopIteration
		self.index -= 1
		return self.items[self.index]

def main():
	print(50 * '-')
	print('main()')

	ri = ReverseIterator([i for i in range(10)])
	print(f'type(ri) = {type(ri)}')

	print(50 * '-')
	print('Cycling through the iterator')
	for item in ri:
		print(item)

if __name__ == '__main__':
	main()
