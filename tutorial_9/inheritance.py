# Section 9.5
# https://docs.python.org/3.11/tutorial/classes.html#inheritance


class Base():

	def f1(self):
		print(50 * '-')
		print('f1() from Base class')
		self.f2()

	def f2(self):
		print(50 * '-')
		print('f2() from Base class')

class Derived(Base):

	def f2(self):
		print(50 * '^')
		print('f2() from Derived class')

def main():

	b = Base()
	d = Derived()

	b.f1()
	d.f1()

if __name__ == '__main__':
	main()
