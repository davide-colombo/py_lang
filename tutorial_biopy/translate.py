# Section 3.8
# 

from Bio.Seq import Seq

def main():

	print(50 * '-')
	print("Messenger RNA sequence")
	mrna_seq = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
	print(mrna_seq)

	print(50 * '-')
	print('Translation from messenger RNA')
	protein_seq = mrna_seq.translate(stop_symbol='@')
	print(protein_seq)

	print(50 * '-')
	print('Translate directly from the CODING DNA')
	dna_seq = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
	protein_from_dna_seq = dna_seq.translate(stop_symbol='@')
	print(protein_from_dna_seq)

	assert protein_from_dna_seq == protein_seq

	print(50 * '-')
	print('Test different tables for the Genetic Code')
	print('Table = "Vertebrate Mitochondria"')

	protein_seq_vm = dna_seq.translate(table=2)
	print(protein_seq_vm)

	print(50 * '-')
	print('Stop when the first stop codon is found (as in nature)')
	protein_seq_stop = dna_seq.translate(to_stop=True)
	print(protein_seq_stop)	

if __name__ == '__main__':
	main()
