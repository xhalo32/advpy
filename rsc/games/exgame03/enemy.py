import pygame as p
import math, random

from pg_enhancements import Bars
from complex import complex

rad = ( 180.0 / math.pi )

class Enemy( object ):

	class Opponent( object ):

		def __init__( self, data ):

			self.data = data
			self.parent = data[ "self" ]
			self.radius = data[ "radius" ]
			self.speed = data[ "speed" ]
			self.health = data[ "health" ]
			self.accuracy = data[ "accuracy" ]
			self.color = data[ "color" ]
			self.shotspeed = data[ "shot" ][ "speed" ]
			self.shotradius = data[ "shot" ][ "radius" ]
			self.shotdamage = data[ "shot" ][ "damage" ]
			self.shotcolor = data[ "shot" ][ "color" ]

			self.player = self.parent.player
			self.scr = self.parent.scr
			self.size = self.parent.size
			self.projectile = self.parent.projectile

			self.pos = [ 
				-self.parent.parent.wsx / 2.0 + random.randint( - self.size[ 0 ], self.size[ 0 ] ),
				-self.parent.parent.wsy / 2.0 + random.randint( - self.size[ 1 ], self.size[ 1 ] ) ]

			self.rotation = 0
			self.timer = 0
			self.radrotation = 0
			self.dead = False
			self.damage = 0
			self.maxhealth = self.health
			self.hpbar = Bars.DynamicHealthBar( self.scr, self.maxhealth )

		def update( self ):

			self.timer += 1

			try:
				self.rotation = math.atan2( self.player.pos[ 0 ] - self.pos[ 0 ],
				self.player.pos[ 1 ] - self.pos[ 1 ] ) * rad

			except:
				pass

			self.radrotation = self.rotation / rad

			self.pos[ 0 ] += - self.parent.parent.vwsx / 2.0 + self.speed * math.sin( self.radrotation )
			self.pos[ 1 ] += - self.parent.parent.vwsy / 2.0 + self.speed * math.cos( self.radrotation )

			if self.damage > 0 and self.health > 0:
				self.health -= self.damage
				self.damage = 0

			if self.health <= 0:
				self.dead = 1
				self.parent.parent.effectC.mkExplosion( ( 255, 0, 0 ), 2, 5, 50, 80, self.pos )

			index = 255.0 / self.maxhealth
			self.healthcolor = [ int( 255 - index * self.health ), 
							     int( index * self.health ),
							     0 ]

			if self.timer % 10 == 0:
				self.shoot(  )

		def shoot( self ):

			self.parent.projectile.mkUnit( 
				self,
				self.shotcolor,
				self.rotation + random.randint( -self.accuracy, self.accuracy ),
				self.shotradius, self.shotspeed, self.shotdamage,
				[ int( self.pos[ 0 ] ), int( self.pos[ 1 ] ) ] )

		def draw( self ):
			
			complex.triangle( self.scr, self.color, self.pos, self.radius, int( self.rotation ) - 30, usecenter=True )

			self.hpbar.draw( self.pos, self.health )

		## --- ##

	def __init__( self, parent ):

		self.parent = parent

		self.projectile = parent.projectile
		self.player = parent.player
		self.scr = parent.scr
		self.size = parent.size
		self.timer = 0

		self.opponentlist = [  ]
		self.totaldied = 0
		self.recentdied = 0

	def update( self ):

		self.timer += 1

		if self.timer % 2 == 0:
			for i in range( 10 - len( self.opponentlist ) ):

				data = { 
				"self" : self,
				"radius" : 15,
				"speed" : 2,
				"health" : 100,
				"accuracy" : 10,
				"color" : ( 255, 0, 0 ),

				"shot" : { 
					"damage" : 0.5,
					"speed" : 7,
					"radius" : 3,
					"color" : ( 0, 255, 255 ),
				 	},
				}

				self.opponentlist.append( self.Opponent( data ) )

		deads = [  ]
		for o in self.opponentlist:

			o.update(  )

			if o.dead:
				deads.append( o )

		for o in deads:

			self.opponentlist.remove( o )
			self.totaldied += 1
			self.recentdied += 1

	def draw( self ):

		for o in self.opponentlist:

			o.draw(  )