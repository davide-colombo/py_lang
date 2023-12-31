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

import re

def main():
	"""A collection of examples on 'how to use' regular expressions"""

	print(50 * '-')
	print('main()')

	print(50 * '-')
	print('Test a simple pattern: "ab*"')
	p1 = re.compile(r'ab*')
	print(p1)

	print(50 * '-')
	print('Test a simple match on "ab*" pattern')

	s = "a"
	s1 = 'ab'
	s2 = 'abbbbb'
	s3 = 'abbba'
	s4 = 'best of abba'

	print(f'"ab*" match {s!r}: ', p1.match(s))
	print(f'"ab*" match {s1!r}: ', p1.match(s1))
	print(f'"ab*" match {s2!r}: ', p1.match(s2))
	print(f'"ab*" match {s3!r}: ', p1.match(s3))

	print(50 * '-')
	print('Demonstrate non-greedy match')
	p2 = re.compile(r'ab*?')

	print(f'"ab*?" match {s!r}: ', p2.match(s))
	print(f'"ab*?" match {s1!r}: ', p2.match(s1))
	print(f'"ab*?" match {s2!r}: ', p2.match(s2))
	print(f'"ab*?" match {s3!r}: ', p2.match(s3))
	print(f'"ab*?" match {s4!r}: ', p2.match(s4))

	print(50 * '-')
	print('Demonstrate how to use the search() method')

	print(f'"ab*?" search {s!r}: ', p2.search(s))
	print(f'"ab*?" search {s1!r}: ', p2.search(s1))
	print(f'"ab*?" search {s2!r}: ', p2.search(s2))
	print(f'"ab*?" search {s3!r}: ', p2.search(s3))
	print(f'"ab*?" search {s4!r}: ', p2.search(s4))

	print(50 * '-')
	print('Inspect the <match> object')

	m2_s4 = p2.search(s4)
	print(f'"ab*?" search {s4!r} span: ', m2_s4.span())
	print(f'"ab*?" search {s4!r} start: ', m2_s4.start())
	print(f'"ab*?" search {s4!r} end: ', m2_s4.end())
	print(f'"ab*?" search {s4!r} group: ', m2_s4.group())

	print(50 * '-')
	print('Demonstrate findall(): "ab*?" on %s' % s4)

	all2_s4 = p2.findall(s4)
	print(all2_s4)
	
	print(50 * '-')
	print(F'Demonstrate finditer(): "ab*?" on {s4!r}')

	iter2_s4 = p2.finditer(s4)
	for match in iter2_s4:
		print(match)

	print(50 * '-')
	print('Try to inspect the behavior when multiple patterns are available')
	
	mystring = '@@abcd!!'
	mypattern = re.compile(r'\w\w\w')
	myall = mypattern.findall(mystring)
	if not myall:
		print(f'Pattern {mypattern!r} does not match anything in {mystring!r}')
	for match in myall:
		print(match)

	print(50 * '-')
	print('Demonstrate lookahead assertion')

	mypattern = re.compile(r'(?=(\w{3}))')
	myall = mypattern.findall(mystring)
	if not myall:
		print(f'Pattern {mypattern!r} does not match anything in {mystring!r}')
	for match in myall:
		print(match)


if __name__ == '__main__':
	main()
