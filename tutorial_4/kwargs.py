# Section 4.8
# Useful ways of using '/' and '*' in function definition

def main():
	print(30 * '-')
	print('main()')
	pos_only_args(111)

	try:
		pos_only_args(action='live')
	except TypeError as te:
		print(f'invalid function call: {te}')
	
	kwd_only_args(letter='a')

	try:
		kwd_only_args(10)
	except TypeError as te:
		print(f'invalid function call: {te}')

	combined_args(1, 'Hello, World!', kwd_only = True)
	combined_args('Foo', standard = 2, kwd_only = False)
	try:
		combined_args(1, 2, 3)
	except TypeError as te:
		print(f'invalid function call: {te}')

def pos_only_args(num, /):
	print(30 * '-')
	print('pos_only_args()')
	print(f'{num = }')

def kwd_only_args(*, letter):
	print(30 * '-')
	print('kwd_only_args()')
	print(f'{letter = }')

def combined_args(pos_only, /, standard, *, kwd_only):
	print(30 * '-')
	print('combined_args()')
	print(f'{pos_only = }, {standard = }, {kwd_only = }')

if __name__ == '__main__':
	main()
