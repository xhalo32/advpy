

class store( object ):

	def __init__( self, func ):
		self.func = func
		self.cache = {}

	def __call__( self, *args ):

		value = self.func( *args )
		self.cache[ args ] = value
		print value, "@", self.func.__name__

@store
def trol( n ):
	return str( n ) + " keh"

for i in range( 5 ):
	print trol( str( i // 2 ) )