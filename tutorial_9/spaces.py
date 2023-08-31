# Section 9.2.1
# https://docs.python.org/3.11/tutorial/classes.html#scopes-and-namespaces-example


def scope_test():

	# NOTE: these are INNER functions!!
	def do_local():
		spam = "do_local()"

	def do_nonlocal():
		nonlocal spam
		spam = 'do_nonlocal()'

	def do_global():
		global spam
		spam = 'do_global()'

	# ======================================================================
	# NOTE: this MUST be present, otherwise using the 'nonlocal' qualifier
	# raises a 'SyntaxError'!!!

	# Why is this the case?
	# Because since the 'nonlocal' qualifier refers to an outer namespace
	# (i.e., a namespace between the local and the global) BUT there could
	# be potentially many of them, it just rebound the 'spam' name in the
	# first namespace it encounters outside the 'local' namespace!
	# ======================================================================
	
	spam = 'scope_test()'

	print(50 * '-')
	print('scope_test()')

	do_local()
	print('After local assignment:', spam)

	do_nonlocal()
	print('After nonlocal assignment:', spam)

	# ======================================================================
	# NOTE: 'do_global()' does not change the value of the object pointer to by 'spam' name
	# in the 'scope_test()' local namespace!!
	# ======================================================================
	
	do_global()			# this creates a new binding in the module's level namespace!
	print('After global assignment:', spam)

if __name__ == '__main__':
	scope_test()
	print('In global scope:', spam)
