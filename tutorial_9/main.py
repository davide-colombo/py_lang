# Section hidden
# Inspect module's __dict__ dictionary

import _main as imported_module

print('Inside module "main.py"')

if __name__ == '__main__':
	print(50 * '-')
	print("'__name__' = ", __name__)

	print(50 * '-')
	print('Read-only dictionary that defines the module-level namespace symbols')

	print('INSPECTING THE DICTIONARY')
	print()
	for key, val in imported_module.__dict__.items():
		vrepr = val.__repr__()[:30]
		vrepr2 = val.__repr__()[-30:]
		print(f'key = {key!r}, value = {vrepr}...{vrepr2}')
