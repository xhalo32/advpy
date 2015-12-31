import pygame as pg
import math, random
import sys
sys.path.append( "/home/toor/Desktop/advpy/rsc/" )
from complex import complex

rad = ( 180.0 / math.pi )



class Types:

	class DEFAULT:

		def __init__( self, projectile ):

			self.prj = projectile

		def update( self ):

			self.prj.vwsx = self.prj.parent.parent.vwsx
			self.prj.vwsy = self.prj.parent.parent.vwsy

			self.prj.timer += 1

			if  self.prj.timer > self.prj.lifetime:
				self.prj.dead = True

			self.prj.pos[ 0 ] += self.prj.speed * math.cos( ( 90 - self.prj.angle ) / rad ) - self.prj.vwsx / 3.0
			self.prj.pos[ 1 ] += self.prj.speed * math.sin( ( 90 - self.prj.angle ) / rad ) - self.prj.vwsy / 3.0
			p = self.prj.pos

			for e in [e for e in self.prj.parent.parent.entitylist if e != self.prj.dad ]:
				
				if p[ 0 ] - self.prj.radius < e.pos[ 0 ] + e.radius and \
				   p[ 0 ] + self.prj.radius > e.pos[ 0 ] - e.radius and \
				   p[ 0 ] + self.prj.radius > e.pos[ 0 ] - e.radius and \
				   p[ 0 ] - self.prj.radius < e.pos[ 0 ] + e.radius and \
				   p[ 1 ] - self.prj.radius < e.pos[ 1 ] + e.radius and \
				   p[ 1 ] + self.prj.radius > e.pos[ 1 ] - e.radius and \
				   p[ 1 ] + self.prj.radius > e.pos[ 1 ] - e.radius and \
				   p[ 1 ] - self.prj.radius < e.pos[ 1 ] + e.radius:

				   self.prj.dead = True
				   e.damage += self.prj.damage

		def draw( self ):

			complex.vector( self.prj.scr, self.prj.color, self.prj.pos, self.prj.angle - 90,
				2 * self.prj.speed, self.prj.radius )

	class TRAIL:

		def __init__( self, projectile ):

			self.prj = projectile
			self.effectC = self.prj.parent.parent.effectC

			self.prj.expradius = self.prj.data[ "exp" ][ "radius" ]
			self.prj.expspeed = self.prj.data[ "exp" ][ "speed" ]
			self.prj.expamount = self.prj.data[ "exp" ][ "amount" ]
			self.prj.explife = self.prj.data[ "exp" ][ "lifetime" ]
			self.prj.colorindex = self.prj.data[ "colorindex"]

		def update( self ):

			self.prj.vwsx = self.prj.parent.parent.vwsx
			self.prj.vwsy = self.prj.parent.parent.vwsy

			self.prj.timer += 1

			if self.prj.timer > self.prj.lifetime:

				self.effectC.mkExplosion2(
					self.prj.color,
					self.prj.colorindex,
					self.prj.expradius,
					self.prj.expspeed,
					self.prj.expamount,
					self.prj.explife,
					self.prj.pos,
					self.prj.angle )

				self.prj.dead = True

			self.prj.pos[ 0 ] += self.prj.speed * math.cos( ( 90 - self.prj.angle ) / rad ) - self.prj.vwsx / 3.0
			self.prj.pos[ 1 ] += self.prj.speed * math.sin( ( 90 - self.prj.angle ) / rad ) - self.prj.vwsy / 3.0
			p = self.prj.pos

			if self.prj.timer % 1 == 0:
				for e in [e for e in self.prj.parent.parent.entitylist if e != self.prj.dad ]:
					
					if p[ 0 ] - self.prj.radius < e.pos[ 0 ] + e.radius and \
					   p[ 0 ] - self.prj.radius < e.pos[ 0 ] + e.radius and \
					   p[ 1 ] - self.prj.radius < e.pos[ 1 ] + e.radius and \
					   p[ 1 ] - self.prj.radius < e.pos[ 1 ] + e.radius and \
					   p[ 0 ] + self.prj.radius > e.pos[ 0 ] - e.radius and \
					   p[ 0 ] + self.prj.radius > e.pos[ 0 ] - e.radius and \
					   p[ 1 ] + self.prj.radius > e.pos[ 1 ] - e.radius and \
					   p[ 1 ] + self.prj.radius > e.pos[ 1 ] - e.radius:

						self.prj.dead = True
						e.damage += self.prj.damage
						
						self.effectC.mkExplosion2(
							self.prj.color,
							self.prj.colorindex,
							self.prj.expradius,
							self.prj.expspeed,
							self.prj.expamount,
							self.prj.explife,
							self.prj.pos,
							self.prj.angle )

			if self.prj.timer % 1 == 0:
				for e in [ e for e in self.prj.parent.projectiles if e != self if e.dad != self.prj.dad ]:

					if p[ 0 ] - self.prj.radius < e.pos[ 0 ] + e.radius and \
					   p[ 0 ] - self.prj.radius < e.pos[ 0 ] + e.radius and \
					   p[ 1 ] - self.prj.radius < e.pos[ 1 ] + e.radius and \
					   p[ 1 ] - self.prj.radius < e.pos[ 1 ] + e.radius and \
					   p[ 0 ] + self.prj.radius > e.pos[ 0 ] - e.radius and \
					   p[ 0 ] + self.prj.radius > e.pos[ 0 ] - e.radius and \
					   p[ 1 ] + self.prj.radius > e.pos[ 1 ] - e.radius and \
					   p[ 1 ] + self.prj.radius > e.pos[ 1 ] - e.radius:

						e.dead = True
						self.prj.dead = True
						self.effectC.mkExplosion2(
							self.prj.color,
							self.prj.colorindex,
							self.prj.expradius,
							self.prj.expspeed,
							self.prj.expamount,
							self.prj.explife,
							self.prj.pos,
							self.prj.angle )

		def draw( self ):

			complex.vector( self.prj.scr, self.prj.color, self.prj.pos, self.prj.angle - 90,
				2 * self.prj.speed, self.prj.radius )

			for i in range( 2 ):

				complex.vector( self.prj.scr, ( 255, 100, 0 ),
					self.prj.pos,
					self.prj.angle + 90 + random.randint( -20, 20 ),
					2 * self.prj.radius, 4 )