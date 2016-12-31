from math import *
import random, math
import pygame as p


def get_angle( dir ):
	if dir[ 0 ] == 0 and dir [ 1 ] == -1: return 90
	elif dir[ 0 ] == 1 and dir [ 1 ] == -1: return 45
	elif dir[ 0 ] == 1 and dir [ 1 ] == 0: return 0
	elif dir[ 0 ] == 1 and dir [ 1 ] == 1: return -45
	elif dir[ 0 ] == 0 and dir [ 1 ] == 1: return -90
	elif dir[ 0 ] == -1 and dir [ 1 ] == 1: return -135
	elif dir[ 0 ] == -1 and dir [ 1 ] == 0: return 180
	elif dir[ 0 ] == -1 and dir [ 1 ] == -1: return 135


def mkbuttons( index ):
	l = "U", "UR", "R", "DR", "D", "DL", "L", "UL"
	return l[ index ]

def triangle( pos, radius, rotation = 0, usecenter=True ):

	rad = 180.0 / pi

	radrot = -rotation / rad

	if usecenter:

		pos1 = pos[0] + radius * cos( radrot + 180 / rad ), \
		 	   pos[1] + radius * sin( radrot + 180 / rad )
		
		pos2 = pos[0] + radius * cos( radrot + 45 / rad ), \
			   pos[1] + radius * sin( radrot + 45 / rad )

		pos3 = pos[0] + radius * cos( radrot - 45 / rad ), \
			   pos[1] + radius * sin( radrot - 45 / rad )

	else:
		pos1 = pos

		pos2 = pos[0] + 2 * radius * cos( radrot + 30 / rad ), \
			   pos[1] + 2 * radius * sin( radrot + 30 / rad )

		pos3 = pos[0] + 2 * radius * cos( radrot - 30 / rad ), \
			   pos[1] + 2 * radius * sin( radrot - 30 / rad )

	return [ pos1, pos2, pos3 ]

def arrow( pos, direction, unit=1, delta=40, order="ULDR" ):
	u = unit
	p0, p1 = pos
	if direction == 0: # UP
		l =	[
				[ p0 + 4*u, p1 + 11*u ],
				[ p0 + 4*u, p1 - 3*u ],
				[ p0 + 12*u, p1 - 3*u ],

				[ p0, p1 - 15*u ],

				[ p0 - 12*u, p1 - 3*u ],
				[ p0 - 4*u, p1 - 3*u ],
				[ p0 - 4*u, p1 + 11*u ],
			]

		for a in range(len(l)):
			dm = -1.5 + order.index( "U" )
			l[ a ] = l[ a ][ 0 ] + dm*delta, l[ a ][ 1 ]
		return l

	if direction == 1: # LEFT
		l =	[
				[ p0 + 11*u, p1 - 4*u ],
				[ p0 - 3*u, p1 - 4*u ],
				[ p0 - 3*u, p1 - 12*u ],

				[ p0 - 15*u, p1 ],

				[ p0 - 3*u, p1 + 12*u ],
				[ p0 - 3*u, p1 + 4*u ],
				[ p0 + 11*u, p1 + 4*u ],
			]

		for a in range(len(l)):
			dm = -1.5 + order.index( "L" )
			l[ a ] = l[ a ][ 0 ] + dm*delta, l[ a ][ 1 ]
		return l

	if direction == 2: # DOWN
		l =	[
				[ p0 + 4*u, p1 - 11*u ],
				[ p0 + 4*u, p1 + 3*u ],
				[ p0 + 12*u, p1 + 3*u ],

				[ p0, p1 + 15*u ],

				[ p0 - 12*u, p1 + 3*u ],
				[ p0 - 4*u, p1 + 3*u ],
				[ p0 - 4*u, p1 - 11*u ],
			]

		for a in range(len(l)):
			dm = -1.5 + order.index( "D" )
			l[ a ] = l[ a ][ 0 ] + dm*delta, l[ a ][ 1 ]
		return l

	if direction == 3: # RIGHT
		l =	[
				[ p0 - 11*u, p1 - 4*u ],
				[ p0 + 3*u, p1 - 4*u ],
				[ p0 + 3*u, p1 - 12*u ],

				[ p0 + 15*u, p1 ],

				[ p0 + 3*u, p1 + 12*u ],
				[ p0 + 3*u, p1 + 4*u ],
				[ p0 - 11*u, p1 + 4*u ],
			]

		for a in range(len(l)):
			dm = -1.5 + order.index( "R" )
			l[ a ] = l[ a ][ 0 ] + dm*delta, l[ a ][ 1 ]
		return l



