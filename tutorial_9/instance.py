# Section 9.3.5
# https://docs.python.org/3.11/tutorial/classes.html#class-and-instance-variables

class Dog:

	# This is a class variable
	# variable defined in the 'class object'
	# all 'instance objects' share the same value
	kind = 'canine'

	def __init__(self, name):
		self.name = name

def main():

	fido = Dog('Fido')
	buddy = Dog('Buddy')

	print(f'fido.name = {fido.name}')
	print(f'buddy.name = {buddy.name}')

	print(f'fido.kind = {fido.kind}')
	print(f'buddy.kind = {buddy.kind}')

if __name__ == '__main__':
	main()
