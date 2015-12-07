import pygame as p
import random

class Stars( object ):

	nebulalist = [  ]

	@classmethod
	def update( self, pt ):

		self.pt = pt
		self.pl = pt.player

		for g in range( 3 - len( self.nebulalist ) ):

			starlist = [  ]

			for i in range( 1000 ):

				starlist.append( [ random.randrange( - pt.scr.get_width(  ), 2 * pt.scr.get_width(  ) ),
										random.randrange( - pt.scr.get_height(  ), 2 * pt.scr.get_height(  ) ) ] )

			self.nebulalist.append( starlist )

		for g in range( len( self.nebulalist ) ):

			for i in self.nebulalist[ g ]:

				i[ 0 ] += self.pl.vx / 5.0 / ( g + 1 )
				i[ 1 ] += self.pl.vy / 5.0 / ( g + 1 )

	@classmethod
	def draw( self ):

		for g in range(len(self.nebulalist)):

			for i in self.nebulalist[ g ]:

				if i[ 0 ] - 10 < self.pt.scr.get_width(  ) and i[ 1 ] - 10 < self.pt.scr.get_height(  ) and \
					i[ 0 ] + 10 > 0 and i[ 1 ] + 10 > 1:

					p.draw.circle( self.pt.scr, (255,255,255), (int(i[0]),int(i[1])), len(self.nebulalist) - g )