# Section 8.4
# https://docs.python.org/3.11/tutorial/errors.html#raising-exceptions

def raising():

	try:
		raise NameError('Hi')
	except NameError as ne:
		print(f'Caught: {ne}')

		# This just re-raise the exception!
		raise


if __name__ == '__main__':
	raising()
