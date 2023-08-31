# Section 8.5
# https://docs.python.org/3.11/tutorial/errors.html#exception-chaining

def func():

	# NOTE: we are not creating an instance here!!!
	# Parenthesis are missing!!
	# However, the Python interpreter does this for us

	raise ConnectionError
	
def main():

	try:
		func()
	except ConnectionError as ce:
		raise RuntimeError('Something went wrong...') from ce

if __name__ == '__main__':
	main()
