# Section 9.4
# https://docs.python.org/3.11/tutorial/classes.html#random-remarks

# Instance prioritization over class

class Warehouse:
	purpose = 'storage'
	region = 'west'

def main():

	west = Warehouse()
	print(f'{west.purpose = }, {west.region}')

	east = Warehouse()
	east.region = 'east'
	print(f'{east.purpose = }, {east.region}')

if __name__ == '__main__':
	main()
	
