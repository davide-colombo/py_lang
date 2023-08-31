# Section 9.9
# https://docs.python.org/3.11/tutorial/classes.html#generators

def reverse(data: str):
	for index in range(len(data)-1, -1, -1):
		yield data[index]

if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		for char in reverse(sys.argv[1]):
			print(char, end='')
		print()
	else:
		print('USAGE: the magic happens only if you pass at least one argument...')
