# Section 4.3
# Feature, location, position objects

from Bio import SeqFeature

def main():

	print(50 * '-')
	print('Start position')
	start_pos = SeqFeature.AfterPosition(109)
	print(start_pos)
	
	print(50 * '-')
	print('End position')	
	end_pos = SeqFeature.WithinPosition(689, left=667, right=689)
	print(end_pos)

	print(50 * '-')
	print('Location')
	location = SeqFeature.SimpleLocation(start_pos, end_pos)
	print(location)

if __name__ == '__main__':
	main()
