# Section 7.1.2
# https://docs.python.org/3.11/tutorial/inputoutput.html#the-string-format-method

def format():
	print(50 * '-')
	print('Demonstrate the str.format() function')
	print('We are the {} who say "{}"!'.format('warriors', 'Uah'))

	print(50 * '-')
	print('Demonstrate use of numbers in the brackets: {0}, {1}, ...')
	print('Three things must never miss in my breakfast: \
{0}, {1}, and {2}'.format('eggs', 'Montasio cheese', 'whole-grain bread'))

	print(50 * '-')
	print('Demonstrate use of keywords in the brackets: {arg1}, {arg2}, ...')
	print('This {thing} is {adj}'.format(thing='hotel', adj='superb'))

	print(50 * '-')
	print('Demonstrate old formatting using <"string" % value>')
	temperature = 37.9
	print('Today is so hot! It is %2.1f outside' % temperature)
	
if __name__ == '__main__':
	format()
