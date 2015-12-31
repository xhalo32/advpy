import pygame as p
from math import *
import sys
sys.path.append( "/home/toor/Desktop/advpy/rsc/" )
from acomplex import acomplex
from complex import complex

def lessen_color( color, index ):

	rcolor = [  ]
	for i in color:
		i -= index
		if i < 0:
			i = 0
		if i > 255:
			i = 255
		rcolor.append( i )
	return rcolor



class EntityTypes:

	class PARTICLE:
		def __init__( self, par ):

			self.par = par
			self.s = self.par.parent.s
			self.x, self.y, self.w, self.h = self.par.pos
			self.color = self.par.color

			self.vector = self.par.vector

			self.dead = False

		def update( self ):

			self.x += self.vector[ "speed" ] * cos( self.vector[ "angle" ] / ( 180.0 / pi ) )
			self.y += self.vector[ "speed" ] * sin( self.vector[ "angle" ] / ( 180.0 / pi ) )
			angle = self.par.parent.timer % 360
			self.vector[ "angle" ] = angle

		def draw( self ):

			p.draw.rect( self.s, self.color, ( int( self.x ), int( self.y ), int( self.w ), int( self.h ) ) )

	class SHADE_PARTICLE:
		def __init__( self, par ):

			self.par = par
			self.s = self.par.parent.s
			self.s_size = self.s.get_size(  )
			self.x, self.y, self.w, self.h = self.par.pos
			self.par.x = self.x
			self.par.y = self.y
			self.color = self.par.color
			self.lifetimer = 0
			self.hitmeter = 0

			self.vector = self.par.vector

			self.lenght = self.par.lenght
			self.addtime = self.par.addtime
			self.shadelist = [  ]

			self.dead = False

		def update( self ):

			self.lifetimer += 1

			self.x += self.vector[ "speed" ] * cos( self.vector[ "angle" ] / ( 180.0 / pi ) )
			self.y += self.vector[ "speed" ] * sin( self.vector[ "angle" ] / ( 180.0 / pi ) )
			self.par.x = self.x
			self.par.y = self.y

			if self.par.parent.timer % self.addtime == 0:

				self.shadelist.append( [ self.x, self.y ] )
				if len( self.shadelist ) > self.lenght:
					del self.shadelist[ 0 ]


			if self.x > self.s_size[ 0 ]:
				self.vector[ "angle" ] = 180 + ( ( 360 - self.vector[ "angle" ] ) % 360 )
				self.x = self.s_size[ 0 ]
				self.hitmeter += 1

			if self.x + self.w < 0:
				self.vector[ "angle" ] = 180 + ( ( 360 - self.vector[ "angle" ] ) % 360 )
				self.x = 0 - self.w
				self.hitmeter += 1

			if self.y > self.s_size[ 1 ]:
				self.vector[ "angle" ] = ( ( 360 - self.vector[ "angle" ] ) % 360 )
				self.y = self.s_size[ 1 ]
				self.hitmeter += 1

			if self.y + self.h < 0:
				self.vector[ "angle" ] = ( ( 360 - self.vector[ "angle" ] ) % 360 )
				self.y = 0 - self.h
				self.hitmeter += 1


			if self.lifetimer > 600:
				self.w -= 0.1
				self.h -= 0.1

			if self.hitmeter >= 3:
				self.w -= 0.1
				self.h -= 0.1

			if self.w < 0 or self.h < 0:
				self.dead = True

		def draw( self ):

			d = 0
			for s in self.shadelist:

				if d > 255: d = 255
				su = p.Surface( ( int( self.w ), int( self.h ) ) )

				su.set_alpha( d )
				su.fill( self.color )
				self.s.blit( su, ( int( s[ 0 ] ), int( s[ 1 ] ) ) )

				d += 255.0 / len( self.shadelist )

			p.draw.rect( self.s, self.color, ( int( self.x ), int( self.y ), int( self.w ), int( self.h ) ) )

	class MOVEABLE_SHADE_PARTICLE:
		def __init__( self, par ):

			self.par = par
			self.s = self.par.parent.s
			self.x, self.y, self.w, self.h = self.par.pos
			self.vx = self.vy = 0
			self.color = self.par.color

			self.vector = self.par.vector

			self.lenght = self.par.lenght
			self.addtime = self.par.addtime
			self.shadelist = [  ]

			self.dead = False

		def update( self ):

			from main import teste

			if teste( self.par.parent.events, "D", "K_d" ): self.vx = self.vector[ "speed" ]
			if teste( self.par.parent.events, "D", "K_a" ): self.vx = -self.vector[ "speed" ]
			if teste( self.par.parent.events, "D", "K_w" ): self.vy = -self.vector[ "speed" ]
			if teste( self.par.parent.events, "D", "K_s" ): self.vy = self.vector[ "speed" ]
			
			if teste( self.par.parent.events, "U", "K_d" ) and self.vx > 0: self.vx = 0
			if teste( self.par.parent.events, "U", "K_a" ) and self.vx < 0: self.vx = 0
			if teste( self.par.parent.events, "U", "K_w" ) and self.vy < 0: self.vy = 0
			if teste( self.par.parent.events, "U", "K_s" ) and self.vy > 0: self.vy = 0
			
			self.x += self.vx
			self.y += self.vy

			if self.par.parent.timer % self.addtime == 0 and \
					( self.vx > 0 or self.vx < 0 or self.vy > 0 or self.vy < 0 ):

				self.shadelist.append( [ self.x, self.y ] )

				if len( self.shadelist ) > self.lenght:
					del self.shadelist[ 0 ]

		def draw( self ):

			d = 0
			for s in self.shadelist:

				if d > 255: d = 255
				su = p.Surface( ( int( self.w ), int( self.h ) ) )

				su.set_alpha( d )
				su.fill( self.color )
				self.s.blit( su, ( int( s[ 0 ] ), int( s[ 1 ] ) ) )

				d += 96.0 / len( self.shadelist )

			p.draw.rect( self.s, self.color, ( int( self.x ), int( self.y ), int( self.w ), int( self.h ) ) )

	class MOVEABLE_SHADE_CIRCLE_PARTICLE:
		def __init__( self, par ):

			self.par = par
			self.s = self.par.parent.s
			self.x, self.y, self.r = self.par.pos
			self.vx = self.vy = 0
			self.color = self.par.color

			self.vector = self.par.vector

			self.lenght = self.par.lenght
			self.addtime = self.par.addtime
			self.shadelist = [  ]

			self.dead = False

		def update( self ):

			from main import teste

			if teste( self.par.parent.events, "D", "K_d" ): self.vx = self.vector[ "speed" ]
			if teste( self.par.parent.events, "D", "K_a" ): self.vx = -self.vector[ "speed" ]
			if teste( self.par.parent.events, "D", "K_w" ): self.vy = -self.vector[ "speed" ]
			if teste( self.par.parent.events, "D", "K_s" ): self.vy = self.vector[ "speed" ]
			
			if teste( self.par.parent.events, "U", "K_d" ) and self.vx > 0: self.vx = 0
			if teste( self.par.parent.events, "U", "K_a" ) and self.vx < 0: self.vx = 0
			if teste( self.par.parent.events, "U", "K_w" ) and self.vy < 0: self.vy = 0
			if teste( self.par.parent.events, "U", "K_s" ) and self.vy > 0: self.vy = 0
			
			self.x += self.vx
			self.y += self.vy

			if self.par.parent.timer % self.addtime == 0 and \
					self.vx > 0 or self.vx < 0 or self.vy > 0 or self.vy < 0:

				self.shadelist.append( [ self.x, self.y ] )
				if len( self.shadelist ) > self.lenght:
					del self.shadelist[ 0 ]


		def draw( self ):

			d = 0
			for s in self.shadelist:

				if d > 255: d = 255
				su = p.Surface( ( int( 2 * self.r ), int( 2 * self.r ) ), p.SRCALPHA )

				sl = list( self.color )
				sl.append( d )
				p.draw.circle( su, sl, [ int( self.r ), int( self.r ) ], self.r )
				self.s.blit( su, ( int( s[ 0 ] - self.r ), int( s[ 1 ] - self.r ) ) )

				d += 64.0 / self.lenght

			p.draw.circle( self.s, self.color, ( int( self.x ), int( self.y ) ), int( self.r ) )

	class MOVEABLE_SHADE_POLYGON_PARTICLE:
		def __init__( self, par ):

			self.par = par
			self.s = self.par.parent.s
			self.x, self.y, self.w, self.h = self.par.pos
			self.vx = self.vy = 0
			self.rot = 0
			self.color = self.par.color

			self.vector = self.par.vector

			self.lenght = self.par.lenght
			self.addtime = self.par.addtime
			self.shadelist = [  ]

			self.dead = False

		def update( self ):

			from main import teste

			if teste( self.par.parent.events, "D", "K_d" ): self.vx = self.vector[ "speed" ]
			if teste( self.par.parent.events, "D", "K_a" ): self.vx = -self.vector[ "speed" ]
			if teste( self.par.parent.events, "D", "K_w" ): self.vy = -self.vector[ "speed" ]
			if teste( self.par.parent.events, "D", "K_s" ): self.vy = self.vector[ "speed" ]
			
			if teste( self.par.parent.events, "U", "K_d" ) and self.vx > 0: self.vx = 0
			if teste( self.par.parent.events, "U", "K_a" ) and self.vx < 0: self.vx = 0
			if teste( self.par.parent.events, "U", "K_w" ) and self.vy < 0: self.vy = 0
			if teste( self.par.parent.events, "U", "K_s" ) and self.vy > 0: self.vy = 0
			
			self.x += self.vx
			self.y += self.vy
			self.rot += self.par.rotspeed


			if self.par.parent.timer % self.addtime == 0 and \
					( self.vx > 0 or self.vx < 0 or self.vy > 0 or self.vy < 0 ):

				self.shadelist.append( [ self.x, self.y, self.rot ] )

				if len( self.shadelist ) > self.lenght:
					del self.shadelist[ 0 ]

		def draw( self ):

			d = 0
			for s in self.shadelist:

				if d > 255: d = 255
				su = p.Surface( ( int( 2 * self.w ), int( 2 * self.w ) ), p.SRCALPHA )

				sl = list( self.color )
				sl.append( d )
				complex.regpolygon( su, sl, [ int( self.w ), int( self.w ) ], int( self.w ), 4, s[ 2 ] )
				
				self.s.blit( su, [ int( s[ 0 ] - self.w ), int( s[ 1 ] - self.w ) ] )

				d += 128.0 / len( self.shadelist )

			acomplex.aregpolygon( self.s, self.color, ( int( self.x ), int( self.y ) ), int( self.w ), 4, self.rot )

	class JUMPABLE_SHADE_POLYGON_PARTICLE:
		def __init__( self, par ):

			self.par = par
			self.s = self.par.parent.s
			self.x, self.y, self.w = self.par.pos
			self.vx = self.par.vector[ "speed" ]
			self.vy = 0
			self.rot = 0
			self.sprint = 0, 0
			self.color = self.par.color

			self.vector = self.par.vector

			self.lenght = self.par.lenght
			self.addtime = self.par.addtime
			self.shadelist = [  ]

			self.dead = False

		def update( self ):

			from main import teste

			if teste( self.par.parent.events, "D", "K_w" ): self.vy -= 4

			self.vy += .1
			if abs( self.vx ) > self.par.vector[ "speed" ]:
				self.vx -= self.vx / 15.0

			if self.sprint[ 0 ] != 0:
				self.sprint = list( self.sprint )[ 0 ] - 1, list( self.sprint )[ 1 ]
				try:
					self.vx = ( self.vx / abs( self.vx ) ) * self.sprint[ 1 ]
				except: pass

			else:
				self.sprint = 0, 0

			if self.x > self.s.get_width(  ):
				self.vx *= -1
				self.par.rotspeed *= -1
				self.x = self.s.get_width(  )

			if self.x < 0:
				self.vx *= -1
				self.par.rotspeed *= -1
				self.x = 0

			if self.y < 0:
				self.vy *= -0.5
				self.y = 0

			if self.y > self.s.get_height(  ):
				self.vy *= -0.5
				self.y = self.s.get_height(  )

			self.x += self.vx
			self.y += self.vy
			self.rot -= self.par.rotspeed

			if self.par.parent.timer % self.addtime == 0 and \
					( self.vx > 0 or self.vx < 0 or self.vy > 0 or self.vy < 0 ):

				self.shadelist.append( [ self.x, self.y, self.rot ] )

				if len( self.shadelist ) > self.lenght:
					del self.shadelist[ 0 ]

		def draw( self ):

			d = 0
			for s in self.shadelist:

				if d > 255: d = 255
				su = p.Surface( ( int( 2 * self.w ), int( 2 * self.w ) ), p.SRCALPHA )

				sl = list( self.color )
				sl.append( d )
				complex.regpolygon( su, sl, [ int( self.w ), int( self.w ) ], int( self.w ), self.par.gon, s[ 2 ] )
				
				self.s.blit( su, [ int( s[ 0 ] - self.w ), int( s[ 1 ] - self.w ) ] )

				d += 128.0 / len( self.shadelist )

			acomplex.aregpolygon( self.s, self.color, ( int( self.x ), int( self.y ) ), int( self.w ), self.par.gon, self.rot )
