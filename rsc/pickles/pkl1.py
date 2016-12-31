#data = pickle.loads( banner )
#
#print '\n'.join([''.join([p[0] * p[1] for p in row]) for row in data])

class Foo(  ):

	def __init__( self, **kwargs ):
		self.data = kwargs
		for key, value in kwargs.items(  ):
			setattr(self, key, value)

def foobar( self, foo="bar" ):
	new = ""
	for bar in foo:
		if ord( bar ) % 2 == 0 and bar.islower(): new += str( ord( bar ) )
		elif ord( bar ) % 2 == 0 and bar.isupper(): new += bar
		elif bar.isupper(  ): new += str( ord( bar ) )
		else: new += bar

	return new
	



foo = Foo(  )
foo.foobar = foobar


import pickle 	# serialization
				# pickle can store object's attribbutes

output = open( "save1.pkl", "wb" ) # open in writebinary
pickle.dump( foo, output, -1 ) #object file [protocol], 			many times dumped -->
output.close(  )