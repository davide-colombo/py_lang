# Section 9.6
# https://docs.python.org/3.11/tutorial/classes.html#private-variables

class Mapping:

	def __init__(self, iterable):
		self.items = []
		self.__update(iterable)			# actually call the method
		
	def update(self, iterable):
		print(50 * '-')
		print('Mapping.update()')
		for item in iterable:
			self.items.append(item)

	# NAME MANGLING -> _Mapping__update
	# pointer to a method
	__update = update

class MappingSubclass(Mapping):

	def update(self, keys, values):
		print(50 * '-')
		print('MappingSubclass.update()')
		for item in zip(keys, values):
			self.items.append(item)

def main():

	print(50 * '-')
	print('main()')

	print(50 * '-')
	print('Creating an instance of type "Mapping()"')
	o1 = Mapping([1, 2, 3])
	o1.update([4, 5, 6])
	print(o1.items)
		
	print(50 * '-')
	print('Creating an instance of type "MappingSubclass()"')
	o2 = MappingSubclass(['a', 'b'])
	o2.update(['Jack', 'Rose', 'Titanic'], ['Main male character', 'Main female character', 'Movie title'])
	print(o2.items)
	
if __name__ == '__main__':
	main()
