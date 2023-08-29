# Section 4.1
# https://docs.python.org/3.11/tutorial/controlflow.html

def main():
	x = 0
	while not x:
		try:
			x = int(input("Please, enter an integer: "))
		except ValueError:
			pass
		
	if x < 0:
		x = 0
		print("Negative changed to zero")
	elif x == 0:
		print("Zero")
	elif x == 1:
		print("One")
	else:
		print("More")

if __name__ == "__main__":
	main()
