import pygame as p
from random import *
from items import Items
from math import *

from balltypes import BallTypes

p.init(  )
p.font.init(  )

def msg( window, text, pos, color=( 255,255,255 ), size=25, bold=0, italic=0, centered=False ):
	font = p.font.SysFont( 'Ubuntu Mono', size, bold, italic )
	label = font.render( str( text ), 1, color )

	rect = label.get_rect(  )

	if centered:
		window.blit( label, [ int( pos[ 0 ] - rect[ 2 ] / 2. ), int( pos[ 1 ] -rect[ 3 ] / 2. ) ] )
	else:
		window.blit( label, pos )

def randcol( colors ):
	done = 0
	tries = 100
	while not done and tries > 0:
		rcolor = [  ]

		for c in range( 3 ):
			rcolor.append( colors[ c ][ randrange( 0, len( colors[ c ] ) ) ] )

		for a in rcolor:
			for b in rcolor:
				for c in rcolor:
					if a != b or a != c or b != c:
						done = 1
		tries -= 1
	return rcolor


class Main:

	class Ball:

		def __init__( self, par, radius, spd, color, t ):

			self.par = par
			self.orgspeed = spd[ 0 ]
			self.topspeed = spd[ 1 ]
			self.speed = self.orgspeed
			self.color = color
			self.r = radius
			self.angle = randint( 0, 359 )
			self.x, self.y = [ i / 2. for i in par.size ]

			self.treshold = 20
			self.hitcooldown = -1
			self.dead = False
			self.lasthit = None

			self.btype = t
			self.types = [  ]
			for t in self.btype:
				self.types.append( t( self ) )

		def update( self ):

			self.x += self.speed * cos( self.angle / ( 180. / pi ) )
			self.y += self.speed * sin( self.angle / ( 180. / pi ) )
			self.hitcooldown -= 1

			for p in ( self.par.p1, self.par.p2 ):
				if self.hitcooldown < 0:
					if self.x + self.r > p.x and self.x - self.r < p.x + p.w and \
					   self.y + self.r > p.y and self.y - self.r < p.y + p.h:

						self.angle %= 360
						
						print self.angle

						if p == self.par.p1: 
							if self.par.p1.m < 0: 
								if not ( 270 > self.angle > 220 ):
									self.angle += 30

							elif self.par.p1.m > 0:
								if not ( 90 < self.angle < 160 ):
									self.angle -= 30

						elif p == self.par.p2: 
							if self.par.p2.m < 0: 
								if not ( 270 < self.angle < 320 ):
									self.angle -= 30

							elif self.par.p2.m > 0:
								if not ( 90 > self.angle > 40 ):
									self.angle += 30

						self.angle = 180 + 360 - self.angle
						#+ ( 45 * ( self.y - (p.y + p.h / 2.) ) / ( p.h / 2. ) )    ##randint( -30, 30 ) ## angle on impact


						if p.x + p.w / 2 - self.x > 0:
							self.x = p.x - self.r
						elif p.x + p.w / 2 - self.x < 0:
							self.x = p.x + p.w + self.r

						p.ballhit = True
						self.hitcooldown = p.w / self.speed + 60
						self.lasthit = p

			if self.x - self.r > self.par.s.get_size(  )[ 0 ]:
				self.dead = True
				self.par.score[0] += 1

			elif self.x + self.r < 0:
				self.dead = True
				self.par.score[1] += 1

			if self.y + self.r > self.par.s.get_size(  )[ 1 ]:
				self.angle = ( ( 360 - self.angle ) % 360 ) + randint( -1, 1 )
				self.y = self.par.s.get_size(  )[ 1 ] - self.r

				if 270 < self.angle < 270 + self.treshold:
					self.angle += 1.5 * self.treshold

				if 270 > self.angle > 270 - self.treshold:
					self.angle += -1.5 * self.treshold

			elif self.y - self.r < 0:
				self.angle = ( ( 360 - self.angle ) % 360 ) + randint( -1, 1 )
				self.y = self.r

				if 90 < self.angle < 90 + self.treshold:
					self.angle += 1.5 * self.treshold

				if 90 > self.angle > 90 - self.treshold:
					self.angle += -1.5 * self.treshold

			for t in self.types:
				t.update(  )

		def draw( self ):

			for t in self.types:
				t.draw(  )

	class Paddle:

		def __init__( self, parent, player, ctrlup, ctrldn, side ):

			self.par = parent
			self.name = player
			self.up = ctrlup
			self.down = ctrldn
			self.color = [ 255, 255, 255 ]
			self.speed = 5
			self.timer = 0
			self.m = 0
			
			self.w = 20
			self.orgh = 60
			self.h = self.orgh
			self.y = self.par.size[ 1 ] / 2.
			self.ballhit = False

			if side == "LEFT": self.x = 20
			if side == "RIGHT": self.x = self.par.size[ 0 ] - 20 - self.w

		def update( self ):

			self.timer += 1
			self.y += self.m

			if not self.y >= 0: self.m = 0; self.y = 0
			if not self.y + self.h <= self.par.s.get_height(  ):
				self.m = 0; self.y = self.par.s.get_height(  ) - self.h

			for e in self.par.events:

				if self.y >= 0 and self.y + self.h <= self.par.s.get_height(  ):

					if e.type == p.KEYDOWN:
						if e.key == getattr( p, self.up ):
							self.m = -self.speed

						if e.key == getattr( p, self.down ):
							self.m = self.speed
							

				if e.type == p.KEYUP:
					if e.key == getattr( p, self.up ) and self.m < 0:
						self.m = 0
					if e.key == getattr( p, self.down ) and self.m > 0:
						self.m = 0

			self.ballhit = False

		def draw( self ):

			p.draw.rect( self.par.s, self.color,
				[ int( self.x ), int( self.y ), int( self.w ), int( self.h ) ] )



	def __init__( self ):

		self.size = ( 640, 480 )
		self.s = p.display.set_mode( self.size ) #, p.FULLSCREEN

		self.reset(  )
		self.debug = 0

	def reset( self ):

		self.p1 = self.Paddle( self, "P1", "K_w", "K_s", "LEFT" )
		self.p2 = self.Paddle( self, "P2", "K_UP", "K_DOWN", "RIGHT" )
		self.items = Items( self )
		self.end = False
		self.score = [0, 0]

		self.balllist = [  ]

		for i in range( 2 ):

			self.makeball()

	def makeball(self):
		
		cs = [ 63, 127, 255 ]
		c = [ cs[ randint( 0, 2 ) ],
			  cs[ randint( 0, 2 ) ],
			  cs[ randint( 0, 2 ) ] ]

		self.balllist.append( self.Ball( self, 8, ( 3, 4 ), c, ( BallTypes.SHADE, ) ) )

	def update( self ):
		
		self.p1.update(  )
		self.p2.update(  )

		l = list( self.balllist )
		for b in self.balllist:
			b.update(  )
			if b.dead: l.remove( b )
		self.balllist = l

		self.items.update(  )

		if len( self.balllist ) <= 0:
			self.end = True
			self.reset(  )

		for b in self.balllist:
			if b.speed < 6:
				b.speed += 1 / 600.

	def draw( self ):

		self.p1.draw(  )
		self.p2.draw(  )
		self.items.draw(  )

		for b in self.balllist:
			b.draw(  )

		if self.debug:

			for n in self.balllist:
				try:
					msg( self.s, n.lasthit.name, ( n.x, n.y - 20 ), size=20, centered=True )
				except:
					msg( self.s, n, ( n.x, n.y - 20 ), size=20 )


		msg( self.s, self.score[0], [self.s.get_width() / 2. - 40,30], size=40, centered=True )
		msg( self.s, self.score[1], [self.s.get_width() / 2. + 40,30], size=40, centered=True )

	def loop( self ):

		c = p.time.Clock(  )

		while 1:

			self.events = p.event.get(  )

			self.s.fill( ( 0,0,0 ) )

			for e in self.events:

				if e.type == p.QUIT:
					p.quit(  )
					quit(  )
				if e.type == p.KEYDOWN:
					if e.key == p.K_d:
						self.debug = self.debug * -1 + 1
					if e.key == p.K_ESCAPE:
						p.quit(  )
						quit(  )

			self.update(  )
			self.draw(  )

			p.display.flip(  )

			c.tick( 60 )
