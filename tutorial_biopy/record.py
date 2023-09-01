# Section 4.2.2
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec32

from Bio import SeqIO

def main():

	print(50 * '-')
	print("Inspecting 'Yersinia pestis' plasmid")
	record = SeqIO.read('io/yersinia_pestis.fasta', 'fasta')
	print(record)

	print(50 * '-')
	print('Querying useful attributes from the SeqRecord object')

	print(50 * '-')
	print('Record name')
	print(record.name)

	print(50 * '-')
	print('Record ID')
	print(record.id)

	print(50 * '-')
	print('Record description')
	print(record.description)

if __name__ == '__main__':
	main()
