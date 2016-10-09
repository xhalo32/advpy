import pygame as p
from random import *
from balltypes import BallTypes
from math import *



p.font.init(  )

def msg( window, text, pos, color=( 255,255,255 ), size=25, bold=0, italic=0, centered=False ):
	font = p.font.SysFont( 'Ubuntu Mono', size, bold, italic )
	label = font.render( str( text ), 1, color )

	rect = label.get_rect(  )

	if centered:
		window.blit( label, [ int( pos[ 0 ] - rect[ 2 ] / 2. ), int( pos[ 1 ] -rect[ 3 ] / 2. ) ] )
	else:
		window.blit( label, pos )


class Items:

	class ENERGY_DRINK:

		def __init__( self, main, lasts, level ):

			self.main = main
			self.p1 = main.p1
			self.p2 = main.p2

			size = main.s.get_size(  )
			self.x = randint( size[ 0 ] // 5, size[ 0 ] // ( 5. / 4. ) )
			self.y = randint( size[ 1 ] // 5, size[ 1 ] // ( 5. / 4. ) )
			self.w = 10
			self.h = 20

			self.timer = lasts
			self.level = level
			self.target = None
			self.dead = False
			self.vdead = False
			self.target_type = None

		def update( self ):

			if not self.vdead:
				for b in self.main.balllist:		

					if b.x + b.r > self.x and b.x - b.r < self.x + self.w and \
						b.y + b.r > self.y and b.y - b.r < self.y + self.h:

						b.speed += self.level
						self.target_type = BallTypes.SHADE( b )
						b.types.append( self.target_type )
						self.target = b
						self.vdead = 1

			if self.vdead:
				self.timer -= 1

				if self.timer < 0:
					self.target.speed -= self.level
					self.target.types.remove( self.target_type )
					self.dead = 1

		def draw( self ):

			from main import randcol
			if not self.vdead:

				c = randcol( ( [ 0 ], [ 200, 232, 255 ], [ 200, 232, 255 ] ) )
				p.draw.rect( self.main.s, c, [ self.x, self.y, self.w, self.h ] )

				msg( self.main.s, round( self.level, 1 ), [self.x + self.w/2. - 1, self.y + self.h/2. - 1], (0,0,0), size=13, centered=1 )
				msg( self.main.s, round( self.level, 1 ), [self.x + self.w/2., self.y + self.h/2.], size=13, centered=1 )

	class COFFEE:

		def __init__( self, main, lasts, level ):

			self.main = main
			self.p1 = main.p1
			self.p2 = main.p2

			size = main.s.get_size(  )
			self.x = randint( size[ 0 ] // 5, size[ 0 ] // ( 5. / 4. ) )
			self.y = randint( size[ 1 ] // 5, size[ 1 ] // ( 5. / 4. ) )
			self.w = 10
			self.h = 20

			self.timer = lasts
			self.level = float( level )
			self.target = None
			self.dead = False
			self.vdead = False
			self.target_type = None

		def update( self ):

			if not self.vdead:
				for b in self.main.balllist:		

					if b.x + b.r > self.x and b.x - b.r < self.x + self.w and \
						b.y + b.r > self.y and b.y - b.r < self.y + self.h:

						b.speed /= self.level
						self.target = b
						self.vdead = 1

			if self.vdead:
				self.timer -= 1

				if self.timer < 0:
					self.target.speed *= self.level
					self.dead = 1

		def draw( self ):

			from main import randcol
			if not self.vdead:

				c = randcol( ( [ 200, 232, 255 ], [ 170, 200, 227 ], [ 50, 90 ] ) )
				p.draw.rect( self.main.s, c, [ self.x, self.y, self.w, self.h ] )

				msg( self.main.s, round( self.level, 1 ), [self.x + self.w/2. - 1, self.y + self.h/2. - 1], (0,0,0), size=13, centered=1 )
				msg( self.main.s, round( self.level, 1 ), [self.x + self.w/2., self.y + self.h/2.], size=13, centered=1 )


	class LONGENER:

		def __init__( self, main, lasts, length ):

			self.main = main
			self.p1 = main.p1
			self.p2 = main.p2

			size = main.s.get_size(  )
			self.x = randint( size[ 0 ] // 5, size[ 0 ] // ( 5. / 4. ) )
			self.y = randint( size[ 1 ] // 5, size[ 1 ] // ( 5. / 4. ) )
			self.w = 20
			self.h = 20

			self.speed = 4
			self.colordepth = 200.
			self.timer = lasts
			self.length = length
			self.target = None
			self.dead = False
			self.vdead = False

		def update( self ):
			if not self.vdead:
				for b in self.main.balllist:		

					if b.x + b.r > self.x and b.x - b.r < self.x + self.w and \
						b.y + b.r > self.y and b.y - b.r < self.y + self.h:

						if b.lasthit != None and b.lasthit.h == b.lasthit.orgh:
							self.target = b.lasthit
							self.target_orgcolor = list( self.target.color )
							self.vdead = 1
							break

			if self.vdead:
				self.timer -= 1

					## LENGTH CHANGE
				if self.target.h < self.length + self.target.orgh and \
					self.timer > ( self.target.h - self.target.orgh ) / 2:

					self.target.h += self.speed
					self.target.y -= self.speed / 2.

				elif self.timer <= ( self.target.h - self.target.orgh ) / 2:
					self.target.h -= self.speed
					self.target.y += self.speed / 2.

					## COLOR CHANGE
				if self.colordepth / self.speed < self.timer < ( 2 * self.colordepth ) / self.speed:
					for i in range( 3 ):
						if i != 0:
							self.target.color[ i ] -= self.speed
							if self.target.color[ i ] < 255 - self.colordepth:
								self.target.color[ i ] = 255 - self.colordepth
				elif self.timer <= self.colordepth / self.speed:
					for i in range( 3 ):
						if i != 0:
							self.target.color[ i ] += self.speed
							if self.target.color[ i ] > 255:
								self.target.color[ i ] = 255

				if self.timer < 0:
					self.target.h = self.target.orgh
					self.target.color = self.target_orgcolor
					self.dead = 1

		def draw( self ):
			from main import randcol
			if not self.vdead:
				c = randcol( ( [ 255 ], [ 0, 127 ], [ 0, 127 ] ) )
				p.draw.rect( self.main.s, c, [ self.x, self.y, self.w, self.h ] )

				msg( self.main.s, int( self.length), [self.x + self.w/2. - 1, self.y + self.h/2. - 1], (0,0,0), size=13, centered=1 )
				msg( self.main.s, int( self.length), [self.x + self.w/2., self.y + self.h/2.], size=13, centered=1 )


	class SPEEDUP:

		def __init__( self, main, lasts, level ):

			self.main = main
			self.p1 = main.p1
			self.p2 = main.p2

			size = main.s.get_size(  )
			self.x = randint( size[ 0 ] // 5, size[ 0 ] // ( 5. / 4. ) )
			self.y = randint( size[ 1 ] // 5, size[ 1 ] // ( 5. / 4. ) )
			self.w = 10
			self.h = 20

			self.pulseindex = 10
			self.pulsespeed = 60
			self.timer = lasts
			self.level = level
			self.target = None
			self.dead = False
			self.vdead = False

		def update( self ):

			if not self.vdead:
				for b in self.main.balllist:		

					if b.x + b.r > self.x and b.x - b.r < self.x + self.w and \
						b.y + b.r > self.y and b.y - b.r < self.y + self.h:

						if b.lasthit != None:
							self.target = b.lasthit
							self.target.speed += self.level
							self.vdead = 1

			if self.vdead:
				self.timer -= 1

				if self.timer % self.pulsespeed > self.pulsespeed / 2.:
					for i in range( 3 ):
						if i != 2:
							self.target.color[ i ] -= self.pulseindex
							if self.target.color[ i ] < 0:
								self.target.color[ i ] = 0
				else:
					for i in range( 3 ):
						if i != 2:
							self.target.color[ i ] += self.pulseindex
							if self.target.color[ i ] > 255:
								self.target.color[ i ] = 255

				if self.timer < 0:
					self.target.speed -= self.level
					self.dead = 1

		def draw( self ):

			from main import randcol
			if not self.vdead:

				c = randcol( ( [ 0 ], [ 0 ], [ 200, 232, 255 ] ) )
				p.draw.rect( self.main.s, c, [ self.x, self.y, self.w, self.h ] )

				msg( self.main.s, round( self.level, 1 ), [self.x + self.w/2. - 1, self.y + self.h/2. - 1], (0,0,0), size=13, centered=1 )
				msg( self.main.s, round( self.level, 1 ), [self.x + self.w/2., self.y + self.h/2.], size=13, centered=1 )


	class TROLLER:

		def __init__( self, main, lasts, index ):

			self.main = main
			self.p1 = main.p1
			self.p2 = main.p2

			size = main.s.get_size(  )
			self.x = randint( size[ 0 ] // 5, size[ 0 ] // ( 5. / 4. ) )
			self.y = randint( size[ 1 ] // 5, size[ 1 ] // ( 5. / 4. ) )
			self.w = 15
			self.h = 10

			self.troll_index = index
			self.timer = lasts
			self.target = None
			self.dead = False
			self.vdead = False
			self.target_type = None

		def update( self ):

			if not self.vdead:
				for b in self.main.balllist:		

					if b.x + b.r > self.x and b.x - b.r < self.x + self.w and \
						b.y + b.r > self.y and b.y - b.r < self.y + self.h:

						b.troll_index = self.troll_index
						self.target_type = BallTypes.TROLL( b )
						b.types.append( self.target_type )
						self.target = b
						self.vdead = 1

			if self.vdead:
				self.timer -= 1

				if self.timer < 0:

					self.target.types.remove( self.target_type )
					self.dead = 1

		def draw( self ):

			from main import randcol
			if not self.vdead:

				c = randcol( ( [ 0 ], [ 200, 232, 255 ], [ 0 ] ) )
				p.draw.rect( self.main.s, c, [ self.x, self.y, self.w, self.h ] )


				msg( self.main.s, round( self.troll_index, 1 ), [self.x + self.w/2. - 1, self.y + self.h/2. - 1], (0,0,0), size=13, centered=1 )
				msg( self.main.s, round( self.troll_index, 1 ), [self.x + self.w/2., self.y + self.h/2.], size=13, centered=1 )



	class ADDBALL:

		def __init__( self, main, amount ):

			self.main = main
			self.p1 = main.p1
			self.p2 = main.p2

			size = main.s.get_size(  )
			self.x = randint( size[ 0 ] // 5, size[ 0 ] // ( 5. / 4. ) )
			self.y = randint( size[ 1 ] // 5, size[ 1 ] // ( 5. / 4. ) )
			self.w = 15
			self.h = 15

			self.ballamount = amount
			self.target = None
			self.dead = False
			self.vdead = False

		def update( self ):

			if not self.vdead:
				for b in self.main.balllist:		

					if b.x + b.r > self.x and b.x - b.r < self.x + self.w and \
						b.y + b.r > self.y and b.y - b.r < self.y + self.h:

						for i in range(self.ballamount):

							self.main.makeball()
							self.dead = 1

		def draw( self ):

			from main import randcol
			c = randcol( ( [ 200, 255 ], [ 200, 255 ], [ 200, 255 ] ) )
			p.draw.ellipse( self.main.s, c, [ self.x, self.y, self.w, self.h ] )


			msg( self.main.s, self.ballamount, [self.x + self.w/2. - 1, self.y + self.h/2. - 1], (0,0,0), size=13, centered=1 )
			msg( self.main.s, self.ballamount, [self.x + self.w/2., self.y + self.h/2.], size=13, centered=1 )


		# --- #



	def __init__( self, main ):

		self.main = main
		self.itemlist = [  ]

	def genrandom( self, amount ):

		for i in range(amount):

			num = randint( 0, 6 )
			print num

			if num == 0:
				self.itemlist.append( 
					self.ENERGY_DRINK( self.main, 	120 * random() + 300, 1.5 * random() + 0.5 ) )

			if num == 1:
				self.itemlist.append( 
					self.COFFEE( self.main, 		300 * random() + 300, 1.5 * random() + 0.5 ) )

			if num == 2:
				self.itemlist.append( 
					self.LONGENER( self.main, 		300 * random() + 300, 100 * random() + 100 ) )

			if num == 3:
				self.itemlist.append( 
					self.SPEEDUP( self.main, 		400 * random() + 300, 10 * random() + 5 ) )

			if num == 4:
				self.itemlist.append( 
					self.TROLLER( self.main, 		250 * random() + 300, 5 * random() + 5 ) )

			if num == 5:
				self.itemlist.append( 
					self.ADDBALL( self.main, 		int( 1 + sqrt( 10 * random() ) ) ) )
		

	def update( self ):

		while len(self.itemlist) < 8:
			self.genrandom( 1 )

		l = list( self.itemlist )
		for i in self.itemlist:
			i.update(  )

			if i.dead:
				l.remove( i )
		self.itemlist = l

	def draw( self ):

		for i in self.itemlist:
			i.draw(  )