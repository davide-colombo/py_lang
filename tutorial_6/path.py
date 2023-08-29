# Module search path

# When a module named 'XXX' is imported,
# the interpreter first searches for a module
# with that name among 'sys.builtin_module_names'
# list.

def print_builtin_module_names():
	print("List of builtin modules:")
	for n in sys.builtin_module_names:
		print(n)
	print()

def print_syspath():
	print("sys.path = ", sys.path)

def print_pathsep():
	print("os.pathsep = ", os.pathsep)

if __name__ == "__main__":
	import sys
	import os
	print_builtin_module_names()
	print_pathsep()
	print_syspath()
