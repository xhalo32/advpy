class A():
	
	def __init__(self):

		self.a = "a"

	def prints(self):

		print self.a

a = A()

a.prints()

def b(self):

	print "asdfb"

A.b = b

a.b()