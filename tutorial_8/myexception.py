# Section 8.3
# https://docs.python.org/3.11/tutorial/errors.html#handling-exceptions


class SunException(Exception):
	pass

class MoonException(SunException):
	pass

class AstronautException(MoonException):
	pass

class AnotherException(Exception):
	pass
	
def raise_exception(exception_instance):
	print(50 * '-')
	print('raise_exception()')
	
	if not isinstance(exception_instance, Exception):
		raise SystemExit('Invalid type')
		
	try:
		raise exception_instance	
	except AstronautException:
		print('AstronautException!')
	except MoonException:
		print('MoonException!')
	except SunException:
		print('SunException')
	else:
		print('No exception has occurred!')
	finally:
		print('Finally clause is always executed')

def main():
	print(50 * '-')
	print('main()')
	raise_exception(SunException())
	raise_exception(MoonException())
	raise_exception(AstronautException())
	raise_exception(AnotherException())		# not caught, propagates back
	print(50 * '-')

if __name__ == '__main__':
	main()
