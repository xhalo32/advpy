import pygame as p
import time

from math import *
from random import *

import utils, message


class Generator:

	def __init__( self, main ):

		self.main = main

		self.allowed_arrows = [ 0,2,4,6 ] #range( 0,8 ) [ 0,2,4,6 ]
		self.timer = 0

		self.generator_list = [] #[ 0, -30, 0, -30 ] # negative numbers for wait, positive for arrows
		self.wait = 0
		self.end = 0

		self.generator_list = self.generate_arrow_list( [ -30, -60, -15 ] + [ 0, 2, 4, 6 ], 10 )

	def generate_arrow_list( self, allowed, amount ):
		l = [  ]
		allowed_arrows = [ a for a in allowed if a >= 0 ]
		allowed_timings = [ a for a in allowed if a < 0 ]

		for i in range( amount ):
			l.append( allowed_arrows[ randrange( len( allowed_arrows ) ) ] )
			l.append( allowed_timings[ randrange( len( allowed_timings ) ) ] )


		l.append( -240 ) # ending wait
		return l

	def read( self, l ):

		if len( l ) == 0: return
		
		if isinstance( l[ 0 ], int ):
			if l[ 0 ] >= 0:

				for player in self.main.handler.playerlist: 				# generate arrow for each player
					player.totalarrows += 1
					self.main.handler.create_arrow( pos=[ player.pos[ 0 ], -50 ], _color=( 20, 70, 255 ),
								button=utils.mkbuttons( l[ 0 ] ), owner=player )

			elif l[ 0 ] < 0:
				self.queue_wait( -l[ 0 ] )

		elif isinstance( l[ 0 ], str ):
			if "/" in l[ 0 ]:
				t = 60.0 / int( l[ 0 ].split( "/" )[ 1 ] )
				self.queue_wait( t )

		del l[ 0 ]

	def queue_wait( self, wait ):
		if self.wait != 0: print "wait time interrupted"
		self.wait = wait - 2

	def generate_beatlines( self, width=220, color=(200,200,255), delta=60, offset=0 ):

		if self.generator_list:
			for player in self.main.handler.playerlist:
				if self.timer % delta == offset: self.main.handler.effect.mkBeatLine(
					color, [ player.pos[ 0 ], -50 ], [ width, 2 ], 3 )

	def ending( self ):

		for p in self.main.handler.playerlist:
				try: ratio = float(p.hits)/p.arrows_gone_by
				except: ratio = 0

				self.main.handler.effect.mkPopUpMessage(
					(225*(1-ratio), 225*ratio, 0), [ p.pos[ 0 ], self.main.size[ 1 ]/2. ],
					str( format( round( ratio * 100, 2 ), ".2f" ) ) + "%", 80, 300, { "italic" : 1, "perfect" : int( ratio ) } )
		

	def update( self ):

		self.generate_beatlines(  )
		self.generate_beatlines( color=( 220,220,255 ), offset=30 )

		self.timer += 1

		if self.wait == 0: self.read( self.generator_list )
		elif self.wait > 0: self.wait -= 1

		if not self.generator_list and not self.wait and not self.end:								# end of the game
			self.end = 1
			self.ending(  )

