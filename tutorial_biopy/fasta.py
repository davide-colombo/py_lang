# Section 2.4
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec11

import sys
from Bio import SeqIO

def main():
	print(50 * '-')
	print('Demonstrate how to read a FASTA file')
	records = (sr for sr in SeqIO.parse('io/orchid.fasta', 'fasta'))
	r = next(records)

	print(50 * '-')
	print()
	print(r)
	print()

	print(50 * '-')
	print()
	print(repr(r))
	print()
	
	print(f'Object of type: "{type(r)}"')	
	print(f'length = {len(r)}')
	print(f'size in bytes = "{sys.getsizeof(r)}"')
	
if __name__ == '__main__':
	main()
