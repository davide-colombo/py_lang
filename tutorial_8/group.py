# Section 8.9
# https://docs.python.org/3.11/tutorial/errors.html#raising-and-handling-multiple-unrelated-exceptions

def func():
	print(50 * '-')
	print('func()')
	
	exceptions = [OSError('error1'), SystemError('error2')]
	raise ExceptionGroup('Multiple exception occurred', exceptions)

def main():
	print(50 * '-')
	print('main()')

	try:
		func()
	except Exception as e:
		print(f'caught {type(e)}: e')

	print(50 * '-')
	print('Demonstrate exception group (no caught)')
	func()
	
if __name__ == '__main__':
	main()
