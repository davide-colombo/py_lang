# Section 5.1.2
# https://docs.python.org/3.11/tutorial/datastructures.html#using-lists-as-queues

def deq():
	print(50 * '-')
	print('deq()')

	# A queue provides the best way to have fast
	# appends and pops from both ends!
	
	queue = deque(["David", "Lucas", "Vanilla"])
	print(queue)

	print(50 * '-')
	print('append an entry')
	
	queue.append('Henry IV')
	print(queue)

	print(50 * '-')
	print('queue.popleft()')
	wholeft = queue.popleft()
	print(queue)
	print(f'"{wholeft}" left the queue')

	print(50 * '-')
	print('queue.pop()')
	wholeft = queue.pop()
	print(queue)
	print(f'"{wholeft}" left the queue')

if __name__ == '__main__':
	from collections import deque
	deq()
