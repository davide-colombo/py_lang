# Demonstrate how it can be useful to use regular
# expression lookahead to get the coding region of gene

import re

def main():

	# ATG 		=> starts with 'ATG'
	# (?:...)	=> non-capturing group
	# [ATGC]{3}	=> string of length 3 made of 'A' or 'T' or 'C' or 'G'
	# ()*?		=> NON-GREEDY match of group, 0 or more times
	# (?:...)	=> another non-capturing group
	# (...|...)	=> match one or the other

	cds = re.compile(r'ATG(?:[ATGC]{3})*?(?:TAA|TAG|TGA)')
	
