# Section 4.8.8
# https://docs.python.org/3.11/tutorial/controlflow.html#function-annotations

def f(ham: str, eggs: str = 'eggs', price: float = 28.99) -> str:
	print(30 * '-.')
	print('f()')
	print(f'Annotations: {f.__annotations__}')
	print(f'Arguments: {ham = }, {eggs = }, {price = }')
	return ham + ' and ' + eggs + ' = ' + str(price)

if __name__ == '__main__':
	try:
		f(56)
	except TypeError as te:
		print('invalid argument type: {te}')
	
	f('San Daniele')
	f('Parma', 'Naturelle')
	f(ham = 'Rovagnati', eggs = 'from free chickens', price = 3.99)
