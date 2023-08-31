# Test different ways to concatenate strings

import timeit

def concat1(nel: int):
	s = ""
	for i in range(nel):
		s += 'a'

def concat2(nel: int):
	elements = ['a' for i in range(nel)]
	s = " ".join(elements)

def concat3(nel: int):
	# NOTE: generator is slower because it is first
	# converted into a 'list' or 'tuple'
	gen = ('a' for i in range(nel))
	s = " ".join(gen)

def concat4(nel: int):
	elements = ('a' for i in range(nel))
	s = ' '.join(elements)

def concat5(nel: int):
	gen = ('a' for i in range(nel))
	s = " ".join(list(gen))

def main(nel: int = 100000, niter: int = 100):
	print(50 * '-')
	print(f'main({nel = }, {niter = })')

	print(50 * '-')
	print('Demonstrate for loop with += operator')
	time_1 = timeit.timeit(lambda: concat1(nel), number=niter)
	print(f'Elapsed = {time_1:.8f} seconds')

	print(50 * '-')
	print('Demonstrate join() on list')
	time_2 = timeit.timeit(lambda: concat2(nel), number=niter)
	print(f'Elapsed = {time_2:.8f} seconds')

	print(50 * '-')
	print('Demonstrate join() on generator')
	time_3 = timeit.timeit(lambda: concat3(nel), number=niter)
	print(f'Elapsed = {time_3:.8f} seconds')

	print(50 * '-')
	print('Demonstrate join() on a tuple')
	time_4 = timeit.timeit(lambda: concat4(nel), number=niter)
	print(f'Elapsed = {time_4:.8f} seconds')

	print(50 * '-')
	print('Demonstrate join(list(generator)) on a generator')
	time_5 = timeit.timeit(lambda: concat5(nel), number=niter)
	print(f'Elapsed = {time_5:.8f} seconds')

if __name__ == '__main__':
	main()
