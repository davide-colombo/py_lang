# Section 9.3.2
# https://docs.python.org/3.11/tutorial/classes.html#class-objects


class MyClass:
	"""A simple class example"""
	i = 12345

	def f(self):
		return 'Hello, World!'


def main():
	print(50 * '-')
	print('main()')

	o1 = MyClass()
	print('o1 = ', o1)
	print('type(o1):', type(o1))

	print('o1.i = ', o1.i)
	print('o1.f = ', o1.f)

if __name__ == '__main__':
	main()
