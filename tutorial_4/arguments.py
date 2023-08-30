# Section 4.8
# Formal parameters: positional arguments and keyworded arguments

def main():
	print(30 * '=')
	print('main()')
	hello('Johnny', 100, 'Pluto', actor='Johnny Depp', movie='Pirates of Caribbean')
	

def hello(name, *args, **kwargs):
	print(30 * '=')
	print('hello()')
	print(f'{name = }')

	print('**Variable length positional arguments')
	for arg in args:
		print(f'{arg = }')

	print('**Variable length keyword arguments')
	for k, v in kwargs.items():
		print(f'{k} : {v}')

if __name__ == '__main__':
	main()
