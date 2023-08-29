# Section 4.4
# https://docs.python.org/3.11/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops


def main():
	print(30 * '=')
	print("testing the break statement")
	test_break()

	print(30 * "=")
	print("testing the continue statement")
	test_continue()

def test_break():

	# This spans 2, 3, 4, 5, 6, 7, 8, 9
	for n in range(2, 10):

		# NOTE: if n = 2, range(2, n) returns an empty list
		for x in range(2, n):
			if n % x == 0:

				# NOTE: n // x is the floor division, returns an 'int'
				print(n, 'equals', x, '*', n // x)
				break
		
		# This else correspond to the nested for statement
		# Runs when no 'break' statement occurs
		else:
			print(n, 'is a prime number')			

def test_continue():
	for n in range(2, 10):
		if n % 2 == 0:
			print("Found an even number", n)
			continue
		print("Found an odd number", n)

if __name__ == "__main__":
	main()
