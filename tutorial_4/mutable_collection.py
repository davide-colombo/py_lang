# Section 4.2
# https://docs.python.org/3.11/tutorial/controlflow.html

def main():
	# key: value
	users = {'edo34': 'active', "fra99": "inactive", "mary147": "active"}

	print(30 * "=")
	print(f'"users" type is "{type(users)}"')
	print(f'"users" value is: {users!r}')
	print(f'"users" memory location is "{hex(id(users))}"')
	print(f'"users" size in bytes is {getsizeof(users)}')
	
	users_copy = users.copy()
	print(30 * "=")
	print(f'"users_copy" type is "{type(users_copy)}"')
	print(f'"users_copy" value is: {users_copy!r}')
	print(f'"users_copy" memory location is "{hex(id(users_copy))}"')
	print(f'"users_copy" size in bytes is {getsizeof(users_copy)}')

	# MEMORY ADDRESS DIFFERENCE
	mem_addr_diff = abs(id(users_copy) - id(users))
	
	print(30 * "=")
	print(f'abs(id(users_copy) - id(users)) = {mem_addr_diff} bytes')
	if mem_addr_diff != getsizeof(users):
		print("'users_copy' and 'users' are NOT stored contiguosly")
	else:
		print("'users_copy' and 'users' ARE stored contiguosly")
	
	# if we need to remove an object from a collection
	# while iterating over the collection, it is better
	# to take a copy
	for user, status in users.copy().items():
		if status == 'inactive':
			del users[user]

	# ALTERNATIVE: create a new collection	
	active_users = {}

	print(30 * "=")
	print(f'"active_users" type is "{type(active_users)}"')
	print(f'{active_users = }')

	for user, status in users.items():
		if status == "active":
			active_users[user] = status

	print(30 * '=')
	print(f'{active_users = }')
	
	# In reality, it may not be useful to store the actual
	# status of the user, since we know that each one will
	# have a status equal to "active".
	gen_active_users = (user for user, status in users.items() if status == "active")

	print(30 * "=")
	print(f'"gen_active_users" type is "{type(gen_active_users)}"')
	print(f'"gen_active_users" value is: {gen_active_users!r}')

	s = ', '.join(gen_active_users)
	print(30 * "=")
	print(f'"s" type is "{type(s)}"')
	print(f'"s" value is: {s!r}')
	print(30 * "=")

	
if __name__ == '__main__':
	from sys import getsizeof
	main()
