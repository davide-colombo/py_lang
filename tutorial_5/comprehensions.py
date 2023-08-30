# Section 5.1.3
# https://docs.python.org/3.11/tutorial/datastructures.html#list-comprehensions

import time

def comprehensions_square(n: int = 10000):

	# Basic version, sloppy
	t0 = time.time()
	squares = []
	for i in range(n):
		squares.append(i ** 2)
	t1 = time.time()
	
	print(50 * '-')
	print('squares')
	print(f'elapsed = {t1 - t0}')
	
	# Better
	t2 = time.time()
	squares2 = [x ** 2 for x in range(n)]
	t3 = time.time()
	
	print(50 * '-')
	print('squares2')
	print(f'elapsed = {t3 - t2}')
	
	# Better, using a lambda expression
	t4 = time.time()
	squares3 = list(map(lambda x: x**2, range(n)))
	t5 = time.time()
	
	print(50 * '-')
	print('squares3')
	print(f'elapsed = {t5 - t4}')

	# Best, using generator
	t6 = time.time()
	squares4 = (x**2 for x in range(n))
	t7 = time.time()
	
	print(50 * '-')
	print('squares4')
	print(f'elapsed = {t7 - t6}')
	
	print(50 * '-')
		
if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		try:
			nel = int(sys.argv[1])
			if nel <= 0:
				raise ValueError('Invalid argument: number of element cannot be negative of zero.')
			comprehensions_square(nel)
		except ValueError as ve:
			print(f'Invalid usage: {ve}')
	else:
		comprehensions_square()
