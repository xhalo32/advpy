import pygame as p
from random import *

class BallTypes:

	class NONE:

		def __init__( self, par ):
			self.par = par
		def update( self ):
			pass
		def draw( self ):
			p.draw.circle( self.par.par.s, self.par.color, [ int( self.par.x ), int( self.par.y ) ], int( self.par.r ) )
		
	class SHADE:

		def __init__( self, par ):
			self.par = par
			self.shadelist = [  ]
			self.alpha = 60

		def update( self ):
			par = self.par
			self.shadelist.append( [ par.x, par.y, par.r, par.color ] )

			if len( self.shadelist ) > 20:
				del self.shadelist[ 0 ]


		def draw( self ):
			for s in self.shadelist:
				su = p.Surface( ( 2 * s[ 2 ], 2 * s[ 2 ] ), p.SRCALPHA )
				c = list( s[ 3 ] )
				c.append( self.alpha )
				p.draw.circle( su, c, [ s[ 2 ], s[ 2 ] ], s[ 2 ] )
				self.par.par.s.blit( su, ( s[ 0 ] - s[ 2 ], s[ 1 ] - s[ 2 ] ) )

			p.draw.circle( self.par.par.s, self.par.color, [ int( self.par.x ), int( self.par.y ) ], int( self.par.r ) )

	class DISTORT:

		def __init__( self, par ):
			self.par = par
			self.distortioin = 2

		def update( self ):
			pass

		def draw( self ):
			p.draw.circle( self.par.par.s, self.par.color,
				[ int( self.par.x + randint( int( -self.distortioin ), int( self.distortioin ) ) ),
				  int( self.par.y + randint( int( -self.distortioin ), int( self.distortioin ) ) ) ], int( self.par.r ) )

	class TROLL:

		def __init__( self, par ):
			self.par = par
			self.trollnes = 0
			try:self.trollindex = par.troll_index
			except: self.trollindex = 5

		def update( self ):

			self.trollnes = randint( int( -self.trollindex ), int( self.trollindex ) )
			self.par.angle += self.trollnes

		def draw( self ):
			p.draw.circle( self.par.par.s, self.par.color,
				[ int( self.par.x ),
				  int( self.par.y ) ], int( self.par.r ) )