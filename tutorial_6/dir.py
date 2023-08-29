# The dir() function

a = [1, 2, 3]

def print_dirfibo():
	print(dir(fibo))

def print_dirsys():
	print(dir(sys))

def print_dirbuiltins():
	print("**Builtins")
	gen = (x for x in dir(builtins) if x[0] != '_')
	s = ', '.join(name for name in gen)
	print(s)
	print("**Builtins with double underscores")
	gen = (x for x in dir(builtins) if x[0] == '_')
	s = ', '.join(name for name in gen)
	print(s)
	
def print_dir():
	print(dir())

if __name__ == "__main__":
	import fibo, sys, builtins
	print_dirfibo()
	print_dirsys()
	print_dirbuiltins()
	print_dir()
