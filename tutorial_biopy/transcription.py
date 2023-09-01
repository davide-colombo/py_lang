# Section 3.7
# 

from Bio.Seq import Seq

COMPLEMENT_DICT = {
	'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'
}

def complement(seq:str)->str:
	"""Computes the sequence in the opposite directionality"""
	return "".join([COMPLEMENT_DICT[n] for n in seq])

def reverse_complement(seq:str)->str:
	"""Return the complement and maintains the directionality of the input sequence"""
	return complement(seq)[::-1]

TRANSCRIPTION_DICT = {
	'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'
}

def transcription_from_coding(seq: str) -> str:
	# Check if 'seq' is a valid dna sequence

	# First: compute complement
	compl = complement(seq)

	# Second: transcribe
	return "".join([TRANSCRIPTION_DICT[n] for n in compl])
	
def transcription_from_noncoding(seq:str)->str:

	rev = seq[::-1]

	# Check if 'seq' is a valid DNA sequence
	return "".join([TRANSCRIPTION_DICT[n] for n in rev])

def main():

	coding_str = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

	# NOTE: this is 3'-5' if "coding_str" directionality is 5'-3'
	noncoding_str = complement(coding_str)

	# NOTE: this has the same directionality as 'coding_str'
	noncoding_str_5_to_3 = reverse_complement(coding_str)
	
	print(50 * '-')
	print("Coding strand (5'-3')")
	coding_seq = Seq(coding_str)
	print(coding_seq)

	print(50 * '-')
	print("Non-coding strand (5'-3')")
	noncoding_seq = coding_seq.reverse_complement()
	print(noncoding_seq)

	assert Seq(noncoding_str_5_to_3) == noncoding_seq
	
	print(50 * '-')
	print('Transcription from the coding sequence (NO BIOPYTHON)')
	mrna_str = transcription_from_coding(coding_str)
	print(mrna_str)

	print(50 * '-')
	print('Transcription using BIOPYTHON')
	mrna_seq = coding_seq.transcribe()
	print(mrna_seq)

	assert Seq(mrna_str) == mrna_seq	

	print(50 * '-')
	print('Transcription from noncoding strand (NO BIOPYTHON)')
	mrna_str = transcription_from_noncoding(noncoding_str_5_to_3)
	print(mrna_str)

	print(50 * '-')
	print('Transcription from noncoding strand (BIOPYTHON)')
	mrna_seq = noncoding_seq.reverse_complement().transcribe()
	print(mrna_seq)

	assert Seq(mrna_str) == mrna_seq
	
if __name__ == '__main__':
	main()
