import sys

while 1:
	done = False
	s = raw_input( ">>> " )
	try:
		if list( s.strip( " " ) )[ -1 ] == ":":
			while not done:
				d = raw_input( "... " )
				if d == "":
					s += "\n"
					done = True
				else:
					s = s + "\n" + d
		
		exec( s )

	except Exception as e:
		try:
			i = sys.exc_info(  )[ 1 ]
			print i[ 0 ] + " at: " + i[ 1 ][ 3 ].strip( "\n" )
		except: print e