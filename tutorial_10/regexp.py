# Section 10.5
# https://docs.python.org/3/tutorial/stdlib.html#string-pattern-matching

# Library/re
# https://docs.python.org/3/library/re.html#regular-expression-syntax

# -start-
# =======================================================================
# BACKSLASH: escape characters with special meaning

# IMPORTANT: use the 'raw' string for regular expression patterns!

# ab	=> matches 'ab'
# ab*	=> matches 'a' followed by 0 or more 'b's
# ab+	=> matches 'a' followed by 1 or more 'b's
# ab?	=> matches 'a' or 'ab'

# GREEDY: match as much text as possible (i.e., longest match)

# Add '?' to match in a NON-GREEDY fashion (i.e., shortest match)

# a{m}		=> matches 'a' exactly m times
# a{m,n}	=> matches 'a' between m and n times (longest, i.e., GREEDY)
# a{m,n}?	=> matches 'a' between m and n times (shortest, i.e., NON-GREEDY)
# =======================================================================
# -end-

def main():
	"""A collection of examples on 'how to use' regular expressions"""

if __name__ == '__main__':
	main()
