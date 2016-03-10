import pygame as p
from random import randrange

class Stars:

	def __init__( self, game ):

		self.game = game
		self.layerls = [  ]
		self.amount = 100
		self.layers = 3

		for l in range( self.layers ):
			temp = [  ]
			for i in range( self.amount ):
				temp.append( [ randrange( 0, 2 * self.game.main.scr.get_width(  ) ), 
							   randrange( 0, self.game.main.scr.get_height(  ) ) ] )

			self.layerls.append( temp )

	def move( self, pxls ):

		for l in range( len( self.layerls ) ):
			for i in self.layerls[ l ]:
				i[ 0 ] -= float( pxls ) / float( l + 1 )

	def gen_layer( self, layer ):

		temp = [  ]
		for i in range( self.amount ):
			temp.append( [ randrange( self.game.main.scr.get_width(  ), 3 * self.game.main.scr.get_width(  ) ), 
						   randrange( 0, self.game.main.scr.get_height(  ) ) ] )

		layer += temp

	def tick( self ):

		for l in range( len( self.layerls ) ):
			res = 0
			for i in self.layerls[ l ]:
				if i[ 0 ] < self.game.main.scr.get_width(  ):
					res += 1
			if res == len( self.layerls[ l ] ):
				self.gen_layer( self.layerls[ l ] )


		ll = self.layerls
		for l in range( len( self.layerls ) ):
			for i in self.layerls[ l ]:
				if i[ 0 ] < -10:
					ll[ l ].remove( i )
		self.layerls = ll


	def draw( self ):

		for l in range( len( self.layerls ) ):
			for i in self.layerls[ l ]:
				p.draw.circle( self.game.main.scr, ( 255 - l, 255 - l, 255 - l ), [ int( i[ 0 ] ), int( i[ 1 ] ) ], int( 2. / ( l + 1 ) ) )