import pygame as pg
import random
import message
import threading as thd

class Block:

	class Unit( object ):

		grav_effect = 1
		vy = vx = 0

		def __init__( self, data, block ):

			self.x, self.y, self.w, self.h = data
			self.block = block
			self.posdata = data
			self.rnd_posdata = ( self.w*( self.x // self.w ), self.h*( self.y // self.h ), self.w, self.h )

			self.col = ( 200, 0, 200 )

		def update( self ):

			self.posdata = self.x, self.y, self.w, self.h
			self.rnd_posdata = ( self.w*( self.x // self.w ), self.h*( self.y // self.h ), self.w, self.h )

			if round(self.vx, 0) != 0:
				self.vx /= 1.5

			else: self.vx = 0

			self.x += self.vx

	dragging = None
	pressure = 12
	gravityspeed = .25

	def __init__( self, scr ):

		self.scr = scr
		self.ulist = [  ]
		self.mrel = pg.mouse.get_rel(  )
		self.msg = message.Messages( self.scr )

		for x in range( 16 ):
			x = self.Unit( ( 200, 25 * x, 20, 20 ), self )
			self.ulist.append( x )

	def __call__( self, game, loop ):

		self.game = game
		self.loop = loop

	def create_unit( self ):

		mpos = pg.mouse.get_pos(  )
		x = self.Unit( ( mpos[ 0 ], mpos[ 1 ], 20, 20 ), self )
		self.ulist.append( x )

	def move( self ):

		if self.dragging != None:
			self.dragging.x += self.mrel[ 0 ]
			self.dragging.y += self.mrel[ 1 ]
			self.dragging.col = ( 55, 200, 170 )

		else: 
			for u in self.ulist:

				if pg.mouse.get_pos()[ 0 ] >= u.posdata[ 0 ] - self.mrel[ 0 ] and \
					pg.mouse.get_pos()[ 0 ] <= u.posdata[ 0 ] + u.posdata[ 2 ] + self.mrel[ 0 ]:

					if pg.mouse.get_pos()[ 1 ] >= u.posdata[ 1 ] - self.mrel[ 1 ] and \
						pg.mouse.get_pos()[ 1 ] <= u.posdata[ 1 ] + u.posdata[ 3 ] + self.mrel[ 1 ]:

						u.x += self.mrel[ 0 ]
						u.y += self.mrel[ 1 ]

						u.col = ( 15, 200, 150 )
						u.grav_effect = 0
						self.dragging = u

	def release( self ):

		if self.dragging != None: self.dragging.grav_effect = 1
		self.dragging = None

	def update( self ):
		tobeterminated = [  ]

		for u in range(len(self.ulist)):

			self.ulist[u].update(  )
			self.ulist[u].col = ( 200, 0, 200 )

			if self.ulist[u].x > self.scr.get_width(  ) or self.ulist[u].x + self.ulist[u].w < 0:
				tobeterminated.append( u )

			if self.ulist[u].grav_effect:

				if self.ulist[u].y + self.ulist[u].h < self.scr.get_height(  ):
					
					self.ulist[u].vy += self.gravityspeed
					self.ulist[u].y += self.ulist[u].vy

				else: 
					self.ulist[u].y = self.scr.get_height(  ) - self.ulist[u].h
					self.ulist[u].vy = 0

		try:
			for u in tobeterminated:
				del self.ulist[u]
		except:
			pass

		self.mrel = pg.mouse.get_rel(  )

		self.hit_test(  )

	def hit_test( self ):

		for u in self.ulist:
			for o in self.ulist:

				if u != o:

					## test for overlap

					if u.y + u.h >= o.y and u.y <= o.y + o.h:

						if u.x + u.h >= o.x and u.x <= o.x + o.w:

							##test for sides

							if u.x + u.w < o.x + o.w / 3:

								if o == self.dragging:
									o.x = u.x + o.w
									u.x = o.x - u.w

								elif u == self.dragging:
									u.x = o.x - u.w
									o.x = u.x + o.w

							if u.y + u.h < o.y + o.h / 2:

								if o == self.dragging:
									o.y = u.y + o.h
									u.y = o.y - u.h

								elif u == self.dragging:
									u.y = o.y - u.h
									o.y = u.y + o.h

								u.y = o.y - u.h ; u.vy = o.vy

							##test for total overlap:

							if u.x + u.w / 2 - u.w / 2 < o.x + o.w / 2 and u.x + u.w / 2 + u.w / 2 > o.x + o.w / 2 and \
							   u.y + u.h / 2 - u.h / 2 < o.y + o.h / 2 and u.y + u.h / 2 + u.h / 2 > o.y + o.h / 2:

								u.vx = self.pressure + random.randint( 0, 5 )
								o.vx = -u.vx

	def draw( self ):

		for u in self.ulist:
			pg.draw.rect( self.scr, u.col, u.posdata )

		if self.dragging != None:
			pg.draw.rect( self.scr, self.dragging.col, self.dragging.posdata )

		self.msg.message( len( self.ulist ), [ 10, 570 ] )