class Effect:

	class Particle:

		'''
		USE ALPHA IN EXPLOSIONS
		'''
		MAX_GRAPHICS = 0

		def __init__( self, scr, color, pos, radius, angle, speed, drag, world ):

			self.scr = scr
			self.color = color
			self.radius = radius
			self.angle = angle
			self.speed = speed
			self.drag = drag
			self.pos = pos
			self.world = world
			#[ self.vwsx, self.vwsy ] = world.vwsx / 3.0, world.vwsy / 3.0

		def update( self ):

			#[ self.vwsx, self.vwsy ] = self.world.vwsx / 3.0, self.world.vwsy / 3.0

			self.speed /= self.drag
			rad = 180.0 / math.pi
			self.pos[ 0 ] += self.speed * math.cos( self.angle / rad ) # - self.vwsx
			self.pos[ 1 ] += self.speed * math.sin( self.angle / rad ) # - self.vwsy

		def draw( self ):
	
			size = self.scr.get_size( )

			if self.MAX_GRAPHICS:
				s = p.Surface( size, p.SRCALPHA )

				p.draw.circle( 
				s, self.color, [ int( self.pos[ 0 ] ), int( self.pos[ 1 ] ) ],
				int( self.radius ) ) 

				self.scr.blit( s, [ 0, 0 ] )
			else:
				p.draw.circle( 
				self.scr, self.color, [ int( self.pos[ 0 ] ), int( self.pos[ 1 ] ) ],
				int( self.radius ) ) 


			## --- ##

	class Explode:

		def __init__( self, parent, color, color2, size, speed, amount, lifetime, pos, opacity=255 ):

			self.parent = parent
			self.size = size
			self.speed = speed
			self.color = color
			self.color2 = color2
			self.pos = pos
			self.opacity = opacity
			self.scr = 			parent.scr
			self.borders = 		parent.size
			self.amount = amount

			self.particles = [  ]
			self.dead = False
			self.timer = lifetime

			for i in range( self.amount ):

				angle = 360.0 / self.amount

				x = self.pos[0]
				y = self.pos[1]

				self.particles.append( 

					self.parent.Particle( 
						self.scr,
						[ random.random() * ( self.color[ 0 ] - self.color2[ 0 ] ) + self.color2[ 0 ],
						  random.random() * ( self.color[ 1 ] - self.color2[ 1 ] ) + self.color2[ 1 ],
						  random.random() * ( self.color[ 2 ] - self.color2[ 2 ] ) + self.color2[ 2 ],
						  self.opacity, ],
						[ x, y ],
						self.size * random.randint( 1, 4 ),
						i * angle,
						self.speed + random.randint( -20, 20 ) / 4.0,
						1.03 + random.randint( 0, 10 ) / 100.0,
						self.parent.parent	) )

		def update( self ):

			self.timer -= 1
			if self.timer <= 0:
				self.dead = True

			for i in self.particles:
				i.update(  )

				if self.timer < 20 and i.radius > 0:
					i.radius -= .3

		def draw( self ):

			size = self.scr.get_size(  )

			for i in self.particles:
				i.draw(  )

	class Explode2:

		def __init__( self, parent, color, colorindex, size, speed, amount, lifetime, pos, angle ):

			self.parent = parent
			self.size = size
			self.speed = speed
			self.color = color
			self.colorindex = colorindex
			self.pos = pos
			self.scr = parent.scr
			self.borders = parent.size
			self.amount = amount
			self.angle = angle

			self.particles = [  ]
			self.dead = False
			self.timer = lifetime

			for i in range( self.amount ):

				x = self.pos[ 0 ]
				y = self.pos[ 1 ]

				self.particles.append( 

					self.parent.Particle( 
						self.scr,
						[ self.color[ 0 ] - random.randint( 0, self.colorindex[ 0 ] ),
						  self.color[ 1 ] - random.randint( 0, self.colorindex[ 1 ] ),
						  self.color[ 2 ] - random.randint( 0, self.colorindex[ 2 ] ), 
						  self.color[ 3 ], ],
						[ x, y ],
						self.size * random.randint( 1, 4 ),
						90 - self.angle + random.randint( -25, 25 ),
						self.speed + random.randint( -20, 20 ) / 10.0,
						1.01 + random.randint( 0, 10 ) / 100.0,
						self.parent.parent	) )

		def update( self ):

			self.timer -= 1
			if self.timer <= 0:
				self.dead = True

			for i in self.particles:
				i.update(  )

				if self.timer < 20 and i.radius > 0:
					i.radius -= .3

		def draw( self ):

			size = self.scr.get_size(  )
			
			for i in self.particles:
				i.draw(  )

		## --- ##

	def __init__( self, parent ):

		self.parent = parent
		self.scr = parent.scr
		self.size = parent.size
		self.effects = [  ]

	def mkExplosion( self, color, color2, size, speed, amount, lifetime, pos, opacity=255 ):

		self.effects.append( self.Explode( self, color, color2, size, speed, amount, lifetime, pos, opacity ) )

	def mkExplosion2( self, color, colorindex, size, speed, amount, lifetime, pos, angle ):

		self.effects.append( self.Explode2( self, color, colorindex, size, speed, amount, lifetime, pos, angle ) )

	def update( self ):

		tt = [  ]
		for e in self.effects:
			e.update(  )

			if e.dead:
				tt.append( e )

		for e in tt:
			self.effects.remove( e )

	def draw( self ):

		for e in self.effects:
			e.draw(  )