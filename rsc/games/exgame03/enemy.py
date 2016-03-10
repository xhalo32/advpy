import pygame as p
import math, random
import sys
sys.path.append( "/home/toor/Desktop/advpy/rsc/" )

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
			self.prot = data[ "protection" ]
			self.accuracy = data[ "accuracy" ]
			self.color = data[ "color" ]
			self.shotspeed = data[ "shot" ][ "speed" ]
			self.shotradius = data[ "shot" ][ "radius" ]
			self.shotdamage = data[ "shot" ][ "damage" ]
			self.shotcolor = data[ "shot" ][ "color" ]
			self.colorindex = data[ "shot" ][ "expindex" ]
			self.shotrate = data[ "shot" ][ "rate" ]
			self.shotlife = data[ "shot" ][ "lifetime" ]

			self.effectC = self.parent.parent.effectC
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


			self.health += 1 / 20.


			if self.damage > 0 and self.health > 0:
				try:
					self.health -= self.damage / self.prot
				except:
					self.health -= self.damage / ( self.prot + 1 )


				if self.health <= 0:
					
					self.dead = 1

					self.effectC.mkExplosion( ( 255, 0, 0, 200 ),
						2 + self.damage / 100,
						5 + self.damage / 50,
						50 + self.maxhealth // 10,
						100, self.pos )

				self.damage = 0


			index = 255.0 / self.maxhealth
			self.healthcolor = [ int( 255 - index * self.health ), 
							     int( index * self.health ),
							     0 ]

			if self.timer % self.shotrate == 0:
				self.shoot(  )

		def shoot( self ):

			self.parent.projectile.mkUnit( {
			"dad" : self,
			"color" : self.shotcolor,
			"colorindex" : self.colorindex,
			"angle" : self.rotation + random.randint( -self.accuracy, self.accuracy ),
			"radius" : self.shotradius,
			"speed" : self.shotspeed,
			"damage" : self.shotdamage,
			"lifetime" : self.shotlife,
			"pos" : self.pos,
			"type" : "DEFAULT",
			"exp" : { 
					"radius" : 3,
					"speed" : 5,
					"amount" : 5,
					"lifetime" : 40,
				},
			} )

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
		self.opponent_amount = 3
		self.totaldied = 0
		self.recentdied = 0

	def update( self ):

		self.timer += 1

		if self.timer % 10 == 0:
			for i in range( self.opponent_amount - len( self.opponentlist ) ):

				data = { 
				"self" : self,
				"radius" : 20,
				"speed" : 2,
				"health" : 10,
				"protection" : 0,
				"accuracy" : 3,
				"color" : ( 255, 0, 0 ),

				"shot" : {
					"damage" : .1,
					"lifetime" : 50,
					"speed" : 10,
					"radius" : 4,
					"rate" : 2,
					"color" : ( 0, 255, 255, 100 ),
					"expindex" : ( 0, 100, 100 ),
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