# Section 9.3.2
# https://docs.python.org/3.11/tutorial/classes.html#class-objects


class MyClass:
	"""A simple class example"""
	i = 12345

	def f(self):
		return 'Hello, World!'

class MyClassWithInit:
	"""A class example with constructor"""

	def __init__(self):
		print('inside __init__()')
		self.data = []

def main():
	print(50 * '-')
	print('main()')

	print(50 * '-')
	print('Instance object')
	o1 = MyClass()
	print('o1 = ', o1)
	print('type(o1):', type(o1))

	print('o1.i = ', o1.i)
	print('o1.f = ', o1.f)

	print(50 * '-')
	print('Class Object')
	print('MyClass = ', MyClass)
	print('MyClass.i = ', MyClass.i)
	print('MyClass.f = ', MyClass.f)
	
	print(50 * '-')
	print('Demonstrating class with __init__() method')
	o2 = MyClassWithInit()

if __name__ == '__main__':
	main()
