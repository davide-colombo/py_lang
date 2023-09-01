# Section 2.2
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec7

import sys
from Bio.Seq import Seq

COMPLEMENT_DICTIONARY = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def my_complement(dnaseq: str):
	res = [COMPLEMENT_DICTIONARY[n] for n in dnaseq]
	return "".join(res)

def main():
	print(50 * '-')
	print('Plain string DNA sequence')
	dnaseq = "AGTACACTGGT"
	print(dnaseq)

	print(50 * '-')
	print('Creating an object of type {type(Seq)}')
	mysequence = Seq(dnaseq)
	print(mysequence, type(mysequence), sys.getsizeof(mysequence))

	print(50 * '-')
	print(f'Complement of {mysequence!r} with BIOPYTHON')
	complement = mysequence.complement()
	print(complement)

	print(50 * '-')
	print('Complement of {dnaseq} using my_complement()')
	complement = my_complement(dnaseq)
	print(complement)

	print(50 * '-')
	print(f'Get the reverse complement of {mysequence!r}')
	reverse = mysequence.reverse_complement()
	print(reverse)
	
if __name__ == '__main__':
	main()
