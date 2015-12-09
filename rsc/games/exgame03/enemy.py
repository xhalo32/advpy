import pygame as p
import math, random

from complex import complex

rad = ( 180.0 / math.pi )

class Enemy( object ):

	class Opponent( object ):

		def __init__( self, parent, radius, health ):

			self.parent = parent
			self.player = parent.player
			self.scr = parent.scr
			self.size = parent.size
			self.projectile = parent.projectile

			self.pos = [self.x, self.y] = [ random.randint( 0, self.size[ 0 ] ), random.randint( 0, self.size[ 1 ] ) ]
			self.speed = 1
			self.radius = radius
			self.rotspeed = 5
			self.rotation = 0
			self.timer = 0
			self.radrotation = 0
			self.dead = False
			self.damage = 0
			self.health = health
			self.maxhealth = health
			self.healthcolor = [ 0, 0, 0 ]

		def update(self):

			self.timer += 1

			try:
				self.rotation = math.atan2( self.player.pos[ 0 ] - self.x,
				self.player.pos[ 1 ] - self.y ) * rad

			except:
				pass

			self.radrotation = self.rotation / rad + random.randrange( -1, 1 )

			self.x += - self.parent.player.vx / 2.0 + self.speed * math.sin( self.radrotation )
			self.y += - self.parent.player.vy / 2.0 + self.speed * math.cos( self.radrotation )

			self.pos = [ self.x, self.y ]

			if self.damage > 0 and self.health > 0:
				self.health -= self.damage
				self.damage = 0

			if self.health <= 0:
				self.dead = 1

			index = 255.0 / self.maxhealth
			self.healthcolor = [ int( 255 - index * self.health ), 
							     int( index * self.health ),
							     0 ]

			if self.timer % 70 == 0:

				self.shoot(  )

		def shoot( self ):

			self.parent.projectile.mkUnit( self, ( 255, 0, 100 ), self.rotation, 3, 8, 3, self.pos )

		def draw(self):
			
			complex.triangle( self.scr, (255, 20, 20), self.pos, self.radius, int( self.rotation ) - 30, usecenter=True )

			p.draw.rect( self.scr, self.healthcolor, [ self.pos[ 0 ] - 5*self.health,
												    self.pos[ 1 ] + self.radius, 10*self.health, 8] )



	def __init__( self, main ):

		self.main = main

		self.projectile = main.projectile
		self.player = main.player
		self.scr = main.scr
		self.size = main.size

		self.opponentlist = [  ]
		for i in range( 10 - len( self.opponentlist ) ):
			self.opponentlist.append( self.Opponent( self, 20, 10 ) )

	def update( self ):

		deads = [  ]
		for o in self.opponentlist:

			o.update(  )

			if o.dead:
				deads.append( o )

		for o in deads:

			self.opponentlist.remove( o )

	def draw( self ):

		for o in self.opponentlist:

			o.draw(  )