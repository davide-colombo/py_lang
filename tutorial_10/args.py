# Section 10.3
# https://docs.python.org/3/tutorial/stdlib.html#file-wildcards

import argparse

def parse_arguments():

	parser = argparse.ArgumentParser(
		prog='myFreakin\'Program',
		description='Demonstrate usage of "ArgumentParser()"',
		epilog='the sun is shining on Sacramento today'
	)

	# More than one 'filename' can be passed from the command line
	# after the 'filenames' keyword
	# IMPORTANT: '+' indicates the argument is required!
	parser.add_argument('-f', '--files', nargs='+')
	
	parser.add_argument('-l', '--lines', type=int, default=10)

	# Demonstrate how to use 'action' argument
	parser.add_argument('-s', '--speed', action='store_const', const=42)
	parser.add_argument('-e', '--ended', action='store_true')
	parser.add_argument('-c', '--choco', action='store_false')
	parser.add_argument('-p', '--pasta', action='count')

	# Demonstrate use of 'choices' argument	
	parser.add_argument('-eg', '--eggs', choices=['fried', 'hard-boiled'])
	parser.add_argument('-d', '--doors', type=int, choices=range(1,4))

	# Demonstrate 'required'
	parser.add_argument('-r', '--required', required=True)

	# Demonstrate 'help'
	parser.add_argument('-o', '--foo', help='fooing all of the bar')
	parser.add_argument('-b', '--bar', help='barring all of the foo')

	args = parser.parse_args()
	print(args)

def main():
	parse_arguments()

if __name__ == '__main__':
	main()
