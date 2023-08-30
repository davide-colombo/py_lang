# Test how much frequently Python reallocates memory


def biglist(n: int = 10000):
	ll = []
	size = sys.getsizeof(ll)
	resizecnt = 0

	for i in range(n):
		ll.append(i)
		if sys.getsizeof(ll) != size:
			resizecnt += 1
			print(f"RESIZED at iteration i = {i}")
			print(f'sys.getsizeof(ll) = {sys.getsizeof(ll)}')
			size = sys.getsizeof(ll)
	print(f'in {n} iterations the list has been resized {resizecnt} times.')

# Best way to convert a list of 'int' into a list of 'str'
# WITHOUT allocating memory for an entire new list!!!
#	gen = (str(x) for x in ll)
#	print(" ".join(gen))
			
if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		try:
			nel = int(sys.argv[1])
			biglist(nel)
		except ValueError as ve:
			print(f'Invalid input: {ve}')
			print(50 * '-')
			print("RUNNING WITH DEFAULT VALUE")
			biglist()
	else:
		biglist()
