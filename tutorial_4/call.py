# Section 4.8.5
# https://docs.python.org/3.11/tutorial/controlflow.html#unpacking-argument-lists

def main():
	print(30 * '-')
	print('main()')

	d = {'voltage': 220, 'state': 'liquid', 'action': 'punch'}

	# NOTE: function call with a dictionary UNPACKED to kwargs
	parrot(**d)

	key_to_del = input('which argument do you want to remove?')
	try:
		del d[key_to_del]
	except KeyError as ke:
		print(f'invalid key: {ke}')

	# If voltage is deleted, code throws an exception
	try:
		parrot(**d)
	except TypeError as te:
		print(f'invalid arguments: {te}')
	
def parrot(voltage, state='solid', action='voom'):
	print(30 * '-')
	print('parrot()')
	print(f'{voltage = }, {state = }, {action = }')

if __name__ == '__main__':
	main()
