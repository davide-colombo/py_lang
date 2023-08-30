# Section 4.8
# https://docs.python.org/3.11/tutorial/controlflow.html#more-on-defining-functions

def main():
	print(30 * "=")
	print('main()')

	ask_ok('Do you really want to quit?')
	ask_ok('OK to overwrite the file?', retries=1)
	ask_ok('OK to overwrite the file?', 2, 'USAGE: "y", "ye", "yes" to confirm; "n", "no" to reject.')
	

def ask_ok(prompt, retries=4, reminder='Please, try again'):
	print(30 * "=")
	print(f'ask_ok({prompt = }, {retries = }, {reminder = })')
	while True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no'):
			return False

		# Update retries
		retries -= 1
		if retries < 0:
			raise ValueError('invalid user response')
		print(reminder)

if __name__ == '__main__':
	main()
