from itertools import *
digits = "123456789ABCD"
base = len( digits ) + 1




def tobase10( l, base ):
	ib10 = 0
	for j in range(len(l)):
		num = digits.index( str( l[ len(l) - j - 1 ] ) ) + 1
		ib10 += base ** j * num
	return int( ib10 )



def polydivisible( l ):
	p = 1

	num = str( l )

	for i in range( 1, len( num )+1 ):
		if tobase10( num[ 0:i ], base ) % i == 0: pass
		else:
			p = 0
			break

	return p


plist = list( permutations( list( digits ) ) )

for i in range(len(plist)):
	plist[ i ] = "".join( [ str( x ) for x in plist[ i ] ] )

#print plist

lpolys = [  ]
for i in plist:
	if polydivisible( i ): lpolys.append( i )


print

for i in lpolys: print i