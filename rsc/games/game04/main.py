import pygame as p


import time
from random import *
from handler import *
from math import *

from message import *

import utils


p.init(  )
p.font.init(  )


class Main:

	def __init__( self ):

		self.size = ( 800, 600 )
		self.scr = p.display.set_mode( self.size )#, p.FULLSCREEN )
		self.active = 1

		self.reset(  )

		self.loop(  )

	def reset( self ):
		# wasd = 119 97 115 100
		# uldr = 273 276 274 275

		self.handler = Handler( self )

		self.handler.create_player( pos=[ 200, 500 ], color=( 200, 0, 255 ), ULDR=( 119,97,115,100 ) )
		
		self.handler.create_player( pos=[ 600, 500 ], color=( 0, 200, 255 ), ULDR=( 273,276,274,275 ), scoreboardside=1 )

		#self.handler.create_arrow( pos=[ 400, 0 ], color=( 20, 25, 255 ), button="U", owner=self.handler.playerlist[ 0 ] )

	def loop( self ):

		clk = p.time.Clock(  )

		while self.active:

			self.handler.update(  )

			self.scr.fill( [ x + 232 for x in ( 0,0,0 ) ] )

			self.handler.draw(  )

			clk.tick( 64 ) # tickrate
			

			p.display.update(  )