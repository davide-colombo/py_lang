# Section 2.2
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec7

import sys
from Bio.Seq import Seq

def main():

	print(50 * '-')
	print('Creating an object of type {type(Seq)}')
	mysequence = Seq("AGTACACTGGT")
	print(mysequence)
	print(type(mysequence))
	print(sys.getsizeof(mysequence))

	print(50 * '-')
	print(f'Get the complement of {mysequence!r}')
	complement = mysequence.complement()
	print(complement)

	print(50 * '-')
	print(f'Get the reverse complement of {mysequence!r}')
	reverse = mysequence.reverse_complement()
	print(reverse)
	
if __name__ == '__main__':
	main()
