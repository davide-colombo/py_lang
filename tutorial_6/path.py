# Module search path

# When a module named 'XXX' is imported,
# the interpreter first searches for a module
# with that name among 'sys.builtin_module_names'
# list.

def print_builtin_module_names():
	for n in sys.builtin_module_names:
		print(n)

if __name__ == "__main__":
	import sys
	print_builtin_module_names()
