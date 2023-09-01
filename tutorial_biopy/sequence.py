# Section 2.2
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec7

import sys
from Bio.Seq import Seq

def main():
	mysequence = Seq("AGTACACTGGT")
	print(mysequence)
	print(type(mysequence))
	print(sys.getsizeof(mysequence))

if __name__ == '__main__':
	main()
