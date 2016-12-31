import pygame as p
import time

from math import *
from random import *

import utils, message


class Player:

	def __init__( self, main, **kwargs ):

		self.main = main

		self.press = { "up" : 0, "left" : 0, "down" : 0, "right" : 0 }
		self.dead = 0
		self.points = self.combo = self.misclicks = self.misses = self.hits = 0
		self.arrows_gone_by = 0
		self.timer = 0

		for arg in kwargs:
			setattr( self, arg, kwargs[ arg ] )

		self.main.handler.create_arrow( pos=[ self.pos[ 0 ], 0 ], _color=( 20, 100, 255 ),
				button=utils.mkbuttons( randint( 0,7 ) ), owner=self )

	def wrong( self ):
		self.misclicks += 1
		self.combo = 0

	def miss( self ):
		self.combo = 0
		self.misses += 1

	def hit( self ):
		self.points += 1 + self.combo / 10.0
		self.combo += 1
		self.hits += 1

	def draw( self ):
		
		p.draw.rect( self.main.scr, self.color, ( self.pos[ 0 ] - 100, self.pos[ 1 ], 200, 10 ) )

		try: per = str( round( float(self.hits)/self.arrows_gone_by * 100, 2 ) ) + "%"
		except: per = ""
		message.msg( self.main.scr,
			str(self.hits) + "/" + str(self.arrows_gone_by) + " " + per,
			[ 100, 10 ], (0,0,100) )
		message.msg( self.main.scr, self.points, [ 10, 10 ], (0,0,100) )
		message.msg( self.main.scr, self.combo, [ 10, 40 ], (0,100,0) )
		message.msg( self.main.scr, self.misclicks, [ 10, 70 ], (100,20,0) )
		message.msg( self.main.scr, self.misses, [ 10, 100 ], (100,100,0) )

		message.msg( self.main.scr, self.main.handler.totalarrows, [ 400, 20 ], (100,200,230) )

	def update( self ):
		self.timer += 1
		self.arrow_in_reach = 0

		for arrow in self.main.handler.arrowlist:
			if arrow.limits[ 0 ] - 20 < self.pos[ 1 ] - arrow.pos[ 1 ] < arrow.limits[ 1 ] + 20: self.arrow_in_reach = 1; break


		for e in self.main.handler.events:
			if e.type == p.KEYDOWN:

				if   e.key == self.ULDR[ 0 ]: self.press[ "up" ] = time.time(  )
				elif e.key == self.ULDR[ 1 ]: self.press[ "left" ] = time.time(  )
				elif e.key == self.ULDR[ 2 ]: self.press[ "down" ] = time.time(  )
				elif e.key == self.ULDR[ 3 ]: self.press[ "right" ] = time.time(  )

		if not self.arrow_in_reach:
			for button in self.press:
				if time.time(  ) - self.press[ button ] < 1 / 100.0: self.wrong(  )



		if self.timer % 30 == 0:
			self.main.handler.create_arrow( pos=[ self.pos[ 0 ], 0 ], _color=( 20, 100, 255 ),
					button=utils.mkbuttons( randint( 0,7 ) ), owner=self )