import pygame as p
from random import randrange

class Player:

	def __init__( self, game ):

		self.game = game

		self.x = 100
		self.y = self.game.main.scr.get_height(  ) / 2.
		self.color = [ 0, 255, 127 ]
		self.speed = 5
		self.vy = 0
		self.vx = 0

	def shoot( self ):

		self.game.projectiles.projectilelist.append( self.game.projectiles.REGULAR( {
			"game":self.game,
			"speed":6,
			"color":( 255, 0, 0 ),
			"scr":self.game.main.scr,
			"pos":[ int( self.x ), int( self.y ) ],
			"length":5 } ) )

	def update( self ):

		for e in self.game.main.events:
			if e.type == p.KEYDOWN:
				if e.key == p.K_w:
					self.vy = -self.speed
				elif e.key == p.K_s:
					self.vy = self.speed

				elif e.key == p.K_a:
					self.vx = -self.speed
				elif e.key == p.K_d:
					self.vx = self.speed

				elif e.key == p.K_SPACE:
					self.shoot(  )

			if e.type == p.KEYUP:
				if e.key == p.K_w and self.vy < 0:
					self.vy = 0
				elif e.key == p.K_s and self.vy > 0:
					self.vy = 0

				elif e.key == p.K_a and self.vx < 0:
					self.vx = 0
				elif e.key == p.K_d and self.vx > 0:
					self.vx = 0

		self.y += self.vy
		self.x += self.vx

		if self.y < 10: self.y = 10
		if self.y > self.game.main.scr.get_height(  ) - 10: self.y = self.game.main.scr.get_height(  ) - 10
		if self.x < 10: self.x = 10
		if self.x > 200: self.x = 200


		temp = self.game.stars.layerls[ 0 ]
		for star in self.game.stars.layerls[ 0 ]:
			if self.x - 10 < star[ 0 ] < self.x and \
			   self.y - 5 < star[ 1 ] < self.y + 5:

				temp.remove( star )
		self.game.stars.layerls[ 0 ] = temp

	def draw( self ):

		p.draw.polygon( self.game.main.scr, self.color, [ [ self.x, self.y ], [ self.x - 10, self.y - 5 ], [ self.x - 10, self.y + 5 ] ] )