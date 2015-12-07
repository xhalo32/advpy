class A(  ):
	
	def __init__( self, arg, qarg ):

		setattr( self, arg, qarg )
		self.name = "haihai"

	def __getitem__( self, arg ):

		return getattr( self, arg )

	def __setitem__( self, arg, qarg ):

		setattr( self, arg, qarg )

	def __str__( self ):

		return self.name



a = A( "adsf", 123 )

a[ "lh" ] = ( "kaatti", "kukko" )

print a[ "lh" ]
print a[ "adsf" ]

print a