import pygame as p
import math
from projectile_types import Types
from complex import complex

rad = ( 180.0 / math.pi )



class Projectile( object ):

	class Unit( object ):

		def __init__( self, parent, data ):

			self.parent = parent
			self.damage = data[ "damage" ]
			self.radius = data[ "radius" ]
			self.speed = data[ "speed" ]
			self.angle = data[ "angle" ]
			self.color = data[ "color"]
			self.pos = data[ "pos" ]
			self.dad = data[ "dad" ]

			try: self.type = getattr( Types, data[ "type" ] )( self )
			except: self.type = Types.DEFAULT( self )

			self.scr = parent.scr
			self.dead = False
			self.timer = 0

		def update( self ):

			self.type.update(  )

		def draw( self ):

			self.type.draw(  )

		## --- ##

	def __init__( self, parent ):

		self.parent = parent
		self.scr = parent.scr

		self.projectiles = []

	def udpate( self ):

		tt = []

		for u in self.projectiles:

			u.update()

			if u.dead:
				tt.append(u)

		for t in tt:
			self.projectiles.remove( t )

	def draw( self ):
		
		for u in self.projectiles:

			u.draw()

	def mkUnit( self, parent, color, angle, radius, speed, damage, pos ):

		data = { 
			"dad" : parent,
			"color" : color,
			"angle" : angle,
			"radius" : radius,
			"speed" : speed,
			"damage" : damage,
			"pos" : pos,
			}

		self.projectiles.append(
				self.Unit( self, data )
			)

	def mkRPG( self, parent, color, angle, radius, speed, damage, pos ):

		data = { 
			"dad" : parent,
			"color" : color,
			"angle" : angle,
			"radius" : radius,
			"speed" : speed,
			"damage" : damage,
			"pos" : pos,
			"type" : "TRAIL"
			}

		self.projectiles.append(
				self.Unit( self, data )
			)