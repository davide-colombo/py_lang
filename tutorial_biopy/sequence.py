# Section 2.2
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec7

import sys
import re
from Bio.Seq import Seq

# ============================================================================
def isvalidnaseq(dnaseq:str) -> bool:
	if dnaseq:
		return bool(re.match(r'^[ATGC]+$', dnaseq))
	return False

# ============================================================================

COMPLEMENT_DICTIONARY = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def my_complement(dnaseq: str):
	if not isvalidnaseq(dnaseq):
		raise ValueError('"%s" is not a valid DNA sequence' % dnaseq)
	return "".join([COMPLEMENT_DICTIONARY[n] for n in dnaseq])

# ============================================================================
def main():
	print(50 * '-')
	print('Plain string DNA sequence')
	dnaseq = "AGTACACTGGT"
	print(dnaseq)

	print(50 * '-')
	print(f'{dnaseq!r} is a valid DNA sequence?')
	r = isvalidnaseq(dnaseq)
	assert r == True
	print(r)

	print(50 * '-')
	invalid_dnaseq = 'ATGXGCATTGAH'
	print(f'{invalid_dnaseq!r} is a valid DNA sequence?')
	r = isvalidnaseq(invalid_dnaseq)
	assert r == False
	print(r)
	
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
