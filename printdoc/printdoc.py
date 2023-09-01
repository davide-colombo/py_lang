# Program that reads a file and prints comments

OUTDIR = './out'

OPENING = '-start-'
CLOSING = '-end-'

if __name__ == '__main__':
	import sys
	import os
	if len(sys.argv) < 3:
		print("USAGE: python3 printdoc.py <dirname> <filename>")
		sys.exit(1)
	srcpath = os.path.join(sys.argv[1], sys.argv[2])
	if not os.path.exists(srcpath):
		print('ERROR: please provide an existing path')
		sys.exit(1)

	lines = []
	with open(srcpath, 'r', encoding='utf-8') as f:
		for line in f:
			if line.startswith('#'):
				lines.append(line.lstrip('# ').strip())

	dstpath = os.path.join(OUTDIR, 'out.txt')
	if not os.path.exists(OUTDIR):
		os.mkdir(OUTDIR)
	
	with open(dstpath, 'w', encoding='utf-8') as f:
		status = 0	# outside
		for line in lines:
			if line == OPENING:
				status = 1	# inside
				continue	# skip opening line
			elif line == CLOSING:
				status = 0	# outside

			if status == 1:
				f.write(line+'\n')
