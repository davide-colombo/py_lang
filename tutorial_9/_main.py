# This module is imported by "./main.py"

foo = f"This is a global variable defined in {__name__!r}"

def f():
	print(50 * '$')
	print(f'Inside f() function defined in {__name__!r}')
