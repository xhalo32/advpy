import pygame as p
import math, random
import sys
sys.path.append( "/home/toor/Desktop/advpy/rsc/" )

from pg_enhancements import Bars
from complex import complex

rad = (180.0 / math.pi)

class Player():

	def __init__(self, parent):

		self.parent = parent
		self.scr = parent.scr
		self.size = parent.size

		self.projectile = parent.projectile

		self.pos = [self.x, self.y] = [ s / 2 for s in self.size ]

		self.vx = self.vy = self.svx = self.svy = 0.0
		self.speed = 5
		self.radius = 15
		self.rotation = 0
		self.damage = 0
		self.dead = False

		self.maxhealth = 15
		self.prot = 0
		self.health = self.maxhealth
		self.hpbar = Bars.DynamicHealthBar( self.scr, self.maxhealth )
		self.rocketshoot_timer = 0

	def shoot( self, data ):

		self.projectile.mkUnit( data )

	def rocketshoot( self ):

		self.rocketshoot_timer = 30
		data = {
			"dad" : self,
			"color" : ( 250, 250, 0, 125 ),
			"colorindex" : ( 20, 100, 0 ),
			"angle" : self.rotation,
			"radius" : 3,
			"speed" : 18,
			"damage" : 100,
			"lifetime" : 30,
			"pos" : self.pos,
			"type" : "TRAIL",
			"exp" : { 
					"radius" : 2,
					"speed" : 5,
					"amount" : 2,
					"lifetime" : 30,
				}
			}

		for i in range( 10 ):
			data[ "angle" ] = self.rotation + random.randint( -10, 10 )
			self.projectile.mkUnit( data )

	def update( self ):

		self.rocketshoot_timer -= 1
		mpos = p.mouse.get_pos()

		try:
			self.rotation = math.atan2( mpos[0] - self.x, mpos[1] - self.y ) * rad
		except:
			pass

		self.svx = self.vx / 2.0
		self.svy = self.vy / 2.0

		self.x += self.svx
		self.y += self.svy

		self.pos = [ self.x, self.y ]

		v1 = self.vx * math.cos( ( 90 - self.rotation ) / rad )
		v2 = self.vy * math.sin( ( 90 - self.rotation ) / rad )

		if int( v1 ) == 0:
			v2 *= math.sqrt( 2 )

		elif int( v2 ) == 0:
			v1 *= math.sqrt( 2 )

		avg = ( v1 + v2 ) // 2

		if avg > 1:

			self.parent.effectC.mkExplosion2(
				( 255, 170, 0, 200 ), ( 0,100,0 ), avg / 2.0, 2 * avg, 10, 2 * avg,
				self.pos, 180 + self.rotation )

		if self.damage > 0 and self.health > 0:
			try:
				self.health -= self.damage / self.prot
			except:
				self.health -= self.damage / ( self.prot + 1 )

			self.damage = 0

		if self.health <= 0:
			self.health = 0
			self.dead = 1

		if self.dead:
			self.parent.restart(  )

	def draw(self):
		
		complex.triangle( self.scr, (255, 20, 255), self.pos, self.radius, int( self.rotation ) - 30, usecenter=True )

		self.hpbar.draw( self.pos, self.health )