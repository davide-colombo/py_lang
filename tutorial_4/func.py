# Section 4.7
# https://docs.python.org/3.11/tutorial/controlflow.html#defining-functions

def main(n):
	print(30 * '=')
	print(f'main({n})')
	
	fibo(n)

def fibo(n):
	print(30 * '=')
	print(f'fibo({n})')
	print(f'print a fibonacci series up to <n>')
	
	a = 0
	b = 1
	while a < n:
		print(a, end=' ')
		c = a
		a = b
		b += c
	print()

if __name__ == "__main__":
	import sys
	if len(sys.argv) == 2:
		try:
			# Throws ValueError if not a digit
			n = int(sys.argv[1])
			
			# OTHERWISE: start the program
			main(n)
		except ValueError as ve:
			print(f'Invalid input: {ve}')

	else:
		raise ValueError(f"USAGE: python[major.minor] func.py <n>")
