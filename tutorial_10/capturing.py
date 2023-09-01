# Demonstrating the usage of capturing group in Py's regular expressions.

import re

def main():
	s = "My name is John and I'm from Michigan"
	p = r"[mM]y name is (\w+) and I'm from (\w+)"
	m = re.search(p, s)	# use module-level function
	name = m.group(1)
	city = m.group(2)

	print(f"Name: {name}")
	print(f"City: {city}")

	a = re.findall(p, s)
	for match in a:
		print("new match! => ", match)

	print(50 * '-')
	print('Capturing pattern 2')

	s = 'abababab'
	p1 = re.compile(r'(ab)+')		# greedy
	p2 = re.compile(r'(ab)+?')		# non-greedy

	print(50 * '-')
	print('GREEDY: findall(), p1, s')
	for m in p1.findall(s):
		print(m)

	print(50 * '-')
	print('NON-GREEDY: findall(), p2, s')
	for m in p2.findall(s):
		print(m)

	print(50 * '-')
	print('GREEDY: match(), p1, s')
	m1 = p1.match(s)
	print(m1)

	print(50 * '-')
	print('NON-GREEDY: match(), p2, s')
	m2 = p2.match(s)
	print(m2)

	print(50 * '-')
	print('GREEDY: group(0)')
	print(m1.group(0))
		
	print(50 * '-')
	print('NON-GREEDY: group(0)')
	print(m2.group(0))

	# WHY IS THERE ONLY A SINGLE GROUP?
	# groups are not matches
	# there is only one group because the RE pattern defines one group

	print(50 * '-')
	print('GREEDY: groups()')
	for g in m1.groups():
		print(g)

	print(50 * '-')
	print('NON-GREEDY: groups()')
	for g in m2.groups():
		print(g)

if __name__ == '__main__':
	main()
