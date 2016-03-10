import pygame as p
from math import sin, cos, tan

class Projectiles:

	class REGULAR:

		def __init__( self, data ):

			for a in data:
				setattr( self, a, data[ a ] )

			self.dead = False

		def update( self ):

			self.pos[ 0 ] += self.speed

			if self.pos[ 0 ] > self.scr.get_width(  ):
				self.dead = 1


			temp = self.game.stars.layerls[ 0 ]
			for star in self.game.stars.layerls[ 0 ]:
				if self.pos[ 0 ] - self.length < star[ 0 ] < self.pos[ 0 ] and \
				   self.pos[ 1 ] - 5 < star[ 1 ] < self.pos[ 1 ] + 5:

					temp.remove( star )
					self.dead = 1

			self.game.stars.layerls[ 0 ] = temp

		def draw( self ):

			p.draw.line( self.scr, self.color, [ self.pos[ 0 ] - self.length, self.pos[ 1 ] ], self.pos, 2 )

		## --- ##

	def __init__( self, game ):

		self.game = game
		self.projectilelist = [  ]

	def update( self ):

		l = self.projectilelist

		for p in self.projectilelist:
			p.update(  )

			if p.dead: l.remove( p )

		self.projectilelist = l

	def draw( self ):

		for p in self.projectilelist:
			p.draw(  )