# Section 4.6
# https://docs.python.org/3.11/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

def main():

	print(30 * '=')
	print(error_code_description(1))
	print(30 * '=')
	print(error_code_description(10))
	print(30 * '=')
	print(error_code_description(11))
	print(30 * '=')
	print(error_code_description(42))
		
def error_code_description(errno):

	# 'match' statement
	# similar to a 'switch' statement
	# different in that it matches the pattern
	
	match errno:
		case 1:
			return "Bad request"
		case 10:
			return "Not found"
		case 11:
			return "Foo"

		# The variable name "_" never fails to match!!
		case _:
			return "Something went wrong, error code invalid"

if __name__ == '__main__':
	main()
