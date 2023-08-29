# Fibonacci numbers module

def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

def fib2(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result


# In order to execute this file as a script
# it is necessary to check whether or not
# it has been invoked with "__main__" name
if __name__ == "__main__":
	import sys
	fib(int(sys.argv[1]))
