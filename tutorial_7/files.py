# Section 7.2
# https://docs.python.org/3.11/tutorial/inputoutput.html#reading-and-writing-files

WORKING_DIR = './testfiles'
FPREFIX = 'file'
MAX_NFILES = 10

import random

def read_from(path: str):
	print(50 * '-')
	print('read_from()')
	print(f'path = {path}')

	with open(path, 'r', encoding='utf-8') as f:
		content = f.read()

	if sys.getsizeof(content) > 30:
		content = content[:30]
	print(content)

def main(validated_paths):
	print(50 * '-')
	print('main()')

	for p in validated_paths:
		read_from(p)

def setupdir(dirpath: str = WORKING_DIR, fileprefix: str = FPREFIX, nfiles: int = 3):
	print(50 * '-')
	print('setupdir()')
	print(f'Creating a directory called "{dirpath}"...')

	if not os.path.exists(dirpath):
		os.mkdir(dirpath)

	print('Check number of file...')
	if nfiles < 1:
		raise ValueError('Invalid argument: number of files must be at least 1 or greater')
	
	if nfiles >= MAX_NFILES:
		nfiles = MAX_NFILES

	print(f'Creating #{nfiles} files...')

	paths = []
	files = [fileprefix + str(i) + '.txt' for i in range(1, nfiles+1)]
	for fname in files:
		filepath = os.path.join(dirpath, fname)
		print(f'{filepath = }')	

		with open(filepath, 'w', encoding='utf-8') as f:
			random_call = lambda: random.randint(1, 100)

			line = 'This is some content for ' + fname
			
			if random_call() > 50:
				f.write(line)

			if random_call() > 50:
				line = 'The moon is blue tonight'
			else:
				line = 'The sun is dark today'

			f.write(line)

			if random_call() > 50:
				line = 'The grocery store is open!'
			else:
				line = 'The grocery store is closed :('

		# Exiting the 'with' statement automatically closes the file!
		print(f'File at path "{filepath}" successfully created!')
		paths.append(filepath)

	return paths
			
	
if __name__ == '__main__':
	import sys
	import os

	nargs = len(sys.argv)
	if nargs > 1:
		files = [f for i, f in enumerate(sys.argv) if i > 0]
		valid_files = []
		for f in files:
			pth = os.path.join(WORKING_DIR, f)
			if not os.path.exists(pth):
				print('Actually creating file...')
				random_call = lambda: random.randint(1, 30)
				with open(pth, 'w', encoding='utf-8') as fd:
					if random_call() > 15:
						fd.write('Created a new file from the command line name ' + f)

					if random_call() > 12:
						fd.write('The roses are red')
					else:
						fd.write('Your sunglasses are very bad!')

					if random_call() > 7:
						fd.write('This year I will spend newyear\'s eve in Austria, Vienna')
					else:
						fd.write('This year I will spend Christma\'s eve in Thailand, Bankok')
				
				print(f'file at "{pth}" successfully created!')
				valid_files.append(pth)

			elif os.path.isfile(pth):
				print(f'{f} is a file!')
				valid_files.append(pth)
			else:
				print(f'{pth} exists but it is not a file')
			
		valid_files.extend([os.path.join(WORKING_DIR, fname) for fname in os.listdir(WORKING_DIR) if os.path.isfile(os.path.join(WORKING_DIR, fname))])
		# Call the program
		main(valid_files)
	else:
		paths = setupdir()
		main(paths)
