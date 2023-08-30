# Section 5.1.3
# Comprehension list
# More precise timing

import timeit

def compreh1(nel: int):
	squares = []
	for n in range(nel):
		squares.append(n ** 2)

def compreh2(nel: int):
	squares = list(map(lambda x: x ** 2, range(nel)))

def compreh3(nel: int):
	squares = [x ** 2 for x in range(nel)]

def compreh4(nel: int):
	squares = (x ** 2 for x in range(nel))

def main(nel: int, niter: int):
	print(50 * '-')
	print(f'timing "compreh1({nel = })"')
	print(f'Number of iterations = {niter}')
	time_compreh1 = timeit.timeit(lambda: compreh1(nel), number=niter)
	print(f'Elapsed: {time_compreh1:.8f}')

	print(50 * '-')
	print(f'timing "compreh2({nel = })"')
	print(f'Number of iterations = {niter}')
	time_compreh2 = timeit.timeit(lambda: compreh2(nel), number=niter)
	print(f'Elapsed: {time_compreh2:.8f}')

	print(50 * '-')
	print(f'timing "compreh3({nel = })"')
	print(f'Number of iterations = {niter}')
	time_compreh3 = timeit.timeit(lambda: compreh3(nel), number=niter)
	print(f'Elapsed: {time_compreh3:.8f}')

	print(50 * '-')
	print(f'timing "compreh4({nel = })"')
	print(f'Number of iterations = {niter}')
	time_compreh4 = timeit.timeit(lambda: compreh4(nel), number=niter)
	print(f'Elapsed: {time_compreh4:.8f}')


if __name__ == '__main__':
	import sys
	nel = 100000
	niter = 100
	
	if len(sys.argv) > 1:
		try:
			nel = int(sys.argv[1])
			if nel <= 0:
				raise ValueError('Invalid argument: number of element must be a positive integer.')
		except ValueError as ve:
			print(f'Invalid usage: {ve}')

	if len(sys.argv) > 2:
		try:
			niter = int(sys.argv[2])
			if niter <= 0:
				raise ValueError('Invalid argument: number of iterations must be a positive integer.')
		except ValueError as ve:
			print(f'Invalid argument: {ve}')

	# Call with default value of the parameters
	main(nel, niter)
