import pickle

infile = open( "save1.pkl", "rb" )
bar = pickle.load( infile )					# <-- will need as many times loaded
print "Returned", bar
infile.close(  )


#print bar.foobar( "The quick brown fox jumps over the lazy dog" )