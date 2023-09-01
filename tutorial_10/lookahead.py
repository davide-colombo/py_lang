# Demonstrate lookahead

import re

def main():
	strings = [
		'sample.foo',
		'file.rc',
		'README.md',
		'template.json',
		'config.yaml',
		'sample.bat',
		'model.batch'
	]

	p = re.compile(r'.*[.](?!bat$)[^.]*')
	for s in strings:
		m = p.match(s)
		if m:
			print(50 * '-')
			print('match found')
			print(f"{m = }")
			print(f"{s = }")
		else:
			print(50 * '~')
			print('NOT A MATCH')
			print(f'{p = }')
			print(f'{s = }')

if __name__ == '__main__':
	main()
